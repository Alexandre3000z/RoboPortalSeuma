from Utils.driverFunctions import *

def downloadFiles(driver):
    time.sleep(2)
    try:
        visualiseFile =findElementByXpath(driver, '//*[@id="tvTransparencia:formPortalTransparenciaEmpresa:dtListaEmpresas:0:row2"]')
        visualiseFile.click()
        
        x = locateByXpath(driver, 150, '//*[@id="formDetalhePortalTransparencia:dlgDetalhesPortalTransparencia"]/div[1]/a')
        
        time.sleep(3)
         
        licenseList = findElementsByXpath(driver, '//*[@id="formDetalhePortalTransparencia:codigoTipoServicoPortalEmpresaLocalizar"]/div[2]/ul/li')
        
        for i in licenseList:
        
            text = i.text.strip()
            if 'Alvará de Funcionamento' in text:
                print('Clickou')
                i.click()
        
        downloadButton = locateByXpath(driver, 10, '//*[@id="formDetalhePortalTransparencia:dtAlvarasFuncionamento:0:j_idt171"]')
        downloadButton.click()
        
        time.sleep(3)
        
        closeButton = locateByXpath(driver, 30, '//*[@id="formDetalhePortalTransparencia:dlgDetalhesPortalTransparencia"]/div[1]/a')
        closeButton.click()
        
        return True
    except:
        try:
            x = locateByXpath(driver, 5, '//*[@id="formDetalhePortalTransparencia:dlgDetalhesPortalTransparencia"]/div[1]/a')
            x.click()
        except:
            print('nada')
                
        print('Empresa não é de fortaleza')
        time.sleep(1.5)
        return False   
    
    
    