from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest
from random import random

class Test(unittest.TestCase):
    def type_initialize(self):
        # Initialization
        driver = webdriver.Chrome()
        driver.get("https://monkey-type.com/")
        prompt = input('Login?(y/n): ')
        # Optional login
        if prompt == 'y':
            driver.find_element_by_xpath('//div[@class="icon-button login"]').click()
            time.sleep(2)
            driver.find_element_by_xpath("//div[@class='login side']//input[@type='text']").click()
            email = input('E-mail: ')
            pw = input('Password: ')
            login = ActionChains(driver)
            login.send_keys(email).perform()
            driver.find_element_by_xpath("//div[@class='login side']//input[@type='password']").click()
            login = ActionChains(driver)
            login.send_keys(pw).perform()
            driver.find_element_by_xpath("//div[@class='login side']//div[@class='button']").click()
        while True:
            try:
                ready_inp = input("Start?(y): ")
                while ready_inp != 'y':
                    ready_inp = input("Ready: ")
                elem = driver.find_element_by_xpath('//div[@class="word active"]')
                while elem:
                    elem = driver.find_element_by_xpath('//div[@class="word active"]')
                    word = elem.text + ' '
                    for character in word:
                        actions = ActionChains(driver)
                        actions.send_keys(character)
                        time.sleep(random() * 0.05)
                        actions.perform()
            except:
                continue



runOne = Test()
runOne.type_initialize()

if __name__ == "__main__":
    unittest.main()
