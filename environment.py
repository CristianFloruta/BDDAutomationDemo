from browser import Browser
from pages.ebay_homepage import Homepage
from pages.ebay_advaced_search_page import Advanced_Search
from pages.ebay_result_page import ResultPage


def before_all(context):
    context.browser = Browser()
    context.homepage_object = Homepage()
    context.advanced_search_object = Advanced_Search()
    context.result_page_object = ResultPage()


def after_all(context):
    context.browser.close()