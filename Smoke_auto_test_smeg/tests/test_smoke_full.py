import datetime
import time

from selenium import webdriver
from pages_test_smoke_full.checkout_page import Checkout_page
from pages_test_smoke_full.login_page import Login_page
from pages_test_smoke_full.main_page import Main_page
from pages_test_smoke_full.product_page import Product_page
from pages_test_smoke_full.start_search_1 import Start_mirco_page


def test_smoke():
    driver = webdriver.Chrome(executable_path='D:\\Хом драйвер и геко\\chromedriver_win32\\chromedriver.exe')

    print("Начало теста")

    en = Main_page(driver)
    en.first_main()

    login = Login_page(driver)
    login.authorization()
    time.sleep(5)

    search_1 = Start_mirco_page(driver)
    search_1.search_micro()

    product = Product_page(driver)
    product.product_1()

    checkout = Checkout_page(driver)
    checkout.checkout()

    print("Конец")
    time.sleep(5)
    driver.quit()
