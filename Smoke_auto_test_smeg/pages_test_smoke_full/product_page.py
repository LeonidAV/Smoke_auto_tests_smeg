from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    color = "//*[@class='jq-checkbox searchpro__page-filter_checkbox-field']"
    show = "//input[@class='searchpro__page-filters_button searchpro__page-filters_button--submit']"
    perehod = "//a[@title='Smeg SO4602M1NR']"
    purchase = "//input[@class='submit-wrapper-buy']"
    go_to_cart = "//a[@class='s-button']"
    order = "//a[@class='s-button s-submit']"

    def get_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color)))

    def get_show(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show)))

    def get_perehod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.perehod)))

    def get_purchase(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.purchase)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    def get_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order)))

    def click_color(self):
        self.get_color().click()
        print("Выбор цвета")

    def click_show(self):
        self.get_show().click()
        print("Показ")

    def click_perehod(self):
        self.get_perehod().click()
        print("Нажатие на товар")

    def click_purchase(self):
        self.get_purchase().click()
        print("Нажатие на кнопку КУПИТЬ")

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("Нажатие на кнопку перейти в корзину")

    def click_order(self):
        self.get_order().click()
        print("Нажатие на кнопку оформить заказ")

    def product_1(self):
        self.driver.maximize_window()
        self.click_color()
        self.click_show()
        self.click_perehod()
        self.click_purchase()
        self.click_go_to_cart()
        self.click_order()
