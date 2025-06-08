from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import Config
from parse_utils import * 


if __name__ == "__main__":

        app_config = Config()
        options = Options()
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")    
        service = webdriver.ChromeService(executable_path=app_config.binary_driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        
        sleep(2)
        print("passing ...")

        for prmpt_features in get_prompts(app_config.prompt_config_path):
                
                prompt = ", ".join(prmpt_features)

                driver.find_element(By.CSS_SELECTOR, 'textarea.scroll-hide.svelte-1f354aw').clear()

                driver.find_element(By.CSS_SELECTOR, 'textarea.scroll-hide.svelte-1f354aw').send_keys(prompt)

                driver.find_element(By.ID, 'component-13').click()

                gen_wait(driver, app_config.gen_wait_limit)