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

@when('AdvancedSearchPage: I enter iphone in Enter keyword or item number block')
def step_impl(context):
    context.advanced_search_object.enter_iphone()


@when('AdvancedSearchPage: I select Sold items from Search including box')
def step_impl(context):
    context.advanced_search_object.select_sold_item()


@when('AdvancedSearchPage: I click Search button from page bottom')
def step_impl(context):
    context.advanced_search_object.click_search_button_bottom()


@when('AdvancedSearchPage: I select buy it now from Buying Format block')
def step_impl(context):
    context.advanced_search_object.select_buy_it_now()


@when('AdvancedSearchPage: I select New from Condition block')
def step_impl(context):
    context.advanced_search_object.select_new_as_condition()


@when('AdvancedSearchPage: I select Free returns from Show Results block')
def step_impl(context):
    context.advanced_search_object.select_free_returns()


@when('AdvancedSearchPage: I select Worldwide from Item Location block')
def step_impl(context):
    context.advanced_search_object.select_worldwide_as_item_location()


@when('AdvancedSearchPage: I select Free Shipping from Shipping Options block')
def step_impl(context):
    context.advanced_search_object.select_free_shipping()

@when('AdvancedSearchPage: I select NotSpecified from Condition block')
def step_impl(context):
    context.advanced_search_object.select_unspecified_as_conditions()


@when('AdvancedSearchPage: I select Available To from Item Location block')
def step_impl(context):
    context.advanced_search_object.select_available_to()


@when('AdvancedSearchPage: I select United Kingdom')
def step_impl(context):
    context.advanced_search_object.select_united_kingdom()




