from selenium import webdriver
from base.find_element import FindElement
import random
import time


class MarriedDeal():
    def __init__(self, url):
        self.driver = self.get_driver(url)

    # 获取driver
    def get_driver(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 获取定位元素
    def get_user_element(self, node, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(node, key)
        return user_element

    # 输入用户信息
    def send_user_info(self, node, key, data):
        self.get_user_element(node, key).send_keys(data)

    # 用户登录
    def user_login(self):
        self.get_user_element("Login", "login").click()
        self.send_user_info("Login", "user_email", "876522068@qq.com")
        self.send_user_info("Login", "login_password", "YGB123456")
        self.get_user_element("Login", "login_button").click()
        time.sleep(1)
        self.get_user_element("HomePage", "trading_hall").click()
        time.sleep(0.5)

    # 撮合交易
    def married_deal(self):
        for i in range(500):
            # 买
            price = str(round(random.uniform(0.1, 1), 2))
            volume = random.randint(1, 10)
            self.send_user_info("TradingHall", "buying_price", price)
            self.send_user_info("TradingHall", "buying_volume", volume)
            self.get_user_element("TradingHall", "buy_aic").click()
            self.send_user_info("TradingHall", "buy_password", "Y123456")
            self.get_user_element("TradingHall", "buy_ok")[1].click()
            time.sleep(0.5)
            # 卖
            self.send_user_info("TradingHall", "selling_price", price)
            self.send_user_info("TradingHall", "selling_volume", volume)
            self.get_user_element("TradingHall", "sell_aic").click()
            self.send_user_info("TradingHall", "sell_password", "Y123456")
            self.get_user_element("TradingHall", "sell_ok")[1].click()
            time.sleep(0.5)
        self.driver.close()


if __name__ == "__main__":
    run_main = MarriedDeal("https://www.topex.top/")
    run_main.user_login()
    run_main.married_deal()
