from Framework.PageObjects.BaseObjects.base_form import BaseForm
from Framework.PageObjects.Elements.label import Label
from Framework.PageObjects.Elements.input import Input
from Project.Utils.local_time import LocalTime


class DatePickerPage(BaseForm):
    def __init__(self):
        super().__init__(
            form_name='date_picker_page',
            uniq_element=Label(
                label_name='date_picker_lbl',
                locator_type='xpath',
                locator='//div[@class="main-header" and contains(text(),"Date Picker")]'
            )
        )
        self.date_field = Input(
            input_name='date_input',
            locator_type='id',
            locator='datePickerMonthYearInput'
        )
        self.date_time_field = Input(
            input_name='date_time_input',
            locator_type='id',
            locator='dateAndTimePickerInput'
        )

    def get_date(self):
        return self.date_field._find_element().get_attribute('value')

    def get_date_time(self):
        return self.date_time_field._find_element().get_attribute('value')

    def date_construct(self):
        leap_year = LocalTime().get_closest_leap_year()
        return f'02/29/{leap_year}'

    def set_date(self, date):
        self.date_field.send_keys('\b\b\b\b\b\b\b\b\b\b')
        return self.date_field.send_keys(date)
