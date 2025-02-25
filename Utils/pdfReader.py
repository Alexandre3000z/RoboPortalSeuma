import os
import glob
import PyPDF2
import re

def encontrar_ultimo_pdf():
    # Obtém o diretório de downloads do usuário
    pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")

    # Busca todos os arquivos PDF na pasta de Downloads
    lista_pdfs = glob.glob(os.path.join(pasta_downloads, "*.pdf"))

    if not lista_pdfs:
        print("Nenhum arquivo PDF encontrado na pasta de Downloads.")
        return None

    # Encontra o arquivo PDF mais recente
    ultimo_pdf = max(lista_pdfs, key=os.path.getctime)
    return ultimo_pdf

def ler_pdf(caminho_pdf):
    try:
        with open(caminho_pdf, "rb") as arquivo:
            leitor = PyPDF2.PdfReader(arquivo)
            texto = ""

            # Itera sobre todas as páginas do PDF e extrai o texto
            for pagina in leitor.pages:
                texto += pagina.extract_text() + "\n"

            return texto.strip()  # Remove espaços extras
    except Exception as e:
        print(f"Erro ao ler o PDF: {e}")
        return None

def extrair_depois_de_observacoes(texto):
    # Expressão regular para encontrar "Observações" seguido de 10 caracteres
    padrao = re.search(r"Observações\s{0,5}(.{10})", texto, re.IGNORECASE)
    
    if padrao:
        return padrao.group(1)  # Retorna os 10 caracteres após "Observações"
    else:
        return "Texto não encontrado."

def getExpiration():
    # Encontra o último PDF baixado
    pdf_recente = encontrar_ultimo_pdf()

    if pdf_recente:
        # print(f"Lendo o arquivo: {pdf_recente}\n")
        texto_pdf = ler_pdf(pdf_recente)

        if texto_pdf:
            # print("Conteúdo extraído do PDF:\n")
            resultado = extrair_depois_de_observacoes(texto_pdf)
            # print(f"🔍 10 letras após 'Observações': {resultado}")
            return resultado
        else:
            print("Não foi possível extrair o texto do PDF.")
