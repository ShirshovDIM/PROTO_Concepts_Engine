from parse_utils import get_prompts

if __name__ == "__main__":

    from driver_setup import * 

    print("running webdriver builder ...")

    driver.get(app_config.remote_executable)

    print("builder completed")