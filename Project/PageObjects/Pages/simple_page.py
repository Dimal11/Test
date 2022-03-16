from Framework.PageObjects.BaseObjects.base_form import BaseForm
from Framework.PageObjects.Elements.label import Label


class SimplePage(BaseForm):
    def __init__(self):
        super().__init__(
            form_name='simple_page',
            uniq_element=Label(
                label_name='simple_page_label',
                locator_type='xpath',
                locator='//*[contains(text(),"sample page")]'
            )
        )
