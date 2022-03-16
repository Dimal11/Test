from Framework.PageObjects.BaseObjects.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, locator_type, locator, button_name):
        super().__init__(locator_type=locator_type, locator=locator, element_name=button_name)
