from selenium.webdriver.common.by import By
from pages.base_page import Base_page


class ResultPage(Base_page):

    EXPECTED_TEST_VALUE_T1_T2 = 1000
    EXPECTED_TEST_VALUE_T3 = 300
    EXPECTED_TEST_VALUE_T4 = 400
    EXPECTED_TEST_VALUE_T5 = 500
    EXPECTED_TEST_VALUE_T6 = 600
    EXPECTED_TEST_VALUE_T7 = 1
    EXPECTED_TEST_VALUE_T8 = 800
    EXPECTED_TEST_VALUE_T9 = 900
    EXPECTED_TEST_VALUE_T10 = 100
    SEARCH_RESULT = (By.CSS_SELECTOR, "div[class='srp-controls__control srp-controls__count'] span:nth-child(1)")

    def search_result_comparison_t1_t2(self):
        text = self.chrome.find_element(*self.SEARCH_RESULT).text
        actual_search_result = int(text.replace(",", ""))
        print(text)
        assert actual_search_result >= self.EXPECTED_TEST_VALUE_T1_T2, f'ERROR: Expected: ' \
                                                                       f'{self.EXPECTED_TEST_VALUE_T1_T2}, Actual: ' \
                                                                       f'{actual_search_result}'
    def search_result_comparison_t3(self):
        text = self.chrome.find_element(*self.SEARCH_RESULT).text
        actual_search_result = int(text.replace(",", ""))
        print(text)
        assert actual_search_result >= self.EXPECTED_TEST_VALUE_T3, f'ERROR: Expected: ' \
                                                                       f'{self.EXPECTED_TEST_VALUE_T3}, Actual: ' \
                                                                       f'{actual_search_result}'
    def search_result_comparison_t4(self):
        text = self.chrome.find_element(*self.SEARCH_RESULT).text
        actual_search_result = int(text.replace(",", ""))
        print(text)
        assert actual_search_result >= self.EXPECTED_TEST_VALUE_T4, f'ERROR: Expected: ' \
                                                                       f'{self.EXPECTED_TEST_VALUE_T4}, Actual: ' \
                                                                       f'{actual_search_result}'

    def search_result_comparison_t5(self):
        text = self.chrome.find_element(*self.SEARCH_RESULT).text
        actual_search_result = int(text.replace(",", ""))
        print(text)
        assert actual_search_result >= self.EXPECTED_TEST_VALUE_T5, f'ERROR: Expected: ' \
                                                                       f'{self.EXPECTED_TEST_VALUE_T5}, Actual: ' \
                                                                       f'{actual_search_result}'


    def search_result_comparison_t6(self):
        text = self.chrome.find_element(*self.SEARCH_RESULT).text
        actual_search_result = int(text.replace(",", ""))
        print(text)
        assert actual_search_result >= self.EXPECTED_TEST_VALUE_T6, f'ERROR: Expected: ' \
                                                                       f'{self.EXPECTED_TEST_VALUE_T6}, Actual: ' \
                                                                       f'{actual_search_result}'

    def search_result_comparison_t7(self):
        text = self.chrome.find_element(*self.SEARCH_RESULT).text
        actual_search_result = int(text.replace(",", ""))
        print(text)
        assert actual_search_result >= self.EXPECTED_TEST_VALUE_T7, f'ERROR: Expected: ' \
                                                                       f'{self.EXPECTED_TEST_VALUE_T7}, Actual: ' \
                                                                       f'{actual_search_result}'

    def search_result_comparison_t8(self):
        text = self.chrome.find_element(*self.SEARCH_RESULT).text
        actual_search_result = int(text.replace(",", ""))
        print(text)
        assert actual_search_result >= self.EXPECTED_TEST_VALUE_T8, f'ERROR: Expected: ' \
                                                                       f'{self.EXPECTED_TEST_VALUE_T8}, Actual: ' \
                                                                       f'{actual_search_result}'

    def search_result_comparison_t9(self):
        text = self.chrome.find_element(*self.SEARCH_RESULT).text
        actual_search_result = int(text.replace(",", ""))
        print(text)
        assert actual_search_result >= self.EXPECTED_TEST_VALUE_T5, f'ERROR: Expected: ' \
                                                                       f'{self.EXPECTED_TEST_VALUE_T9}, Actual: ' \
                                                                       f'{actual_search_result}'

    def search_result_comparison_t10(self):
        text = self.chrome.find_element(*self.SEARCH_RESULT).text
        actual_search_result = int(text.replace(",", ""))
        print(text)
        assert actual_search_result >= self.EXPECTED_TEST_VALUE_T10, f'ERROR: Expected: ' \
                                                                       f'{self.EXPECTED_TEST_VALUE_T10}, Actual: ' \
                                                                       f'{actual_search_result}'