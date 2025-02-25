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


