import pytest
from Framework.Utils.config_manager import ConfigManager
from Project.Utils.users import User
from Project.Utils.comparison_users import ComparisonUsers
from Project.PageObjects.Pages.home_page import HomePage
from Project.PageObjects.NavigationMenu.navigation_menu import NavMenu
from Project.PageObjects.Pages.web_tables_page import WebTablesPage
from Project.PageObjects.Pages.registration_form import RegistrationForm
from loguru import logger


class TestTables:
    users = ConfigManager().get_test_data()['users']

    @pytest.mark.parametrize('user_data', users)
    def test_tables(self, driver, user_data):
        logger.info('Test 3 is start')
        driver.get(ConfigManager().get_driver_conf()["url"])

        assert HomePage().is_page_open() is True, 'The page is not found'

        NavMenu().click_nav_button(button_name='Elements')
        NavMenu().click_nav_button(button_name='Web Tables')
        assert WebTablesPage().is_page_open() is True, 'The page is not found'

        WebTablesPage().click_add_button()
        assert RegistrationForm().is_page_open() is True, 'The page is not found'
        user = User(user_data)
        RegistrationForm().set_user_in_form(user)
        RegistrationForm().form_submit()
        assert ComparisonUsers.comparison_users(user) is True, 'The data on the site does not match the test'
        WebTablesPage().click_delete_user_button()
        assert ComparisonUsers.comparison_users(user) is False, 'User not deleted'
        logger.info('Test 3 is finish')

