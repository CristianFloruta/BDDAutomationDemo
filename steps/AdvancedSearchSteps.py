from behave import *


@When('AdvancedSearchPage: I enter "{product_name}" in Enter keyword or item number block')
def step_impl(context, product_name):
    context.advanced_search_object.enter_keyword_or_item_number(product_name=product_name)


@When('AdvancedSearchPage: I select "{keyword_choice}" from keyword option list')
def step_impl(context, keyword_choice):
    context.advanced_search_object.select_keyword_option(keyword_choice=keyword_choice)


@When('AdvancedSearchPage: I enter "{exclude_brand}" in Exclude words from your search')
def step_impl(context, exclude_brand):
    context.advanced_search_object.exclude_keyword(exclude_brand=exclude_brand)


@When('AdvancedSearchPage: I click Search button')
def step_impl(context):
    context.advanced_search_object.click_search_button()



