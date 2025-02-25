from Config.browserConfig import Chorme

from Classes.listCompanys import company_list

from Scripts.startSeuma import startSeuma
from Scripts.putCNPJ import putCNPJ
from Scripts.downloadFiles import downloadFiles

from Utils.pdfReader import getExpiration
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
    
    validateCompany = downloadFiles(driver)
    
    if validateCompany == True:
        expirationDate = getExpiration()
        
        companyObjct = {
            
            'CNPJ': cnpj,
            'Nome': name,
            'Data de Expiração': expirationDate,
            
            }
        company_list.add_data(companyObjct)
        

cnpj = '29058360000126'
nome = 'OFICINA AUTO EXPRESS'

driver = initSeuma()

executeProcess(driver, cnpj, nome)
print(company_list.list)
time.sleep(1000)    