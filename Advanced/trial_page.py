from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This classes should be in their respective modules
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
            EC.element_to_be_clickable(self.web_element)
        )
        element.click()
        return None
    
    def type_input(self, text):
        # should check that it is possible to type in the element
        self.web_element.clear()
        self.web_element.send_keys(text)
        return None
    
    @property
    def text(self):
        text = self.web_element.text
        return text

class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

# Start of this module 
class TrialPage(BasePage):
    url = "https://techstepacademy.com/trial-of-the-stones/"

    @property
    def stone_input(self):
        locator = (By.CSS_SELECTOR, "input#r1Input")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def stone_button(self):
        locator = (By.CSS_SELECTOR, "button#r1Btn")
        return BaseElement(self.driver, by=locator[0], value=locator[1])    

    @property
    def secrets_input(self):
        locator = (By.CSS_SELECTOR, "input#r2Input")
        return BaseElement(self.driver, by=locator[0], value=locator[1])    

    @property
    def secrets_button(self):
        locator = (By.CSS_SELECTOR, "button#r2Butn")
        return BaseElement(self.driver, by=locator[0], value=locator[1]) 

# Test should be in his own module   
# Test setup
browser = webdriver.Chrome()

# Trial Page
trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_input.type_input("rock")
trial_page.stone_button.click()
# For finishing the lecture's shake
input()
browser.quit()