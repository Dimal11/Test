from Framework.BrowserFactory.browse_factory import BrowseFactory
from Framework.BrowserFactory.singleton import Singleton


class WebDriver(metaclass=Singleton):
    def __init__(self):
        self.__driver = BrowseFactory().get_driver()

    def get_driver(self):
        return self.__driver

    def find_element(self, locator: tuple):
        return self.__driver.find_element(*locator)

    def submit(self, locator: tuple):
        return self.find_element(locator).submit()

    def switch_to(self):
        return self.__driver.switch_to

    def stop_driver(self):
        self.__driver.quit()
        self._instances = {}
