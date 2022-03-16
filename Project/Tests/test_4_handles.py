from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Framework.Utils.config_manager import ConfigManager
from Project.PageObjects.Pages.home_page import HomePage
from Project.PageObjects.Pages.browser_windows_page import BrowserWindowsPage
from Project.PageObjects.Pages.simple_page import SimplePage
from Project.PageObjects.Pages.links_page import LinksPage
from Project.PageObjects.NavigationMenu.navigation_menu import NavMenu
from loguru import logger


class TestHandles:
    def test_handles(self, driver):
        logger.info('Test 4 is start')
        driver.get(ConfigManager().get_driver_conf()["url"])

        assert HomePage().is_page_open() is True, 'The page is not found'

        NavMenu().click_nav_button(button_name='Alerts, Frame & Windows')
        NavMenu().click_nav_button(button_name='Browser Windows')
        assert BrowserWindowsPage().is_page_open() is True, 'The page is not found'

        BrowserWindowsPage().click_new_tab_button()
        WebDriverWait(driver, ConfigManager().get_driver_conf()["waiting_time"]) \
            .until(EC.number_of_windows_to_be(2))
        main_window = driver.current_window_handle
        for window_handle in driver.window_handles:
            if window_handle != main_window:
                driver.switch_to.window(window_handle)
                break
        assert SimplePage().is_page_open() is True, 'The page is not found'
        driver.close()
        driver.switch_to.window(main_window)
        assert BrowserWindowsPage().is_page_open() is True, 'The page is not found'
        NavMenu().click_nav_button(button_name='Elements')
        WebDriverWait(driver, ConfigManager().get_driver_conf()["waiting_time"]) \
            .until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Links"]')))
        NavMenu().click_nav_button(button_name='Links')
        assert LinksPage().is_page_open() is True, 'The page is not found'
        LinksPage().click_home_link()
        WebDriverWait(driver, ConfigManager().get_driver_conf()["waiting_time"]) \
            .until(EC.number_of_windows_to_be(2))
        main_window = driver.current_window_handle
        for window_handle in driver.window_handles:
            if window_handle != main_window:
                driver.switch_to.window(window_handle)
                break
        assert HomePage().is_page_open() is True, 'The page is not found'
        driver.switch_to.window(main_window)
        assert LinksPage().is_page_open() is True
        logger.info('Test 4 is finish')
