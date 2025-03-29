from flask import Flask, request, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas as origens

CSV_FILE = 'Relatorio_cadop.csv'

# Carregar dados do arquivo CSV
def load_data():
    data = []
    with open(CSV_FILE, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')  # Usando ';' como delimitador
        for row in reader:
            data.append(row)
    return data

# Rota de busca textual
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    data = load_data()

    # Filtra os dados que contêm o texto da consulta nos campos de interesse
    results = [
        row for row in data if any(
            query in str(value).lower() for value in row.values()
        )
    ]
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
