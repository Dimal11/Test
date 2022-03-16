from Framework.PageObjects.BaseObjects.base_form import BaseForm
from Framework.PageObjects.Elements.label import Label
from Framework.BrowserFactory.browser import WebDriver
from selenium.webdriver.common.by import By


class FramesPage(BaseForm):
    def __init__(self):
        super().__init__(
            form_name='frame_page',
            uniq_element=Label(
                label_name='frames',
                locator_type='xpath',
                locator='//div[@class="main-header" and contains(text(),"Frames")]'
            )
        )

    @staticmethod
    def get_text_from_iframes():
        iframes_dict = {}
        iframe_1 = WebDriver().find_element(('id', 'frame1'))
        WebDriver().switch_to().frame(iframe_1)
        iframes_dict['iframe_1_text'] = WebDriver().find_element(('id', 'sampleHeading')).text
        WebDriver().switch_to().default_content()
        iframe_2 = WebDriver().get_driver().find_element(By.ID, 'frame2')
        WebDriver().switch_to().frame(iframe_2)
        iframes_dict['iframe_2_text'] = WebDriver().find_element(('id', 'sampleHeading')).text
        WebDriver().switch_to().default_content()
        return iframes_dict
