#SCRIPT IN PYTHON BY DINO GREJO - DINOGREJO@GMAIL.COM GITHUB: DGREJ

import os
import xml.etree.ElementTree as ET
import pandas as pd

# Pasta contendo os arquivos XML
caminho_pasta = r'C:\Users\dino.grejo\OneDrive - VIVEO\Documentos\python\xml'

# Lista para armazenar os dados extraídos
dados = []

# Função para extrair as informações de cada XML
def extrair_dados_do_xml(caminho_xml):
    tree = ET.parse(caminho_xml)
    root = tree.getroot()
    
    # Definir o namespace
    ns = {'nfe': 'http://www.portalfiscal.inf.br/cte'}
    
    # Função auxiliar para extrair texto de elementos com verificação
    def get_element_text(path):
        element = root.find(path, ns)
        return element.text if element is not None else ''
    
    # Ajuste para remover os dois primeiros dígitos
    def ajustar_codigo_municipio(codigo):
        return codigo[2:] if len(codigo) > 2 else codigo

    # Extrair as informações desejadas
    cte_info = {
        'CNPJ FILIAL': get_element_text('.//nfe:dest/nfe:CNPJ'),
        'CNPJ TRANSP.':get_element_text('.//nfe:emit/nfe:CNPJ'),
        'TRANSPORTADOR':get_element_text('.//nfe:emit/nfe:xNome'),
        'REMETENTE': get_element_text('.//nfe:rem/nfe:xNome'),
        'CNPJ_REMETENTE': get_element_text('.//nfe:rem/nfe:CNPJ'),
        'CTE': get_element_text('.//nfe:ide/nfe:nCT'),
        'SERIE': get_element_text('.//nfe:ide/nfe:serie'),
        'VALOR': get_element_text('.//nfe:vPrest/nfe:vTPrest').replace('.', ','),
        'CHAVEnf': '\n'.join([chave.text for chave in root.findall('.//nfe:infDoc/nfe:infNFe/nfe:chave', ns)]),
        'EMISSAO': get_element_text('.//nfe:ide/nfe:dhEmi').split('T')[0] if get_element_text('.//nfe:ide/nfe:dhEmi') else '',  # Formato de data apenas
        'UFIni': get_element_text('.//nfe:ide/nfe:UFIni'),
        'cMunIni': ajustar_codigo_municipio(get_element_text('.//nfe:ide/nfe:cMunIni')),
        'xMunIni': get_element_text('.//nfe:ide/nfe:xMunIni'),
        'UFFim': get_element_text('.//nfe:ide/nfe:UFFim'),
        'cMunFim': ajustar_codigo_municipio(get_element_text('.//nfe:ide/nfe:cMunFim')),
        'xMunFim': get_element_text('.//nfe:ide/nfe:xMunFim'),
        'chCTe': get_element_text('.//nfe:infProt/nfe:chCTe'),
        'vTrib': get_element_text('.//nfe:vPrest/nfe:vTPrest').replace('.', ','),
        'icms%': get_element_text('.//nfe:ICMS/nfe:ICMS00/nfe:pICMS'),
        'vICMS': get_element_text('.//nfe:ICMS/nfe:ICMS00/nfe:vICMS').replace('.', ','),
        'ICMSOutUF%': get_element_text('.//nfe:ICMS/nfe:ICMSOutraUF/nfe:pICMSOutraUF'),
        'vICMSOutUF': get_element_text('.//nfe:ICMS/nfe:ICMSOutraUF/nfe:vICMSOutraUF').replace('.', ','),
        
    }

     # Ajuste para a data de emissão no formato desejado (dd/mm/aaaa)
    if cte_info['EMISSAO']:
        data_emissao = cte_info['EMISSAO'].split('-')
        cte_info['EMISSAO'] = f"{data_emissao[2]}/{data_emissao[1]}/{data_emissao[0]}"
    
    return cte_info

# Percorrer todos os arquivos XML na pasta
for arquivo in os.listdir(caminho_pasta):
    if arquivo.endswith('.xml'):
        caminho_xml = os.path.join(caminho_pasta, arquivo)
        dados.append(extrair_dados_do_xml(caminho_xml))

# Criar um DataFrame com os dados extraídos
df = pd.DataFrame(dados)

# Adicionar colunas vazias (em branco) ao DataFrame
colunas_extras = ['Venc.', 'Data lanç.', 'serviço', 'NOME FILIAL', 'COD']
for coluna in colunas_extras:
    df[coluna] = ''  # Preenche a coluna com valores vazios

# Ajustar a ordem das colunas de acordo com o modelo Excel
df = df[['Venc.', 'Data lanç.', 'serviço', 'CNPJ FILIAL', 'NOME FILIAL', 'CNPJ TRANSP.', 'COD', 'TRANSPORTADOR', 'REMETENTE', 'CNPJ_REMETENTE', 'CTE', 'SERIE', 'VALOR', 'CHAVEnf', 'EMISSAO', 'UFIni', 'cMunIni', 'xMunIni', 'UFFim', 
         'cMunFim', 'xMunFim', 'chCTe', 'vTrib', 'icms%', 'vICMS', 'ICMSOutUF%', 'vICMSOutUF']]

# Gerar a planilha Excel
caminho_excel = r'C:\Users\dino.grejo\OneDrive - VIVEO\Documentos\python\Fatura_CTes.xlsx'
df.to_excel(caminho_excel, index=False)

print(f'Planilha gerada em: {caminho_excel}')
