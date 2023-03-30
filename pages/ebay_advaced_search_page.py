from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page


class Advanced_Search(Base_page):

    KEYWORD_TEXT = (By.ID, "_nkw")
    KEYWORD_OPTION = (By.ID, "s0-1-17-4[0]-7[1]-_in_kw")
    KEYWORD_EXCLUDE = (By.ID, "_ex_kw")
    SEARCH_CATEGORY = (By.ID, "s0-1-17-4[0]-7[3]-_sacat")
    ADVANCED_SEARCH_BUTTON = (By.XPATH, "/html/body/div[3]/div/main/form/fieldset[1]/div[5]/button")
    ADVANCED_SEARCH_BUTTON_BOTTOM = (By.XPATH, "//div[@class='adv-form__actions']//button[@type='submit']"
                                               "[normalize-space()='Search']")
    SOLD_ITEM_RADIO_BUTTON = (By.XPATH, "//input[@id='s0-1-17-5[1]-[2]-LH_Sold']")
    BUY_IT_NOW_RADIO_BUTTON = (By.XPATH, "//input[@id='s0-1-17-6[3]-[2]-LH_BIN']")
    NEW_CONDITION_RADIO_BUTTON = (By.XPATH, "//input[@id='s0-1-17-6[4]-[0]-LH_ItemCondition']")
    FREE_RETURNS_RADIO_BUTTON = (By.XPATH, "//input[@id='s0-1-17-5[5]-[0]-LH_FR']")
    WORLDWIDE_LOCATION_RADIO_BUTTON = (By.XPATH, "//input[@id='s0-1-17-6[7]-[4]-LH_PrefLoc']")
    AVAILABLE_TO_RADIO_BUTTON = (By.XPATH, "//input[@id='s0-1-17-6[7]-[6]-LH_AvailTo']")
    LOCATION_CATEGORY = (By.XPATH, "//select[@id='s0-1-17-6[7]-5[@field[]]_1-_saact']")
    FREE_SHIPPING_RADIO_BUTTON = (By.XPATH, "//input[@id='s0-1-17-5[6]-[0]-LH_FS']")
    NOT_SPECIFIED_RADIO_BUTTON = (By.XPATH, "//input[@id='s0-1-17-6[4]-[2]-LH_ItemCondition']")

    def enter_keyword_or_item_number(self, product_name):
        self.chrome.find_element(*self.KEYWORD_TEXT).send_keys(product_name)

    def enter_iphone(self):
        self.chrome.find_element(*self.KEYWORD_TEXT).send_keys("iphone")

    def select_keyword_option(self, keyword_choice):
        keyword_option_dropdown = Select(self.chrome.find_element(*self.KEYWORD_OPTION))
        keyword_option_dropdown.select_by_visible_text(keyword_choice)

    def exclude_keyword(self, exclude_brand):
        self.chrome.find_element(*self.KEYWORD_EXCLUDE).send_keys(exclude_brand)

    def select_category(self):
        select_category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORY))
        select_category_dropdown.select_by_visible_text("Clothing, Shoes & Accessories")

    def select_sold_item(self):
        self.chrome.find_element(*self.SOLD_ITEM_RADIO_BUTTON).click()

    def select_buy_it_now(self):
        self.chrome.find_element(*self.BUY_IT_NOW_RADIO_BUTTON).click()

    def select_new_as_condition(self):
        self.chrome.find_element(*self.NEW_CONDITION_RADIO_BUTTON).click()

    def select_free_returns(self):
        self.chrome.find_element(*self.FREE_RETURNS_RADIO_BUTTON).click()

    def select_unspecified_as_conditions(self):
        self.chrome.find_element(*self.NOT_SPECIFIED_RADIO_BUTTON).click()

    def select_worldwide_as_item_location(self):
        self.chrome.find_element(*self.WORLDWIDE_LOCATION_RADIO_BUTTON).click()

    def select_available_to(self):
        self.chrome.find_element(*self.AVAILABLE_TO_RADIO_BUTTON).click()

    def select_united_kingdom(self):
        category_dropdown = Select(self.chrome.find_element(*self.LOCATION_CATEGORY))
        category_dropdown.select_by_visible_text("United Kingdom")

    def select_free_shipping(self):
        self.chrome.find_element(*self.FREE_SHIPPING_RADIO_BUTTON).click()

    def click_search_button(self):
        self.chrome.find_element(*self.ADVANCED_SEARCH_BUTTON).click()

    def click_search_button_bottom(self):
        self.chrome.find_element(*self.ADVANCED_SEARCH_BUTTON_BOTTOM).click()

