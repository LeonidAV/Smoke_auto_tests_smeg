import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class Scroll_filter_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    color = "//*[@id='s-category-filters']/form/div[2]/div/div[5]/label"
    category = "//*[@id='s-category-filters']/form/div[3]/div/div[2]/label/div"
    aesthetics = "//*[@id='s-category-filters']/form/div[4]/div/div[1]/label/div"
    scroll = "//*[@id='s-category-filters']/form/div[8]/h5"
    # system_clear_click = "//*[@id='s-category-filters']/form/div[6]/h5"
    # system_clear_end = "//*[@id='s-category-filters']/form/div[6]/div/div[2]/label/div/div"
    buy = "//*[@id='s-category-wrapper']/section/ul/li[1]/div[3]/form/div[2]/input"
    korzina = "//*[@id='s-category-wrapper']/section/ul/li[1]/div[3]/form/div[2]/input"
    oformlenie = "//*[@id='header-cart-wrapper']/div/form/div[3]/div[5]/a"

    def get_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color)))

    def get_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category)))

    def get_aesthetics(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.aesthetics)))

    # def get_system_clear_click(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.system_clear_click)))
    #
    # def get_system_clear_end(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.system_clear_end)))

    def get_buy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy)))

    def get_korzina(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.korzina)))

    def get_oformlenie(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.oformlenie)))

    def click_color(self):
        self.get_color().click()
        time.sleep(2)
        print("Цвет")

    def click_category(self):
        self.get_category().click()
        time.sleep(2)
        print("Категория")

    def click_aesthetics(self):
        self.get_aesthetics().click()
        time.sleep(2)
        print("Эстетика")

    # def click_system_clear_click(self):
    #     self.get_system_clear_click().click()
    #     time.sleep(2)
    #     print("Нажатие на Систему очистки")
    #
    # def click_system_clear_end(self):
    #     self.get_system_clear_end().click()
    #     time.sleep(2)
    #     print("Выбор Системы очистки")

    def click_buy(self):
        self.get_buy().click()
        time.sleep(2)
        print("Купить")

    def click_korzina(self):
        self.get_korzina().click()
        print("В корзину")

    def click_oformlenie(self):
        self.get_oformlenie().click()
        print("Оформить заказ")

    def scroll_filter(self):
        self.driver.maximize_window()
        self.click_color()
        self.click_category()
        self.click_aesthetics()
        self.click_buy()
        self.click_korzina()
        self.click_oformlenie()
