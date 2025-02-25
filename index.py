from Config.browserConfig import Chorme


from Scripts.startSeuma import startSeuma

def executeProcess():
    try:
        # Instância do navegador Chrome
        driver = Chorme()
    except:
        raise Exception('Erro ao inicializar o Google Chrome.')
    
    startSeuma(driver)
    

executeProcess()    