from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", 'B', 16)
        self.cell(0, 10, "Trend Longitudinali Policlinico Italia", ln=True, align="C")
        self.set_font("Helvetica", '', 10)
        self.cell(0, 10, f"Generato il {datetime.today().strftime('%d/%m/%Y')}", ln=True, align="C")
        self.ln(5)

    def add_section(self, title, image_path, caption):
        self.add_page()
        self.set_font("Helvetica", 'B', 14)
        self.cell(0, 10, title, ln=True)
        self.image(image_path, w=170)
        self.set_font("Helvetica", '', 11)
        self.multi_cell(0, 10, caption)

# Crea il PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Sezioni
pdf.add_section(
    "Pazienti unici per anno",
    "results/figures/trend_pazienti_unici.png",
    "Il numero di pazienti unici mostra una riduzione progressiva dal 2006 al 2021, con leggera ripresa nel 2022."
)

pdf.add_section(
    "Età media e Grandi anziani",
    "results/figures/trend_eta_grandianziani.png",
    "L'età media è aumentata costantemente, con una prevalenza significativa di grandi anziani (età >= 80 anni)."
)

pdf.add_section(
    "Barthel medio all'ingresso",
    "results/figures/trend_barthel_ingresso.png",
    "Il livello funzionale all'ingresso (Barthel) è diminuito fino al 2012, stabilizzandosi successivamente tra 40 e 45 punti."
)

pdf.add_section(
    "Diagnosi prevalenti",
    "results/figures/trend_diagnosi.png",
    "Nel tempo si osserva una riduzione delle fratture e un aumento delle riabilitazioni specifiche per patologie neurologiche."
)

# Salva
pdf.output("results/trend_longitudinali_report.pdf")
print("PDF creato: results/trend_longitudinali_report.pdf")