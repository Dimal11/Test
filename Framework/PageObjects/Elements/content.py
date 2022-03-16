from Framework.PageObjects.BaseObjects.base_element import BaseElement


class Content(BaseElement):
    def __init__(self, locator_type, locator, content_name):
        super().__init__(locator_type=locator_type, locator=locator, element_name=content_name)
