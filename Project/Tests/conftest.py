import pytest

from Framework.BrowserFactory.browser import WebDriver
from Framework.Utils.logger import Logger


@pytest.fixture(scope='session')
def driver():
    Logger().get_logger()
    yield WebDriver().get_driver()
    WebDriver().stop_driver()
