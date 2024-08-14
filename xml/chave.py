#SCRIPT IN PYTHON BY DINO GREJO - DINOGREJO@GMAIL.COM GITHUB: DGREJ

import os
import re

# pasta contendo os arquivos XML
caminho_pasta = r'C:\Users\dino.grejo\OneDrive - VIVEO\Documentos\python\xml'

# regex para extrair os números da tag chave
regex = r'<chCTe>(\d+)</chCTe>'

# abrindo o arquivo de texto para escrita
with open('chave.txt', 'w') as arquivo_chave:
    # ESCREVENDO CHAVE NO CABEÇALHO DO TXT
    arquivo_chave.write('CHAVE\n')
    # iterando sobre cada arquivo na pasta
    for nome_arquivo in os.listdir(caminho_pasta):
        if nome_arquivo.endswith('.xml'):
            # abrindo o arquivo XML e lendo o conteúdo
            with open(os.path.join(caminho_pasta, nome_arquivo), 'r') as arquivo_xml:
                conteudo = arquivo_xml.read()
                # extraindo os números da tag chave usando regex
                match = re.search(regex, conteudo)
                if match:
                    numero_chave = match.group(1)
                    # escrevendo o número da chave no arquivo de texto
                    arquivo_chave.write(numero_chave + ",1" '\n')
