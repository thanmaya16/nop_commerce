from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Test.pages.loginpage import loginpage
from Test.pages.homepage import homepage



class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.set_page_load_timeout(10)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = loginpage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        print("Login complete")


    def test_logout_valid(self):
        driver = self.driver
        hp = homepage(driver)
        hp.click_dropdown()
        hp.click_logout()
        print("Logout complete")



        #self.driver.find_element(By.NAME, "username").send_keys("Admin")
        #self.driver.find_element(By.NAME, "password").send_keys("admin123")
        #self.driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
        #self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
        #self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-link").click()
        time.sleep(50)
#used to run in terminal without using --m command.
if __name__ == '__main__':
        unittest.main()






