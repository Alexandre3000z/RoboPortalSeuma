import pandas as pd

def extract_xlsxData(caminho_arquivo, colunas):
    """
    Lê um arquivo XLSX e extrai três colunas específicas para listas separadas.
    
    :param caminho_arquivo: Caminho do arquivo Excel (.xlsx)
    :param colunas: Lista com os nomes ou índices das 3 colunas a serem extraídas
    :return: Três listas contendo os dados das colunas especificadas
    """
    try:
        # Lê a planilha do arquivo
        df = pd.read_excel(caminho_arquivo)

        # Verifica se as colunas existem no DataFrame
        for coluna in colunas:
            if coluna not in df.columns:
                raise ValueError(f"A coluna '{coluna}' não foi encontrada na planilha.")

        # Extrai as colunas em listas separadas
        lista1 = df[colunas[0]].tolist()  # Remove valores NaN
        lista2 = df[colunas[1]].tolist()

        return lista1, lista2

    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        return None, None, None


def saveListToExcel(lista_de_objetos, caminho_arquivo):
    """
    Converte uma lista de dicionários em um arquivo Excel (.xlsx).
    
    :param lista_de_objetos: Lista de dicionários [{}] representando os dados.
    :param caminho_arquivo: Caminho onde o arquivo Excel será salvo.
    """
    if not lista_de_objetos:
        print("A lista está vazia. Nenhum dado para salvar.")
        return
    
    try:
        # Converte a lista de dicionários em um DataFrame
        df = pd.DataFrame(lista_de_objetos)

        # Salva o DataFrame em um arquivo Excel
        df.to_excel(caminho_arquivo, index=False, engine="openpyxl")
        
        print(f"Arquivo Excel salvo com sucesso em: {caminho_arquivo}")
    
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")



