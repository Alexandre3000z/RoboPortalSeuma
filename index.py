from Config.browserConfig import Chorme

from Classes.listCompanys import company_list

from Scripts.startSeuma import startSeuma
from Scripts.putCNPJ import putCNPJ
from Scripts.downloadFiles import downloadFiles

from Utils.pdfReader import getExpiration
from Utils.excelReader.excelReader import extract_xlsxData, saveListToExcel
import time

def initSeuma():
    try:
        # Instância do navegador Chrome
        driver = Chorme()
    except:
        raise Exception('Erro ao inicializar o Google Chrome.')


    startSeuma(driver)
    return driver

def executeProcess(driver, cnpj, name):
   
    putCNPJ(driver,cnpj)
    print(f'{name} - {cnpj}')
    validateCompany = downloadFiles(driver)
    
    if validateCompany == True:
        expirationDate = getExpiration()
        
        companyObjct = {
            
            'Nome': name,
            'CNPJ': cnpj,
            'Data de Expiração': expirationDate,
            
            }
        print(companyObjct)
        company_list.add_data(companyObjct)
        

driver = initSeuma()

wish_columns = ['EMPRESA','CNPJ']
xlsx_path = r'C:\Users\ADM\Desktop\PROJETOS\RoboPortalSeuma\Utils\excelReader\PlanilhaEmpresas.xlsx'
listas = extract_xlsxData(xlsx_path, wish_columns)


for empresa, cnpj in zip(listas[0], listas[1]):
    
    executeProcess(driver, cnpj, empresa)
print(company_list.list)

caminho_excel = "dados.xlsx"  # Nome do arquivo de saída

saveListToExcel(company_list.list, caminho_excel)
   