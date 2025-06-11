# cluster_profiler.py

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 🔧 Simulazione dati per training (da sostituire in produzione con X reale)
num_cols_valid = ['età del paziente dimesso', 'tipdim', 'barthel_totale_ingresso', 'totale_scimric'] + [f'intproc{i}' for i in range(1, 11)]
cat_cols = ['sesso', 'età_clinica']

df_sim = pd.DataFrame({
    "età del paziente dimesso": np.random.randint(60, 90, 1000),
    "sesso": np.random.choice(["uomo", "donna"], 1000),
    "età_clinica": np.random.choice(["adulto", "anziano", "grande_anziano"], 1000),
    "tipdim": np.random.randint(1, 5, 1000),
    "barthel_totale_ingresso": np.random.randint(20, 80, 1000),
    "totale_scimric": 49,
    **{f"intproc{i}": np.random.normal(9200 + i*10, 50, 1000) for i in range(1, 11)}
})

df_sim_encoded = pd.get_dummies(df_sim, drop_first=True)

# 🔧 Fit dei preprocessori e modello
num_imputer = SimpleImputer(strategy="median")
cat_imputer = SimpleImputer(strategy="constant", fill_value="missing")
scaler = StandardScaler()

X_sim_scaled = scaler.fit_transform(df_sim_encoded)
kmeans = KMeans(n_clusters=2, random_state=42, n_init='auto')
kmeans.fit(X_sim_scaled)

def predict_cluster(nuovo_paziente_raw: pd.DataFrame) -> tuple:
    # Fit solo sulle colonne giuste
    num_imputer.fit(df_sim[num_cols_valid])
    cat_imputer.fit(df_sim[cat_cols])

    # Imputazione del nuovo paziente
    nuovo_num = pd.DataFrame(
        num_imputer.transform(nuovo_paziente_raw[num_cols_valid]),
        columns=num_cols_valid
    )
    nuovo_cat = pd.DataFrame(
        cat_imputer.transform(nuovo_paziente_raw[cat_cols]),
        columns=cat_cols
    )

    # Dummy encoding
    nuovo_df = pd.get_dummies(pd.concat([nuovo_num, nuovo_cat], axis=1), drop_first=True)

    # Allineamento colonne
    for col in df_sim_encoded.columns:
        if col not in nuovo_df.columns:
            nuovo_df[col] = 0
    nuovo_df = nuovo_df[df_sim_encoded.columns]

    # Scaling
    nuovo_scaled = scaler.transform(nuovo_df)

    # Predizione
    cluster_pred = kmeans.predict(nuovo_scaled)[0]

    messaggio = {
        0: "🔹 Cluster 0 – Paziente fragile, età avanzata, bassa autonomia all’ingresso, probabile degenza più lunga.",
        1: "🔸 Cluster 1 – Paziente mediamente più autonomo, età leggermente inferiore, possibile degenza più breve."
    }

    return cluster_pred, messaggio[cluster_pred]


# 📥 ESEMPIO DI USO
if __name__ == "__main__":
    nuovo_paziente = pd.DataFrame([{
        "età del paziente dimesso": 87,
        "sesso": "donna",
        "età_clinica": "grande_anziano",
        "tipdim": 1,
        "barthel_totale_ingresso": 36,
        "totale_scimric": 49,
        **{f"intproc{i}": 9200 + i*10 for i in range(1, 11)}
    }])

    cluster, spiegazione = predict_cluster(nuovo_paziente)
    print(f"\n📍 Cluster predetto: {cluster}")
    print(spiegazione)