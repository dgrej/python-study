# SCRIPT IN PYTHON BY DINO GREJO - DINOGREJO@GMAIL.COM GITHUB: DGREJ

import os
import re

# Pasta contendo os arquivos XML
caminho_pasta = r'C:\Users\dino.grejo\OneDrive - VIVEO\Documentos\python\xml'

# Caminho para salvar o arquivo chave.txt
caminho_arquivo_chave = r'C:\Users\dino.grejo\OneDrive - VIVEO\Documentos\python\chave.txt'

# Regex para extrair os números da tag chave
regex = r'<chCTe>(\d+)</chCTe>'

# Abrindo o arquivo de texto para escrita
with open(caminho_arquivo_chave, 'w') as arquivo_chave:
    # Escrevendo "CHAVE" no cabeçalho do arquivo TXT
    arquivo_chave.write('CHAVE\n')
    
    # Iterando sobre cada arquivo na pasta
    for nome_arquivo in os.listdir(caminho_pasta):
        if nome_arquivo.endswith('.xml'):
            # Abrindo o arquivo XML e lendo o conteúdo
            with open(os.path.join(caminho_pasta, nome_arquivo), 'r') as arquivo_xml:
                conteudo = arquivo_xml.read()
                # Extraindo os números da tag chave usando regex
                match = re.search(regex, conteudo)
                if match:
                    numero_chave = match.group(1)
                    # Escrevendo o número da chave no arquivo de texto
                    arquivo_chave.write(numero_chave + ",1" + '\n')

print(f"Arquivo chave.txt gerado em: {caminho_arquivo_chave}")
