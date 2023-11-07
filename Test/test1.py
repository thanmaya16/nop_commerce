from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()
driver.maximize_window()  

driver.set_page_load_timeout(10)
driver.get("http://www.google.com")


def google_search(a):
    driver.find_element(By.NAME, 'q').send_keys("Automation Step by Step")
    driver.find_element(By.NAME, "btnK").click()

google_search(driver)
time.sleep(10)
driver.quit()
