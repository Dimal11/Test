from Project.PageObjects.Pages.web_tables_page import WebTablesPage


class ComparisonUsers:

    @staticmethod
    def comparison_users(user_data):
        user_list = WebTablesPage().get_users_from_table()
        result = False
        for user in user_list:
            if user_data.__eq__(user):
                result = True
                break

        return result
