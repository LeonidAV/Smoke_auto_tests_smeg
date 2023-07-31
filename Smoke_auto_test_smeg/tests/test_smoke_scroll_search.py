import datetime
import time

from selenium import webdriver


from pages_test_smoke_full_2.login_page import Login_page
from pages_test_smoke_full_2.main_page import Main_page
from pages_test_smoke_full_2.start_search_1_page import Start_search_page
from pages_test_smoke_full_2.scroll_filter_page import Scroll_filter_page
from pages_test_smoke_full_2.checkout_page import Checkout_page
def test_smoke():
    driver = webdriver.Chrome(executable_path='D:\\Хом драйвер и геко\\chromedriver_win32\\chromedriver.exe')

    print("Начало теста")

    en = Main_page(driver)
    en.first_main()

    login = Login_page(driver)
    login.authorization()
    time.sleep(5)

    sh = Start_search_page(driver)
    sh.search()

    sc = Scroll_filter_page(driver)
    sc.scroll_filter()

    checkout = Checkout_page(driver)
    checkout.checkout()

    print("Конец")
    time.sleep(5)
    driver.quit()
