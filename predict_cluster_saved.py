# predict_cluster_saved.py

import pandas as pd
import joblib

# Caricamento modelli
kmeans = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")
num_imputer = joblib.load("models/num_imputer.pkl")
cat_imputer = joblib.load("models/cat_imputer.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")

# Nuovo paziente
nuovo_paziente = pd.DataFrame([{
    "età del paziente dimesso": 87,
    "sesso": "donna",
    "età_clinica": "grande_anziano",
    "tipdim": 1,
    "barthel_totale_ingresso": 36,
    "totale_scimric": 49,
    **{f"intproc{i}": 9200 + i*10 for i in range(1, 11)}
}])

# Colonne
num_cols_valid = ['età del paziente dimesso', 'tipdim', 'barthel_totale_ingresso', 'totale_scimric'] + [f'intproc{i}' for i in range(1, 11)]
cat_cols = ['sesso', 'età_clinica']

# Imputazione
X_num = pd.DataFrame(num_imputer.transform(nuovo_paziente[num_cols_valid]), columns=num_cols_valid)
X_cat = pd.DataFrame(cat_imputer.transform(nuovo_paziente[cat_cols]), columns=cat_cols)

# Dummy encoding + allineamento
X_new = pd.get_dummies(pd.concat([X_num, X_cat], axis=1), drop_first=True)

for col in feature_columns:
    if col not in X_new.columns:
        X_new[col] = 0
X_new = X_new[feature_columns]

# Scaling + predizione
X_scaled = scaler.transform(X_new)
cluster = kmeans.predict(X_scaled)[0]

# Spiegazione
messaggio = {
    0: "🔹 Cluster 0 – Paziente fragile, età avanzata, bassa autonomia all’ingresso, probabile degenza più lunga.",
    1: "🔸 Cluster 1 – Paziente mediamente più autonomo, età leggermente inferiore, possibile degenza più breve."
}

print(f"\n📍 Cluster predetto: {cluster}")
print(messaggio[cluster])
