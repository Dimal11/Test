from loguru import logger
from dateutil import parser

from Framework.Utils.config_manager import ConfigManager
from Project.PageObjects.NavigationMenu.navigation_menu import NavMenu
from Project.PageObjects.Pages.date_picker_page import DatePickerPage
from Project.PageObjects.Pages.home_page import HomePage
from Project.Utils.local_time import LocalTime


class TestDatePicker:
    def test_date_picker(self, driver):
        logger.info('Test 6 is start')
        driver.get(ConfigManager().get_driver_conf()["url"])

        assert HomePage().is_page_open() is True, '"Home page" is not found'

        NavMenu().click_nav_button(button_name='Widgets')
        NavMenu().click_nav_button(button_name='Date Picker')
        assert DatePickerPage().is_page_open() is True, '"Date Picker page" is not found'

        assert LocalTime().get_date() == DatePickerPage().get_date(), \
            'Date in date_field is not real date'

        assert parser.parse(LocalTime().get_date_time()).__str__() == \
               parser.parse(DatePickerPage().get_date_time()).__str__(), \
            'Date in date_time_field is not real date'

        input_date = DatePickerPage().date_construct()
        DatePickerPage().set_date(input_date)
        assert DatePickerPage().get_date() == input_date, \
            'The date in the date_field is not equal to the entered date'
