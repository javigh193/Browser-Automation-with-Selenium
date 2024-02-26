from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://techstepacademy.com/iframe-training")

# Switch to the iframe
iframe = browser.find_element(By.CSS_SELECTOR, "iframe")
browser.switch_to.frame(iframe)

welcome_text = browser.find_element(By.CSS_SELECTOR, "div#block-ec928cee802cf918d26c div p")
print(welcome_text.text)

# Accessing the contents of the parent page
browser.switch_to.default_content()
title_text = browser.find_element(By.CSS_SELECTOR, "div#block-5d3de848045889000188d389 div p")
print(title_text.text)

browser.quit()
