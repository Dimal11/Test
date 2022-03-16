from Framework.PageObjects.BaseObjects.base_form import BaseForm
from Framework.PageObjects.Elements.label import Label


class HomePage(BaseForm):

    def __init__(self):
        super().__init__(
            form_name='home_page',
            uniq_element=Label(
                locator_type='xpath',
                locator='//div[@id="app"]//div[contains(@class, "home-banner")]',
                label_name='home_page_uniq_element'
            )
        )
