from Framework.Utils.config_manager import ConfigManager
from Project.PageObjects.Pages.home_page import HomePage
from Project.PageObjects.Pages.nested_frames_page import NestedFramesPage
from Project.PageObjects.Pages.frames_page import FramesPage
from Project.PageObjects.NavigationMenu.navigation_menu import NavMenu
from loguru import logger


class TestIframe:
    def test_iframe(self, driver):
        logger.info('Test 2 is start')
        driver.get(ConfigManager().get_driver_conf()["url"])

        assert HomePage().is_page_open() is True, 'The page is not found'

        NavMenu().click_nav_button(button_name='Alerts, Frame & Windows')
        NavMenu().click_nav_button(button_name='Nested Frames')
        assert NestedFramesPage().is_page_open() is True, 'The page is not found'

        frames_text = NestedFramesPage().get_iframe_text()
        assert frames_text['parent_frame_text'] == 'Parent frame', 'The text does not match the given'
        assert frames_text['child_frame_text'] == 'Child Iframe', 'The text does not match the given'

        driver.switch_to.default_content()

        NavMenu().click_nav_button(button_name='Frames')
        assert FramesPage().is_page_open() is True, 'The page is not found'

        iframes_text = FramesPage().get_text_from_iframes()
        assert iframes_text['iframe_1_text'] == iframes_text['iframe_2_text'], 'The text does not match the given'
        logger.info('Test 2 is finish')






