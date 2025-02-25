from Config.browserConfig import Chorme

from Classes.listCompanys import company_list

from Scripts.startSeuma import startSeuma
from Scripts.putCNPJ import putCNPJ
from Scripts.downloadFiles import downloadFiles

from Utils.pdfReader import getExpiration
import time

def executeProcess(cnpj, name):
    try:
        # Instância do navegador Chrome
        driver = Chorme()
    except:
        raise Exception('Erro ao inicializar o Google Chrome.')
    
    startSeuma(driver)
    putCNPJ(driver,cnpj)
    downloadFiles(driver)
    
    expirationDate = getExpiration()
    
    companyObjct = {
        
        'CNPJ': cnpj,
        'Nome': name,
        'Data de Expiração': expirationDate,
        
        }
    company_list.add_data(companyObjct)
    print(company_list.list)
    
    time.sleep(1000)

cnpj = '29058360000126'
nome = 'OFICINA AUTO EXPRESS'

executeProcess(cnpj, nome)    