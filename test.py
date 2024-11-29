from fpdf import FPDF

# Créer un objet PDF
pdf = FPDF()

# Ajouter une page
pdf.add_page()

# Définir la police
pdf.set_font("Arial", size=12)

# Titre du document
pdf.cell(200, 10, txt="Dossier Médical - Exemple Fictif", ln=True, align='C')

# Ajouter un saut de ligne
pdf.ln(10)

# Informations personnelles
pdf.cell(200, 10, txt="Informations Personnelles", ln=True, align='L')
pdf.cell(200, 10, txt="Nom: Dupont Jean", ln=True, align='L')
pdf.cell(200, 10, txt="Date de naissance: 15/03/1985", ln=True, align='L')
pdf.cell(200, 10, txt="Adresse: 123 Rue Fictive, 75000 Paris, France", ln=True, align='L')
pdf.cell(200, 10, txt="Numéro de téléphone: +33 1 23 45 67 89", ln=True, align='L')
pdf.cell(200, 10, txt="Email: jean.dupont@example.com", ln=True, align='L')

# Ajouter un saut de ligne
pdf.ln(10)

# Antécédents médicaux
pdf.cell(200, 10, txt="Antécédents Médicaux", ln=True, align='L')
pdf.multi_cell(0, 10, txt="- Asthme depuis l'enfance\n- Allergie à la pénicilline\n- Opération de la vésicule biliaire en 2010", align='L')

# Ajouter un saut de ligne
pdf.ln(10)

# Médications actuelles
pdf.cell(200, 10, txt="Médications Actuelles", ln=True, align='L')
pdf.multi_cell(0, 10, txt="- Ventoline (inhalateur) 2 fois par jour pour l'asthme\n- Paracétamol 500mg en cas de douleurs", align='L')

# Ajouter un saut de ligne
pdf.ln(10)

# Consultations récentes
pdf.cell(200, 10, txt="Consultations Récentes", ln=True, align='L')
pdf.multi_cell(0, 10, txt="1. Consultation avec le Dr. Martin (médecin généraliste) - 20/11/2024 : Bilan de santé général.\n2. Consultation avec le Dr. Durand (spécialiste en allergie) - 05/11/2024 : Allergies et traitements.\n", align='L')

# Ajouter un saut de ligne
pdf.ln(10)

# Résultats de tests
pdf.cell(200, 10, txt="Résultats de Tests", ln=True, align='L')
pdf.multi_cell(0, 10, txt="- Test de spirométrie : Résultats normaux\n- Prise de sang : Tout est dans les normes", align='L')

# Ajouter un saut de ligne
pdf.ln(10)

# Remarques supplémentaires
pdf.cell(200, 10, txt="Remarques Supplémentaires", ln=True, align='L')
pdf.multi_cell(0, 10, txt="- Le patient suit un suivi médical régulier pour l'asthme.\n- Recommandation : éviter les irritants pulmonaires.", align='L')

# Sauvegarder le fichier PDF
output_file = "dossier_medical_fictif.pdf"
pdf.output(output_file)

output_file  # Renvoie le chemin du fichier PDF généré
