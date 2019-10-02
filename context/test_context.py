import os
import json

test_context = None


class TestContext(object):
    """Simple singleton class for managing and accessing settings"""

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = TestContext()
        return cls.instance

    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testsettings.json')) as f:
            test_settings = json.load(f)
            self.device_capabilities = test_settings['deviceCapabilities']
            self.appium_server = test_settings['appiumServer']
            self.driver_timeout = int(test_settings['driverTimeout'])


test_context = TestContext.get_instance()