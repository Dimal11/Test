from Framework.PageObjects.BaseObjects.base_element import BaseElement


class Link(BaseElement):
    def __init__(self, locator_type, locator, link_name):
        super().__init__(locator_type=locator_type, locator=locator, element_name=link_name)
