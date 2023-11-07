
from selenium.webdriver.common.by import By
from Test.Locators.locators import locators

class homepage():
    def __init__(self, driver):
        self.driver = driver
        self.popup_CLASS_NAME = locators.popup_CLASS_NAME
        self.paulcollings_dropdown_CLASS_NAME = locators.paulcollings_dropdown_CLASS_NAME
        self.logout_Button_LINK_TEXT = locators.logout_Button_LINK_TEXT


    def click_dropdown(self):
        self.driver.find_element(By.CLASS_NAME, self.paulcollings_dropdown_CLASS_NAME).click()


    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_Button_LINK_TEXT).click()

