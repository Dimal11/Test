from Framework.PageObjects.BaseObjects.base_element import BaseElement


class Label(BaseElement):
    def __init__(self, locator_type, locator, label_name):
        super().__init__(locator_type=locator_type, locator=locator, element_name=label_name)
