# First example, less abstraction, harder to maintain
from selenium import webdriver
from selenium.webdriver.common.by import By

class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://techstepacademy.com/training-ground/"

    def go(self):
        self.driver.get(self.url)

    def type_ipt_field(self, text):
        ipt = self.driver.find_element(By.ID, "ipt1")
        ipt.clear()
        ipt.send_keys(text)
        return None

    def get_ipt_text(self):
        ipt = self.driver.find_element(By.ID, "ipt1")
        elem_text = ipt.get_attribute('value')
        return elem_text

    def click_btn_1(self):
        btn = self.driver.find_element(By.ID, "b1")
        btn.click()
        return None
    
# Our Test
browser = webdriver.Chrome()

test_val = 'Example text'

trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
trng_page.type_ipt_field(test_val)
# NEXT line would trigger and alert window, forcing us to interact with it in order to continue
# trng_page.click_btn_1()
txt_from_ipt = trng_page.get_ipt_text()
assert txt_from_ipt == test_val, f"Test Failed: Input did not match expected {test_val}."
print("Test passed")

browser.quit()