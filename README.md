## 🏥 Rehab-Intelligence: Data-Driven Insights for Policlinico Italia
Questo repository raccoglie cinque progetti di analisi avanzata su dati clinico-riabilitativi reali, con l’obiettivo di estrarre insight utili alla pianificazione sanitaria, ottimizzazione delle risorse e personalizzazione delle cure presso il Policlinico Italia.

# 📁 Struttura del repository
.
├── 01_outcome_model/           # Predizione outcome riabilitativi (Barthel, FIM)
├── 02_degenza_analysis/        # Analisi predittiva della degenza prolungata
├── 03_patient_clustering/      # Clustering per pattern clinici
├── 04_riammissioni/            # Modello predittivo di riammissioni a 30/90 giorni
├── 05_trend_longitudinali/     # Analisi epidemiologica e trend pluriennali
├── results/                    # Report e grafici generati
└── README.md                   # Questo file

# Progetti inclusi

1. *Predizione di outcome riabilitativi*
Obiettivo: Predire punteggio Barthel, delta Barthel.
Tecniche: Regressione XGBoost, SHAP per interpretabilità.
Impatto: Supporto alla pianificazione dei percorsi e confronti tra centri o team clinici.

2. *Analisi dei tempi di degenza*
Obiettivo: Identificare fattori clinici e sociodemografici associati a ricoveri lunghi.
Tecniche: Classificazione binaria (degenza ≥ 30gg), SHAP.
Impatto: Ottimizzazione delle risorse, riduzione costi e miglioramento dell'efficienza.

3. *Clustering per pattern clinici nascosti*
Obiettivo: Segmentare i pazienti in gruppi omogenei per stato clinico e traiettoria di cura.
Tecniche: KMeans, PCA, silhouette analysis, profiling con grafici radar.
Impatto: Personalizzazione della riabilitazione, miglioramento comunicazione medico-paziente.
👉 Estensione: Abbiamo incluso un modulo di Cluster Profiling che consente di:
-Identificare i profili clinici prevalenti in ciascun cluster.
-Visualizzare le variabili discriminanti per ogni gruppo.
-Integrare le informazioni in modelli predittivi o dashboard interattiv

4. *Modello predittivo di riammissioni ospedaliere*
Obiettivo: Prevedere il rischio di riammissione a 30/90 giorni.
Tecniche: Classificatori supervisati, analisi SHAP, bilanciamento classi.
Impatto: Prevenzione secondaria, follow-up mirati, riduzione dei rientri in reparto. (Dato non sufficiente)

5. *Trend longitudinali e analisi epidemiologiche*
Obiettivo: Monitorare l’evoluzione nel tempo di indicatori clinici e demografici.
Tecniche: Analisi descrittiva + report automatico in PDF (generate_trend_report.py)
Grafici inclusi: Pazienti unici per anno, Età media e percentuale grandi anziani, Barthel medio all’ingresso, Diagnosi prevalenti nel tempo
Impatto: Supporto a decisioni strategiche e politiche sanitarie.

# 🚀 Come iniziare
1. Clona il repository
git clone https://github.com/DanteTrb/rehab-intelligence.git
cd rehab-intelligence

2. Crea ambiente virtuale
python -m venv .venv
source .venv/bin/activate  # su Mac/Linux
oppure
.venv\Scripts\activate.bat  # su Windows

3. Installa i requisiti
pip install -r requirements.txt

4. Esegui uno dei notebook
Apri il file Jupyter corrispondente al progetto che ti interessa (01_outcome_model/..., ecc.)

5. Genera PDF finale dei trend epidemiologici (opzionale)
python generate_trend_report.py

# 🛠️ Tecnologie usate
Python (pandas, scikit-learn, matplotlib, seaborn, fpdf)
SHAP, clustering unsupervised
Export in PDF per report automatizzati
Dataset originale in formato .parquet

# 📈 Risultati principali
Accuratezza modelli > 80% nei task predittivi
Insight clinicamente interpretabili via SHAP
Riduzione significativa delle feature inutili grazie a filter/wrapper selection
Cluster clinici coerenti con tipologie reali di pazienti

## 🧠 Autore
Progetto sviluppato da Dante Trabassi, PhD Neuroscience, esperto in AI applicata alla riabilitazione e all’analisi del movimento.