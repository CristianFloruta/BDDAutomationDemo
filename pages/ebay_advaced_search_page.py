from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page


class Advanced_Search(Base_page):

    KEYWORD_TEXT = (By.ID, "_nkw")
    KEYWORD_OPTION = (By.ID, "s0-1-17-4[0]-7[1]-_in_kw")
    KEYWORD_EXCLUDE = (By.ID, "_ex_kw")
    SEARCH_CATEGORY = (By.ID, "s0-1-17-4[0]-7[3]-_sacat")
    ADVANCED_SEARCH_BUTTON = (By.XPATH, "/html/body/div[3]/div/main/form/fieldset[1]/div[5]/button")


    def enter_keyword_or_item_number(self, product_name):
        self.chrome.find_element(*self.KEYWORD_TEXT).send_keys(product_name)

    def select_keyword_option(self, keyword_choice):
        keyword_option_dropdown = Select(self.chrome.find_element(*self.KEYWORD_OPTION))
        keyword_option_dropdown.select_by_visible_text(keyword_choice)

    def exclude_keyword(self, exclude_brand):
        self.chrome.find_element(*self.KEYWORD_EXCLUDE).send_keys(exclude_brand)

    def select_category(self):
        select_category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORY))
        select_category_dropdown.select_by_visible_text("Clothing, Shoes & Accessories")

    def click_search_button(self):
        self.chrome.find_element(*self.ADVANCED_SEARCH_BUTTON).click()