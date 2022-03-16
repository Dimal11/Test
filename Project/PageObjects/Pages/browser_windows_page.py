from Framework.PageObjects.BaseObjects.base_form import BaseForm
from Framework.PageObjects.Elements.label import Label
from Framework.PageObjects.Elements.button import Button


class BrowserWindowsPage(BaseForm):
    def __init__(self):
        super().__init__(
            form_name='browser_windows_page',
            uniq_element=Label(
                label_name='browser_windows',
                locator_type='xpath',
                locator='//div[@class="main-header" and contains(text(),"Browser Windows")]'
            )
        )
        self.new_tab_button = Button(button_name='new_tab', locator_type='xpath', locator='//button[@id="tabButton"]')

    def click_new_tab_button(self):
        self.new_tab_button.click()
