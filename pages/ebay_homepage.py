from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page


class Homepage(Base_page):

    HOMEPAGE_LINK = ("https://www.ebay.com/")
    SEARCH_TEXTBOX = (By.ID, "gh-ac")
    SEARCH_CATEGORY = (By.ID, "gh-cat")
    SEARCH_BUTTON = (By.ID, "gh-btn")
    ADVANCED_SEARCH_LINK = (By.ID, "gh-as-a")
    SEARCH_RESULT = (By.XPATH, "//h1//child::span[text()='12,000,000']")

    def navigate_to_homepage(self):
        self.chrome.get(self.HOMEPAGE_LINK)

    def insert_search_value(self, product_name):
        self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys(product_name)

    def select_category(self, category_name):
        category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORY))
        category_dropdown.select_by_visible_text(category_name)

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def click_advanced_search_link(self):
        self.wait_and_click_element_by_selector(*self.ADVANCED_SEARCH_LINK)

    def search_result_comparison(self):
        pass
