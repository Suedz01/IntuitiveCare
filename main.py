import zipfile
import pdfplumber
from pathlib import Path
import pandas as pd

# 1.2. Acesso aos PDFs (Anexo I e II) manualmente
# Supondo que você já tenha os arquivos PDF locais
pdf_paths = ["Anexo_I.pdf", "Anexo_II.pdf"]  # Substitua pelos caminhos corretos dos seus PDFs

# 1.3. Compactação dos arquivos PDF em um único ZIP
with zipfile.ZipFile("Anexos.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
    for pdf_path in pdf_paths:
        zipf.write(pdf_path, arcname=Path(pdf_path).name)

# 2.1. Extração dos dados da tabela do PDF Anexo I
pdf_path_anexo_i = pdf_paths[0]  # O primeiro PDF é o Anexo I
dados = []

with pdfplumber.open(pdf_path_anexo_i) as pdf:
    for pagina in pdf.pages:
        tabelas = pagina.extract_tables()
        for tabela in tabelas:
            for linha in tabela:
                if any(linha):
                    dados.append(linha)

df = pd.DataFrame(dados)

# 2.2. Definir os nomes das colunas
if df.shape[0] > 1:
    df.columns = df.iloc[0]
    df = df[1:]

# 2.4. Substituindo os nomes das colunas
colunas_substituicoes = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial",
}

df.rename(columns=colunas_substituicoes, inplace=True)

# 2.5. Substituindo os valores dentro das colunas (caso existam)
for coluna in df.columns:
    if coluna in colunas_substituicoes.values():  # Garante que só altera as colunas modificadas
        df[coluna] = df[coluna].replace({"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"})

# 2.3. Salvando os dados extraídos em CSV
csv_path = "dados_extraidos.csv"
df.to_csv(csv_path, index=False)

# Compactação do CSV em um arquivo ZIP
with zipfile.ZipFile(f"Teste_{'seu_nome'}.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_path, arcname="dados_extraidos.csv")

print("Processo completo!")