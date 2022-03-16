from Framework.PageObjects.BaseObjects.base_form import BaseForm
from Framework.PageObjects.Elements.label import Label


class AlFrWinPage(BaseForm):
    def __init__(self):
        super().__init__(
            form_name='alerts_frame_windows_page',
            uniq_element=Label(
                locator_type='xpath',
                locator='//div[@class="main-header" and contains(text(),"Alerts, Frame & Windows")]',
                label_name='al_fr_win_uniq_element'
            )
        )


