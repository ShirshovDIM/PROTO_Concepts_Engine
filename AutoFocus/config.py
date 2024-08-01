import pathlib


class Config(object): 
    def __init__(self
                 , exec_protocol = "http"
                 , exec_host = "127.0.0.1"
                 , exec_port = "7865"
                 , prompt_config_path = f"{pathlib.Path().resolve()}\\AutoFocus\\prompts\\prompt_config.xlsx"
                 , binary_driver_path = f"{pathlib.Path().resolve()}\\AutoFocus\\ext\\webdriver\\chromedriver.exe"
                 , gen_wait_limit = 3600): 

        self.remote_executable = f"{exec_protocol}://{exec_host}:{exec_port}" 
        self.prompt_config_path = prompt_config_path
        self.binary_driver_path = binary_driver_path
        self.gen_wait_limit = gen_wait_limit