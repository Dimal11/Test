from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Framework.BrowserFactory.browser import WebDriver
from Framework.Utils.config_manager import ConfigManager
from abc import ABC
from loguru import logger


class BaseForm(ABC):

    def __init__(self, uniq_element=None, form_name=None):
        self.uniq_element = uniq_element
        self.form_name = form_name
        logger.debug(f'Page {self.form_name} is created')

    @logger.catch
    def is_page_open(self):
        WebDriverWait(WebDriver().get_driver(), ConfigManager().get_driver_conf()["waiting_time"]) \
            .until(EC.visibility_of(self.uniq_element._find_element()))

        return True

