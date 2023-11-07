from Test.Locators.locators import locators
from selenium.webdriver.common.by import By
class loginpage():
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_NAME = locators.username_textbox_NAME
        self.password_textbox_NAME = locators.password_textbox_NAME
        self.login_button_CLASS_NAME = locators.login_button_CLASS_NAME
    def enter_username(self, username):
        self.driver.find_element(By.NAME,  self.username_textbox_NAME).clear()
        self.driver.find_element(By.NAME,  self.username_textbox_NAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_NAME ).clear()
        self.driver.find_element(By.NAME, self.password_textbox_NAME).send_keys(password)
    def click_login(self):
        self.driver.find_element(By.CLASS_NAME, self.login_button_CLASS_NAME ).click()


