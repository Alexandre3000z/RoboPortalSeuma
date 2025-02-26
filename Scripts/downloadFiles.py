from Utils.driverFunctions import *

import autoit
def downloadFiles(driver):
    time.sleep(2)
    try:
        visualiseFile =locateByXpath(driver,10, '//*[@id="tvTransparencia:formPortalTransparenciaEmpresa:dtListaEmpresas:0:row2"]')
        visualiseFile.click()
        
        x = locateByXpath(driver, 150, '//*[@id="formDetalhePortalTransparencia:dlgDetalhesPortalTransparencia"]/div[1]/a')
        
        time.sleep(3)
         
        licenseList = locateElementsByXpath(driver, 30, '//*[@id="formDetalhePortalTransparencia:codigoTipoServicoPortalEmpresaLocalizar"]/div[2]/ul/li')
        
        for i in licenseList:
        
            text = i.text.strip()
            if 'Alvará de Funcionamento' in text:
                print('Clickou')
                i.click()
        
        downloadButton = locateByXpath(driver, 10, '//*[@id="formDetalhePortalTransparencia:dtAlvarasFuncionamento:0:j_idt171"]')
        downloadButton.click()
        
        time.sleep(15)
        
        closeButton = locateByXpath(driver, 30, '//*[@id="formDetalhePortalTransparencia:dlgDetalhesPortalTransparencia"]/div[1]/a')
        time.sleep(2)
        closeButton.click()
        
        time.sleep(10)
        return True
    except:
        try:
            time.sleep(2)
            x = locateByXpath(driver, 15, '//*[@id="formDetalhePortalTransparencia:dlgDetalhesPortalTransparencia"]/div[1]/a')
            x.click()
            time.sleep(3)
            
            return 'empresa'
        except:
            print('nada')
                
        print('Empresa não é de fortaleza')
        time.sleep(1.5)
        return False   
    