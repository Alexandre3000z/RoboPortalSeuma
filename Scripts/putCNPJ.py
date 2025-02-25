from Utils.driverFunctions import *
def putCNPJ(driver,cnpj):
    
    company = locateByXpath(driver, 30, '//*[@id="tvTransparencia"]/ul/li[2]/a')
    company.click()
    
    inputCNPJ = locateByXpath(driver, 30, '//*[@id="tvTransparencia:formPortalTransparenciaEmpresa:cnpjEstabelecimento"]')
    inputCNPJ.clear()
    inputCNPJ.send_keys(cnpj)
    
    time.sleep(1)
    
    searchCNPJ = locateByXpath(driver, 30, '//*[@id="tvTransparencia:formPortalTransparenciaEmpresa:btnLocalizarPesquisarEmpresas"]')
    searchCNPJ.click()
    
    time.sleep(3)
    