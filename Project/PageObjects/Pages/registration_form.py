from Framework.PageObjects.BaseObjects.base_form import BaseForm
from Framework.PageObjects.Elements.label import Label
from Framework.PageObjects.Elements.input import Input
from Framework.BrowserFactory.browser import WebDriver


class RegistrationForm(BaseForm):
    def __init__(self):
        super().__init__(
            form_name='registration_form',
            uniq_element=Label(
                label_name='registration_form_label',
                locator_type='xpath',
                locator='//div[@id="registration-form-modal"]'
            )
        )
        self.first_name_input = Input(
            input_name='first_name_input',
            locator_type='xpath',
            locator='//input[@id="firstName"]'
        )
        self.last_name_input = Input(
            input_name='last_name_input',
            locator_type='xpath',
            locator='//input[@id="lastName"]'
        )
        self.email_input = Input(
            input_name='email_input',
            locator_type='xpath',
            locator='//input[@id="userEmail"]'
        )
        self.age_input = Input(
            input_name='age_input',
            locator_type='xpath',
            locator='//input[@id="age"]'
        )
        self.salary_input = Input(
            input_name='salary_input',
            locator_type='xpath',
            locator='//input[@id="salary"]'
        )
        self.department_input = Input(
            input_name='department_input',
            locator_type='xpath',
            locator='//input[@id="department"]'
        )

    def set_user_in_form(self, user):
        self.first_name_input.send_keys(user.first_name)
        self.last_name_input.send_keys(user.last_name)
        self.email_input.send_keys(user.email)
        self.age_input.send_keys(user.age)
        self.salary_input.send_keys(user.salary)
        self.department_input.send_keys(user.department)

    @classmethod
    def form_submit(cls):
        WebDriver().submit(('id', 'userForm'))

        






