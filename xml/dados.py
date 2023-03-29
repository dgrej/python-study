import os
import csv
import xml.etree.ElementTree as ET

# Define o diretório onde estão os arquivos XML
diretorio = r'C:\Users\dinog\Downloads\Fatura número 1704 - TORNADO LOG'

# Define o nome do arquivo CSV onde serão salvos os resultados
arquivo_csv = 'resultados.csv'

# Define as colunas do arquivo CSV
cabecalho = ['CT-e', 'Chave']

# Inicializa uma lista vazia para armazenar os resultados
resultados = []

# Percorre todos os arquivos na pasta especificada
for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.xml'):  # Verifica se o arquivo é XML
        caminho_arquivo = os.path.join(diretorio, arquivo)
        
        # Faz o parsing do arquivo XML e extrai os valores das tags
        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()
        cte = root.find('.//{http://www.portalfiscal.inf.br/cte}nCT').text
        chave = root.find('.//{http://www.portalfiscal.inf.br/cte}chCTe').text
        
        # Adiciona os resultados à lista
        resultados.append([cte, chave])

# Salva os resultados em um arquivo CSV
with open(arquivo_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(cabecalho)
    writer.writerows(resultados)
