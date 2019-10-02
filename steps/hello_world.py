from behave import given, when, then
from pages.hello_world import hello_world_page

@given(u'I am on the splash page')
def on_splash_page(context):
    assert hello_world_page.is_page_loaded() is True

@then(u'I should see that my device is ready')
def device_ready(context): 
    assert hello_world_page.is_device_ready() is True

