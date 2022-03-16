from Framework.PageObjects.BaseObjects.base_element import BaseElement
from loguru import logger


class Input(BaseElement):
    def __init__(self, locator_type, locator, input_name):
        super().__init__(locator_type=locator_type, locator=locator, element_name=input_name)

    def send_keys(self, text):
        self._find_element().clear()
        self._find_element().send_keys(text)
        logger.info(f'In {self.element_name} send "{text}"')

