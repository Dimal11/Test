from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Framework.Utils.config_manager import ConfigManager


class BrowseFactory:

    @staticmethod
    def get_driver():
        driver_conf = ConfigManager.get_driver_conf()
        if driver_conf["browser"] == "chrome":
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
        elif driver_conf["browser"] == "firefox":
            service = Service(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
        if driver_conf["size"] == "maximize":
            driver.maximize_window()
        elif driver_conf["size"] == "minimize":
            driver.minimize_window()
        else:
            driver.fullscreen_window()

        return driver
