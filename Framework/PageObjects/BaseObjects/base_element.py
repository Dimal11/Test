from Framework.BrowserFactory.browser import WebDriver
from abc import ABC
from loguru import logger


class BaseElement(ABC):

    @logger.catch
    def __init__(self, locator_type, locator, element_name):
        self.locator = (locator_type, locator)
        self.element_name = element_name
        logger.debug(f'Element "{self.element_name}" is created')

    def _find_element(self):
        element = WebDriver().find_element(self.locator)
        logger.info(f'Element "{self.element_name}" find')
        return element

    def _find_elements(self):
        elements = WebDriver().get_driver().find_elements(self.locator)
        logger.info(f'List of {len(elements)} "{self.element_name}" elements find')
        return elements

    def click(self):
        WebDriver().find_element(self.locator).click()
        logger.info(f'Click "{self.element_name}"')

    def is_displayed(self):
        WebDriver().find_element(self.locator).is_displayed()
