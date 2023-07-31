import datetime

class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method screenshot"""
    def get_screenshot(self):
        date = datetime.datetime.utcnow().strftime("%Y,%m,%d,%H,%M,%S")
        name_screenshot = 'screenshot' + date + '.png'
        self.driver.save_screenshot(
            'D:\\Мои проекты и тестирование\\Тестирование\\Новая папка\\MyFirstAutoTests\\screen\\' + name_screenshot)

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")