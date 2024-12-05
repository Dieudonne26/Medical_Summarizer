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
pdf.cell(200, 10, txt="Nom:  Jean", ln=True, align='L')
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



# Ajouter un saut de ligne
pdf.ln(10)



# Ajouter un saut de ligne
pdf.ln(10)

# Résultats de tests
pdf.cell(200, 10, txt="Résultats de Tests", ln=True, align='L')
pdf.multi_cell(0, 10, txt="- Test de spirométrie : Résultats normaux\n- Prise de sang :Negatif", align='L')

# Ajouter un saut de ligne
pdf.ln(10)



# Sauvegarder le fichier PDF
output_file = "test.pdf"
pdf.output(output_file)

output_file  # Renvoie le chemin du fichier PDF généré
