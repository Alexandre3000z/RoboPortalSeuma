from Utils.driverFunctions import *
def putCNPJ(driver,cnpj):
    
    inputCNPJ = locateByXpath(driver, 30, '//*[@id="tvTransparencia:formPortalTransparenciaEmpresa:cnpjEstabelecimento"]')
    inputCNPJ.clear()
    time.sleep(2)
    inputCNPJ.send_keys(cnpj)
    
    time.sleep(2)
    
    searchCNPJ = locateByXpath(driver, 30, '//*[@id="tvTransparencia:formPortalTransparenciaEmpresa:btnLocalizarPesquisarEmpresas"]')
    searchCNPJ.click()
    
    time.sleep(30)