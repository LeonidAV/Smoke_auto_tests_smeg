from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class Main_page(Base):

    url = 'https://smeg-store.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    entrance = "//a[@href='/login/']"

    def get_entrance(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.entrance)))

    def click_entrance(self):
        self.get_entrance().click()
        print("Нажали на кнопку ВХОД")

    def first_main(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_entrance()