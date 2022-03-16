from Framework.PageObjects.BaseObjects.base_form import BaseForm
from Framework.PageObjects.Elements.label import Label
from Framework.PageObjects.Elements.link import Link


class LinksPage(BaseForm):
    def __init__(self):
        super().__init__(
            form_name='links_page',
            uniq_element=Label(
                label_name='links_page_label',
                locator_type='xpath',
                locator='//div[@class="main-header" and text() = "Links"]'
            )
        )
        self.home_link = Link(link_name='home_link', locator_type='xpath', locator='//a[@id="simpleLink"]')

    def click_home_link(self):
        self.home_link.click()
