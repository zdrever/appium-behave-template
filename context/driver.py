from appium import webdriver
from context.test_context import test_context


class Driver(object):
    """Singleton class for interacting with the selenium webdriver object"""
    instance = None

    class AppiumDriverNotFound(Exception):
        pass

    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = Driver()
        return cls.instance

    def __init__(self):
        self._driver = webdriver.Remote(
            test_context.appium_server, test_context.device_capabilities)
        self._driver.implicitly_wait(test_context.driver_timeout)
        
        # switch to webview for cross platform testing
        if test_context.device_capabilities['platformName'] == "Android":
            self._driver.switch_to.context(self._driver.contexts[-1])


    def get_driver(self):
        return self._driver

    def stop_instance(self):
        self._driver.quit()
        instance = None

    def find_element(self, locator):
        return self._driver.find_element(locator.l_type, locator.selector)


driver = Driver.get_instance()
