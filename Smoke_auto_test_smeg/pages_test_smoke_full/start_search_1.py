from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class Start_mirco_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    lypa = "//*[@class='icon-active-search']"
    click_stroka = "//input[@class='searchpro__field-input js-searchpro__field-input']"
    search = "//*[@class='searchpro__field-button js-searchpro__field-button']"

    def get_lypa(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.lypa)))

    def get_click_stroka(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.click_stroka)))

    def get_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search)))

    def click_lypa(self):
        self.get_lypa().click()
        print("Нажали на лупу")

    def input_click_stroka(self, click_stroka):
        self.get_click_stroka().send_keys(click_stroka)
        print("Ввели название товара")

    def click_search(self):
        self.get_search().click()
        print("Нажали на НАЙТИ")

    def search_micro(self):
        self.driver.maximize_window()
        self.click_lypa()
        self.input_click_stroka("Микроволновая печь")
        self.click_search()
