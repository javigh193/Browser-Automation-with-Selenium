from selenium import webdriver
from trial_page import TrialPage
from training_ground_page import TrainingGroundPage

# Test Setup
browser = webdriver.Chrome()

# Trial Page Test
trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_input.type_input("rock")
trial_page.stone_button.click()

# For finishing the lecture's shake
input() 

# Training Ground Page Test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == "Button1", "Unexpected button1 text: {trng_page.button1.text}; expected: Button1."

# For finishing the lecture's shake
input()

browser.quit()