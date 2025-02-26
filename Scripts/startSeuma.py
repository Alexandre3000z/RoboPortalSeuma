from Utils.driverFunctions import *

def startSeuma(driver):
    driver.get('https://portal.seuma.fortaleza.ce.gov.br/fortalezaonline/portal/homelogado')
    
    transparency = locateByXpath(driver, 30, '//*[@id="menuform:j_idt70"]/a')
    transparency.click()
    
    time.sleep(2)
    
    company = locateByXpath(driver, 30, '//*[@id="tvTransparencia"]/ul/li[2]/a')
    company.click()
    
    
