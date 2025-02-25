from Config.browserConfig import Chorme


from Scripts.startSeuma import startSeuma
from Scripts.putCNPJ import putCNPJ
from Scripts.downloadFiles import downloadFiles

from Utils.pdfReader import getExpiration
import time

cnpj = '29058360000126'
def executeProcess():
    try:
        # Instância do navegador Chrome
        driver = Chorme()
    except:
        raise Exception('Erro ao inicializar o Google Chrome.')
    
    startSeuma(driver)
    putCNPJ(driver,cnpj)
    downloadFiles(driver)
    
    expirationDate = getExpiration()
    
    
    time.sleep(1000)

executeProcess()    