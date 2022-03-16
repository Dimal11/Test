from Framework.PageObjects.BaseObjects.base_form import BaseForm
from Framework.PageObjects.Elements.button import Button


class NavMenu(BaseForm):
    def __init__(self):
        super().__init__(form_name='nav_menu')

    @staticmethod
    def click_nav_button(button_name):
        Button(
            button_name=f'{button_name}',
            locator_type='xpath',
            locator=f'//*[text()="{button_name}"]'
            ).click()



