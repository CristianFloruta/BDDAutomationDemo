from behave import *


@given('Homepage: I am on ebay.com homepage')
def step_impl(context):
    context.homepage_object.navigate_to_homepage()
    context.homepage_object.accept_cookies()


@when('Homepage: I enter "{product_name}" on search bar')
def step_impl(context, product_name):
    context.homepage_object.insert_search_value(product_name=product_name)


@when('Homepage: I select "{category_name}" from all categories dropdown menu')
def step_impl(context, category_name):
    context.homepage_object.select_category(category_name=category_name)


@when('Homepage: I click Search button')
def step_impl(context):
    context.homepage_object.click_search_button()


@when('Homepage: I click on Advanced search text link')
def step_impl(context):
    context.homepage_object.click_advanced_search_link()


@then('ResultPage: Minimum 1,000 results are retrieved')
def step_impl(context):
    pass
