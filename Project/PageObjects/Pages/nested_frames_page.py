from Framework.PageObjects.BaseObjects.base_form import BaseForm
from Framework.PageObjects.Elements.label import Label
from Framework.PageObjects.Elements.content import Content
from Framework.BrowserFactory.browser import WebDriver


class NestedFramesPage(BaseForm):
    def __init__(self):
        super().__init__(
            form_name='nested_frame_page',
            uniq_element=Label(
                label_name='nested_frames',
                locator_type='xpath',
                locator='//div[@class="main-header" and contains(text(),"Nested Frames")]'
            )
        )

    def get_iframe_text(self):
        frames_dict = {}
        parent_frame = WebDriver().find_element(('id', 'frame1'))
        WebDriver().switch_to().frame(parent_frame)
        frames_dict['parent_frame_text'] = Content(
            locator_type='xpath',
            locator='//body[contains(text(),"Parent frame")]',
            content_name='parent_frame'
        )._find_element().text
        child_frame = WebDriver().find_element(('tag name', 'iframe'))
        WebDriver().switch_to().frame(child_frame)
        frames_dict['child_frame_text'] = Content(
            locator_type='xpath',
            locator='//p',
            content_name='child_frame'
        )._find_element().text

        return frames_dict
