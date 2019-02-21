from selenium import webdriver
from base.find_element import FindElement
import time


class RegisterFunction():
    def __init__(self, url):
        self.driver = self.get_driver(url)

    # 获取driver
    def get_driver(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 获取定位元素
    def get_user_element(self,node, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(node, key)
        return user_element

    # 输入用户信息
    def send_user_info(self, node,  key, data):
        self.get_user_element(node, key).send_keys(data)

    def main(self):
        self.send_user_info("RegisterElementOrRetrieve", "user_email", "876522068@qq.com")
        self.send_user_info("RegisterElementOrRetrieve", "user_code", "12df5")
        self.send_user_info("RegisterElementOrRetrieve", "user_password", "ygb123456")
        self.send_user_info("RegisterElementOrRetrieve", "again_password", "ygb123456")
        self.get_user_element("RegisterElementOrRetrieve", "check").click()
        self.get_user_element("RegisterElementOrRetrieve", "button").click()
        self.get_user_element("RegisterElementOrRetrieve", "button_forget").click()
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    register = RegisterFunction("http://www.topex.fat/forget")
    register.main()

