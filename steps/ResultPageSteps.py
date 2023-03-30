from behave import *


@then('ResultPage: Minimum 1000 results are retrieved')
def step_impl(context):
    context.result_page_object.search_result_comparison_t1_t2()


@then('ResultPage: Minimum 300 results are retrieved')
def step_impl(context):
    context.result_page_object.search_result_comparison_t3()


@then('ResultPage: Minimum 400 results are retrieved')
def step_impl(context):
    context.result_page_object.search_result_comparison_t4()

@then('ResultPage: Minimum 100 results are retrieved')
def step_impl(context):
    context.result_page_object.search_result_comparison_t10()


@then('ResultPage: Minimum 500 results are retrieved')
def step_impl(context):
    context.result_page_object.search_result_comparison_t5()


@then('ResultPage: Minimum 600 results are retrieved')
def step_impl(context):
    context.result_page_object.search_result_comparison_t6()


@then('ResultPage: Minimum 1 result is retrieved')
def step_impl(context):
    context.result_page_object.search_result_comparison_t7()


@then('ResultPage: Minimum 800 results are retrieved')
def step_impl(context):
    context.result_page_object.search_result_comparison_t8()


@then('ResultPage: Minimum 900 results are retrieved')
def step_impl(context):
    context.result_page_object.search_result_comparison_t9()
