from selenium import webdriver
from base.find_element import FindElement
import time


class ActionMethod():

    # 打开浏览器
    def open_browser(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "Firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    # 输入地址
    def enter_url(self, url):
        self.driver.get(url)

    # 定位元素
    def get_element(self, node, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(node, key)
        return user_element

    # 输入信息数据
    def element_send_keys(self, node, key, value):
        element_send = self.get_element(node, key)
        element_send.send_keys(value)

    # 点击元素
    def click_element(self, node, key):
        self.get_element(node, key).click()

    # 等待时间
    def sleep_time(self):
        time.sleep(3)

    # 关闭浏览器
    def close(self):
        self.driver.close()

