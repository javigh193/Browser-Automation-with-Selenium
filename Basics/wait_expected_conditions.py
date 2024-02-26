from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/training-ground")

# Playing with WebDriverWait
try:
    WebDriverWait(browser, 10).until(alert_is_present())
    print("An alert is present, accepting it.")
    alert = Alert(browser)
    alert.accept()
    print("Alert accepted.")
except Exception:
    print("Waiting time expired without an alert being present.")

# Playing with the Select Element
sel = browser.find_element(By.ID, "sel1")
my_select = Select(sel)
my_select.select_by_index(1)
try:
    assert my_select.first_selected_option.text == 'Beets'
    print("Everything went according to the plan.")
except Exception:
    print("Selected option contains unexpected text.")

browser.quit()