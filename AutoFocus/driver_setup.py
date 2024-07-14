from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import Config
from parse_utils import sleep

if __name__ == "__main__": 
    print("running driver setup ...")

    sleep(2)

    try:
        app_config = Config()
        options = Options()
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")    
        service = webdriver.ChromeService(executable_path=app_config.binary_driver_path)
        driver = webdriver.Chrome(service=service, options=options)

            
        driver.get(app_config.remote_executable)
        # driver.close()

    except Exception as ex:
        print(ex)
        print("setup failed")

    else: 
        print("setup successfull")
