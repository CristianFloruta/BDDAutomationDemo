from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page


class Homepage(Base_page):

    HOMEPAGE_LINK = ("https://www.ebay.com/")
    SEARCH_TEXTBOX = (By.ID, "gh-ac")
    SEARCH_CATEGORY = (By.ID, "gh-cat")
    SEARCH_BUTTON = (By.ID, "gh-btn")
    ADVANCED_SEARCH_LINK = (By.ID, "gh-as-a")
    SEARCH_RESULT = (By.CSS_SELECTOR, "div[class='srp-controls__control srp-controls__count'] span:nth-child(1)")
    EXPECTED_TEST_VALUE = 1000


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
        self.chrome.find_element(*self.ADVANCED_SEARCH_LINK).click()

    def search_result_comparison(self):
        text = self.chrome.find_element(*self.SEARCH_RESULT).text
        actual_result = text.replace(",", "")
        assert int(actual_result) > self.EXPECTED_TEST_VALUE, f"ERROR: Expected: {self.EXPECTED_TEST_VALUE}, Actual: " \
                                                              f"{int(actual_result)}"
