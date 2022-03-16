from Framework.PageObjects.BaseObjects.base_form import BaseForm
from Framework.PageObjects.Elements.content import Content
from Framework.PageObjects.Elements.button import Button


class AlertsPage(BaseForm):
    def __init__(self):
        super().__init__(
            form_name='alerts_page',
            uniq_element=Content(
                locator_type='xpath',
                locator='//div[@id="javascriptAlertsWrapper"]',
                content_name='alerts_uniq_element'
            )
        )
        self.see_alert_button = Button(
            button_name='see_alert',
            locator_type='xpath',
            locator='//button[@id="alertButton"]'
        )
        self.confirm_alert_button = Button(
            button_name='confirm_alert',
            locator_type='xpath',
            locator='//button[@id="confirmButton"]'
        )
        self.prompt_alert_button = Button(
            button_name='prompt_alert',
            locator_type='xpath',
            locator='//button[@id="promtButton"]'
        )
        self.after_confirm_alert_text = Content(
            content_name='selected_ok_text',
            locator_type='xpath',
            locator='//span[@id="confirmResult"]'
        )
        self.after_prompt_alert_text = Content(
            content_name='prompt_text',
            locator_type='xpath',
            locator='//span[@id="promptResult"]'
        )

    def click_to_button_see_alert(self):
        self.see_alert_button.click()

    def click_to_button_confirm_alert(self):
        self.confirm_alert_button.click()

    def click_to_button_prompt_alert(self):
        self.prompt_alert_button.click()

    def get_text_after_confirm_alert(self):
        return self.after_confirm_alert_text._find_element().text

    def get_text_after_prompt_alert(self):
        return self.after_prompt_alert_text._find_element().text
