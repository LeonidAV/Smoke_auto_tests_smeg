from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from base.base_class import Base


class Checkout_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    name = "//input[@name='customer[firstname]']"
    surname = "//input[@name='customer[lastname]']"
    email = "//input[@name='customer[email]']"
    phone = "//input[@name='customer[phone]']"

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_surname(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.surname)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def input_name(self, name):
        self.get_name().clear()
        self.get_name().send_keys(name)
        print("Ввод имени")

    def input_surname(self, surname):
        self.get_surname().clear()
        time.sleep(2)
        self.get_surname().send_keys(surname)
        print("Ввод фамилии")

    def input_email(self, email):
        self.get_email().clear()
        time.sleep(2)
        self.get_email().send_keys(email)
        print("Ввод почты")

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print("Ввод телефона")

    def checkout(self):
        self.driver.maximize_window()
        self.input_name("Leonid")
        self.input_surname("Averyanov")
        self.input_email("live112233@yandex.ru")
        self.input_phone("89665754488")
        self.assert_url('https://smeg-store.ru/buy2/')
        self.get_screenshot()

