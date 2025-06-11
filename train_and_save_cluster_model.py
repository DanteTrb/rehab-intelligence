# train_and_save_cluster_model.py

import pandas as pd
import numpy as np
import joblib
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 🔧 Simula dataset realistico
num_cols_valid = ['età del paziente dimesso', 'tipdim', 'barthel_totale_ingresso', 'totale_scimric'] + [f'intproc{i}' for i in range(1, 11)]
cat_cols = ['sesso', 'età_clinica']

df = pd.DataFrame({
    "età del paziente dimesso": np.random.randint(60, 90, 1000),
    "sesso": np.random.choice(["uomo", "donna"], 1000),
    "età_clinica": np.random.choice(["adulto", "anziano", "grande_anziano"], 1000),
    "tipdim": np.random.randint(1, 5, 1000),
    "barthel_totale_ingresso": np.random.randint(20, 80, 1000),
    "totale_scimric": 49,
    **{f"intproc{i}": np.random.normal(9200 + i*10, 50, 1000) for i in range(1, 11)}
})

# Imputazione
num_imputer = SimpleImputer(strategy="median")
X_num = pd.DataFrame(num_imputer.fit_transform(df[num_cols_valid]), columns=num_cols_valid)

cat_imputer = SimpleImputer(strategy="constant", fill_value="missing")
X_cat = pd.DataFrame(cat_imputer.fit_transform(df[cat_cols]), columns=cat_cols)

# Dummy encoding
X_full = pd.concat([X_num, X_cat], axis=1)
X_encoded = pd.get_dummies(X_full, drop_first=True)

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Clustering
kmeans = KMeans(n_clusters=2, random_state=42, n_init='auto')
kmeans.fit(X_scaled)

# Salvataggio
joblib.dump(kmeans, "models/kmeans_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(num_imputer, "models/num_imputer.pkl")
joblib.dump(cat_imputer, "models/cat_imputer.pkl")
joblib.dump(X_encoded.columns.tolist(), "models/feature_columns.pkl")

print("✅ Modelli e preprocessing salvati con successo.")