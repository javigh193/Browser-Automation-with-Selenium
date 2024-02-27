from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseElement(object):
    def __init__(self, driver, value, by):
        self.driver = driver
        self.locator = by, value
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator)
            )
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator=self.locator)
        )
        element.click()
        return None
    
    @property
    def text(self):
        text = self.web_element.text
        return text

class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://techstepacademy.com/training-ground/"

    def go(self):
        self.driver.get(self.url)

    @property
    def button1(self):
        locator = (By.ID, "b1")
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value=locator[1]
        )
    
# Our Test
browser = webdriver.Chrome()

test_val = 'Button1'

trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
trng_page.button1.text
assert trng_page.button1.text == test_val, f"Test failed: Button text did not match expected value: {test_val}"
print("Test passed")

browser.quit()