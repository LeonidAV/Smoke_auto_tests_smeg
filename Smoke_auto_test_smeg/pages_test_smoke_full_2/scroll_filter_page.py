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
    system_clear_1 = "//*[@class='s-filter-group collapsed']"
    system_clear_2 = "//*[@id='s-category-filters']/form/div[6]/div/div[2]/label"
    buy = "//*[@id='s-category-wrapper']/section/ul/li[1]/div[3]/form/div[2]/input"
    korzina = "//*[@id='s-category-wrapper']/section/ul/li[1]/div[3]/form/div[2]/input"
    oformlenie = "//*[@id='header-cart-wrapper']/div/form/div[3]/div[5]/a"
    word = '//*[@id="s-category-wrapper"]/section/ul/li[1]/div[2]/h5/a'

    def get_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color)))

    def get_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category)))

    def get_aesthetics(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.aesthetics)))

    def get_system_clear_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.system_clear_1)))

    def get_system_clear_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.system_clear_2)))

    def get_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word)))

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

    def click_system_clear_1(self):
        self.get_system_clear_1().click()
        time.sleep(2)
        print("Нажатие на Систему очистки")

    def click_system_clear_2(self):
        self.get_system_clear_2().click()
        time.sleep(2)
        print("Выбор Системы очистки")

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
        self.get_scroll_1()
        self.click_system_clear_1()
        self.click_system_clear_2()
        time.sleep(2)
        self.assert_word(self.get_word(), 'Smeg SO6302TX')
        self.click_buy()
        self.click_korzina()
        self.click_oformlenie()
