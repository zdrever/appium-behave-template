from selenium.webdriver.common.by import By


class Locator:
    """Locator objects for finding Selenium WebElements"""
    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector

    def parameterize(self, *args):
        self.selector = self.selector.format(*args)


class HelloWorldLocators: 
    PAGE_TITLE = Locator(By.XPATH, "//div[@class='app']")
    DEVICE_READY = Locator(By.XPATH, "//p[text()='Device is Ready']")