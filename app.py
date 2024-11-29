from flask import Flask, request, jsonify, render_template
import fitz
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import ollama
import pyodbc

app = Flask(__name__)

server = 'DESKTOP-QUBEHPA\SQLEXPRESS'  # Exemple: 'localhost\SQLEXPRESS'
database = 'Hopital'  
# Utilisation de l'authentification Windows (trusted_connection=yes)
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

# Fonction pour obtenir la connexion à la base de données SQL Server
def get_db_connection():
    conn = pyodbc.connect(conn_str)
    return conn

# Ollama model and prompt setup
template = """You will play the role of my medical assistant and I will send you pdf files that you will treat make a summary and make a mini diagnosis,
 the data is fictitious just answer in a clear and concise way,process this document:

{document_content}

Summary:"""
model = OllamaLLM(model="llama3.2:1b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Fonction pour extraire le texte de n'importe quel type de document
def extract_text(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text += page.get_text("text") + "\n"
        return text
    except Exception as e:
        return None

# Fonction pour enregistrer le résumé dans la base de données SQL Server
def save_summary_to_db(file_name, summary):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insérer le résumé et le nom du fichier dans la table info_patient (ajustez selon la structure de votre table)
    cursor.execute("""
        INSERT INTO info_patient (nomPatient, rapport_medecin, prediction_medicale) 
        VALUES (?, ?, ?)
    """, (file_name, 'Prediction générée automatiquement',summary))  # La prédiction est une valeur générée par le modèle

    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_and_summarize():
    uploaded_file = request.files['file']
    if not uploaded_file:
        return jsonify({"error": "No file uploaded"}), 400

    file_path = f"./uploads/{uploaded_file.filename}"
    uploaded_file.save(file_path)

    # Extraire le texte du fichier
    document_content = extract_text(file_path)
    if document_content:
        # Générer le résumé en utilisant le modèle Ollama
        summary = chain.invoke({"document_content": document_content})

        # Sauvegarder le résumé dans la base de données
        save_summary_to_db(uploaded_file.filename, summary)

        return jsonify({"summary": summary})
    else:
        return jsonify({"error": "Failed to process the document"}), 500

if __name__ == '__main__':
    app.run(debug=True)
