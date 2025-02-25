from Utils.driverFunctions import *

def startSeuma(driver):
    driver.get('https://portal.seuma.fortaleza.ce.gov.br/fortalezaonline/portal/homelogado')
    
    transparency = locateByXpath(driver, 30, '//*[@id="menuform:j_idt70"]/a')
    transparency.click()
    