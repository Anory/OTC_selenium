from selenium import webdriver
from base.find_element import FindElement
import time


class HomePage():
    def __init__(self, url):
        self.driver = self.get_driver(url)

    def get_driver(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    def get_user_element(self,node, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(node, key)
        return user_element

    def main(self):
        self.get_user_element("HomePage", "trading_hall").click()
        time.sleep(0.5)
        self.get_user_element("HomePage", "home_page").click()
        time.sleep(0.5)
        self.get_user_element("HomePage", "c2c").click()
        time.sleep(0.5)
        self.get_user_element("HomePage", "help_center").click()
        time.sleep(0.5)
        self.get_user_element("HomePage", "topex").click()
        # self.get_user_element("HomePage", "trading_hall").click()
        # self.get_user_element("HomePage", "trading_hall").click()
        # self.get_user_element("HomePage", "trading_hall").click()
        time.sleep(3)
        self.driver.close()


if __name__ == "__main__":
    home = HomePage("http://www.topex.fat/")
    home.main()
