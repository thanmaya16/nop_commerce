import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class login_page(unittest.TestCase):

    @classmethod
    def set_up(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def login_page(self, driver):
        # self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        # self.driver.find_element(By.ID, "Email").click()
        # self.driver.find_element(By.ID, "Password").click()
        # self.driver.find_element(By.CLASS_NAME, "button-1").click()
        # self.driver.find_element(By.LINK_TEXT, "Logout").click()
       # time.sleep(10)

#locators
testbox_username_ID = "Email"
testbox_password_ID = "Password"
button_login_classname = "button-1"
button_logout_linktext = "Logout"

def __init__(self,driver):
    self.driver = driver

#login page
def enterusername(self, username):
    self.driver.find_element(By.ID, self.testbox_username_ID).click()
def enterpassword(self, Password) :
    self.driver.find_element(By.ID, self.testbox_password_ID ).click()

def clickbutton(self, login):
    self.driver.find_element(By.CLASS_NAME, self.button_login_classname).click()
#homepage
def clicklogout(self, logout):
    self.driver.find_element(By.CLASS_NAME, self.button_logout_linktext).click()

