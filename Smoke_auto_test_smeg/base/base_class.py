import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method screenshot"""
    def get_screenshot(self):
        date = datetime.datetime.utcnow().strftime("%Y,%m,%d,%H,%M,%S")
        name_screenshot = 'screenshot' + date + '.png'
        self.driver.save_screenshot(
            'D:\\Мои проекты и тестирование\\Тестирование\\Новая папка\\Smoke_auto_test_smeg\\screen\\' + name_screenshot)

    """Scroll 1"""

    def get_scroll_1(self):
        action = ActionChains(self.driver)
        red = self.driver.find_element(By.XPATH, "//*[@id='s-category-filters']/form/div[9]/h5")
        action.move_to_element(red).perform()

    """Assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")