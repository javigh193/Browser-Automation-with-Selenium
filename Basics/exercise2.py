from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/trial-of-the-stones")

# Riddle of Stones
stone_input = browser.find_element(By.ID, "r1Input")
stone_answer_btn = browser.find_element(By.CSS_SELECTOR, "button#r1Btn")
stone_result = browser.find_element(By.CSS_SELECTOR, "div#passwordBanner > h4")

# Riddle of Secrets
secrets_input = browser.find_element(By.CSS_SELECTOR, "input#r2Input")
secrets_answer_btn = browser.find_element(By.CSS_SELECTOR, "button#r2Butn")

# Two Merchants
# Simple Approach
richest_merchant_name = browser.find_element(By.XPATH, "//p[text()='3000']/../span").text
merchant_input = browser.find_element(By.ID, "r3Input")
merchant_answer_btn = browser.find_element(By.CSS_SELECTOR, "button#r3Butn")

# Check Results
check_btn = browser.find_element(By.CSS_SELECTOR, "button[name='checkButn']")
complete_msg = browser.find_element(By.CSS_SELECTOR, "div#trialCompleteBanner h4")

# Actions
stone_input.send_keys('rock')
stone_answer_btn.click()
password = stone_result.text

secrets_input.send_keys(password)
secrets_answer_btn.click()

merchant_input.send_keys(richest_merchant_name)
merchant_answer_btn.click()

check_btn.click()
assert complete_msg.text == "Trial Complete", "Something went wrong, Trial Failed"
print("Trial Completed Successfully")

browser.quit()