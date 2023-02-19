from browser import Browser
from pages.ebay_homepage import Homepage
from pages.ebay_advaced_search_page import Advanced_Search


def before_all(context):
    context.browser = Browser()
    context.homepage_object = Homepage()
    context.advanced_search_object = Advanced_Search()


def after_all(context):
    context.browser.close()