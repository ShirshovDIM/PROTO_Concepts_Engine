import pandas as pd 
from itertools import product
from config import * 
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


def get_prompts(prompt_config_path): 
    prompt_data = pd.read_excel(prompt_config_path)

    prompt_list = []

    for col in prompt_data.columns: 
        prompt_list.append(prompt_data[col][~prompt_data[col].isna()].to_list())

    return product(*prompt_list, repeat=1)


def gen_wait(driver, wait_limit):
        sleep(1)
        try: 
            (
                WebDriverWait(driver, wait_limit)
                .until(
                    expected_conditions
                    .text_to_be_present_in_element_attribute(
                        (By.XPATH, '//div[@class="loader-container"]/div[@class="progress-container"]/progress')
                        , 'value'
                        , '100')
                    )
            )
        except TimeoutException: 
            print("TimeoutException occured")