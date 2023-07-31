from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class Start_search_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    smeg = "//*[@class='no-print-inline']"
    bit_tech = "//*[@class='s-catalog-button']"
    dyh_shkaf = "//*[@id='s-fixed-header']/div/div[2]/div/ul/li[1]/a"



    def get_smeg(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smeg)))

    def get_bit_tech(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bit_tech)))

    def get_dyh_shkaf(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dyh_shkaf)))

    def click_smeg(self):
        self.get_smeg().click()
        print("Нажали на логотип Smeg")

    def click_bit_tech(self):
        self.get_bit_tech().click()
        print("Нажали на Бытовая Техника")

    def click_dyh_shkaf(self):
        self.get_dyh_shkaf().click()
        print("Нажали на Духовые Шкафы")

    def search(self):
        self.driver.maximize_window()
        self.click_smeg()
        self.click_bit_tech()
        self.click_dyh_shkaf()