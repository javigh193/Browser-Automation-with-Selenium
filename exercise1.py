from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/training-ground")

input1_css_locator = "input[id='ipt1']"
button4_xpath_locator = "//button[@id='b4']"

input1_elem = browser.find_element(By.CSS_SELECTOR, input1_css_locator)
butn4_elem = browser.find_element(By.XPATH, button4_xpath_locator)

input1_elem.send_keys("Test text")
butn4_elem.click()
