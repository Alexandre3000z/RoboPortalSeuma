from Utils.driverFunctions import *

def downloadFiles(driver):
    time.sleep(2)
    try:
        visualiseFile =findElementByXpath(driver, '//*[@id="tvTransparencia:formPortalTransparenciaEmpresa:dtListaEmpresas:0:row2"]')
        visualiseFile.click()
        
        alvara = locateByXpath(driver, 1000, '//*[@id="formDetalhePortalTransparencia:codigoTipoServicoPortalEmpresaLocalizar"]/div[2]/ul/li[3]')
        alvara.click()
        
        downloadButton = locateByXpath(driver, 30, '//*[@id="formDetalhePortalTransparencia:dtAlvarasFuncionamento:0:j_idt171"]')
        downloadButton.click()
        
    except:
        print('Empresa não é de fortaleza')    
    
    
    
    