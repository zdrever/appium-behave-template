from pages.page import Page
from pages.locators import HelloWorldLocators
from selenium.common.exceptions import NoSuchElementException


class HelloWorld(Page):

    def __init__(self):
        super().__init__()

    def is_page_loaded(self):
        try:
            self._driver.find_element(HelloWorldLocators.PAGE_TITLE)
            return True
        except(NoSuchElementException):
            return False

    def is_device_ready(self):
        try:
            self._driver.find_element(HelloWorldLocators.DEVICE_READY)
            return True
        except(NoSuchElementException):
            return False


hello_world_page = HelloWorld()
