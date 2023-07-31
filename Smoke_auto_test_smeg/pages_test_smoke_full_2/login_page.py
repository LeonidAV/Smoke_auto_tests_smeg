from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class Login_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    login = "//input[@name='login']"
    password = "//input[@name='password']"
    enter = "//input[@class='wa-login-submit']"

    """Getters"""

    def get_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_enter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter)))

    """Actions"""

    def input_login(self, login):
        self.get_login().send_keys(login)
        print("Ввод логина")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Ввод пароля")

    def click_enter(self):
        self.get_enter().click()
        print("Нажатие кнопки войти")

    """Methods"""

    def authorization(self):
        self.driver.maximize_window()
        self.input_login("live112233@yandex.ru")
        self.input_password("live112233")
        self.click_enter()