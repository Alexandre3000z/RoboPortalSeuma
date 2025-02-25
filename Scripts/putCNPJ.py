from Utils.driverFunctions import *
def putCNPJ(driver,cnpj):
    
    company = locateByXpath(driver, 30, '//*[@id="tvTransparencia"]/ul/li[2]/a')
    company.click()
    
    inputCNPJ = locateByXpath(driver, 30, '//*[@id="tvTransparencia:formPortalTransparenciaEmpresa:cnpjEstabelecimento"]')
    