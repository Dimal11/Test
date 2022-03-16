from Framework.Utils.config_manager import ConfigManager
from Project.PageObjects.Pages.home_page import HomePage
from Project.PageObjects.Pages.alerts_page import AlertsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Framework.Utils.alerts import Alert
from Project.PageObjects.NavigationMenu.navigation_menu import NavMenu
from Project.Utils.random_string import RandomString
from loguru import logger


class TestAlerts:

    def test_alerts(self, driver):
        logger.info('Test 1 is start')
        driver.get(ConfigManager().get_driver_conf()["url"])

        assert HomePage().is_page_open() is True, '"Home page" is not found'

        NavMenu().click_nav_button(button_name='Alerts, Frame & Windows')
        NavMenu().click_nav_button(button_name='Alerts')
        assert AlertsPage().is_page_open() is True, '"Alert page" is not found'

        AlertsPage().click_to_button_see_alert()
        WebDriverWait(driver, ConfigManager().get_driver_conf()["waiting_time"]) \
            .until(EC.alert_is_present())
        assert driver.switch_to.alert.text == 'You clicked a button', 'The text in Alert does not match the given'

        driver.switch_to.alert.accept()

        assert Alert().is_alert_invisible() is True, 'Alert is visible'

        AlertsPage().click_to_button_confirm_alert()

        WebDriverWait(driver, ConfigManager().get_driver_conf()["waiting_time"]) \
            .until(EC.alert_is_present())
        assert driver.switch_to.alert.text == 'Do you confirm action?', 'The text in Alert does not match the given'

        driver.switch_to.alert.accept()
        assert Alert().is_alert_invisible() is True, 'Alert is visible'

        assert AlertsPage().get_text_after_confirm_alert() == 'You selected Ok', \
            'The text does not match the given'

        AlertsPage().click_to_button_prompt_alert()
        WebDriverWait(driver, ConfigManager().get_driver_conf()["waiting_time"]) \
            .until(EC.alert_is_present())
        assert driver.switch_to.alert.text == 'Please enter your name', 'The text in Alert does not match the given'

        random_text = RandomString.generate_random_string()
        driver.switch_to.alert.send_keys(random_text)
        driver.switch_to.alert.accept()
        assert Alert().is_alert_invisible() is True, 'Alert is visible'

        assert AlertsPage().get_text_after_prompt_alert() == f'You entered {random_text}', \
            'The text does not match the given'
        logger.info('Test 1 is finish')
