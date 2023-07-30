from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class SearchHelper(BasePage):

    def text_input_and_search(self, text):
        locator_search_string = (By.TAG_NAME, 'textarea')
        search_string = self.find_element(locator_search_string)
        search_string.click()
        search_string.send_keys(text, Keys.ENTER)

    def assert_text_in_search_result(self, text):
        self.is_element_present(By.XPATH, f"(//div[@id=\"search\"]//h3[contains(text(), '{text}')])[3]")

