from context.driver import driver

def after_all(context):
    driver.stop_instance()
    