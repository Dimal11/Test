from Framework.PageObjects.BaseObjects.base_form import BaseForm
from Framework.PageObjects.Elements.label import Label
from Framework.PageObjects.Elements.button import Button
from Framework.PageObjects.Elements.content import Content
from selenium.webdriver.common.by import By
from Project.Utils.users import User


class WebTablesPage(BaseForm):
    def __init__(self):
        super().__init__(
            form_name='web_tables_page',
            uniq_element=Label(
                label_name='web_tables_label',
                locator_type='xpath',
                locator='//div[@class="main-header" and text() = "Web Tables"]'
            )
        )
        self.add_button = Button(
            button_name='add_button',
            locator_type='xpath',
            locator='//button[@id="addNewRecordButton"]'
        )
        self.table = Content(
            content_name='table',
            locator_type='xpath',
            locator='//div[@class="rt-tbody"]'
        )
        self.delete_user_button = Button(
            button_name='delete_user_button',
            locator_type='xpath',
            locator='//span[@id="delete-record-4"]'
        )

    def click_add_button(self):
        self.add_button.click()

    def get_users_from_table(self):
        object_list = []
        user_list = []
        table = self.table._find_element()
        rows = table.find_elements(By.XPATH, '//div[@role="row"]')

        for row in rows:
            cells = row.text
            cells_list = cells.split('\n')
            user_list.append(cells_list)

        for user in user_list:
            if len(user) < 6:
                continue
            user_data = \
                {
                    'first_name': user[0],
                    'last_name': user[1],
                    'age': user[2],
                    'email': user[3],
                    'salary': user[4],
                    'department': user[5],
                }

            object_list.append(User(user_data))
        return object_list

    def click_delete_user_button(self):
        self.delete_user_button.click()
