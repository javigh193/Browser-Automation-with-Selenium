from selenium import webdriver

# Multiple windows
browser1 = webdriver.Chrome()
browser2 = webdriver.Chrome()

browser1.get("https://techstepacademy.com/training-ground")
browser2.get("https://google.com")

# Multiple tabs
browser1.execute_script("window.open('https://google.com', '_blank')")
browser1.execute_script("window.open('https://yahoo.com', '_blank')")

# In the example, the order of the handles did not correspond with the order in which the different 
# tabs where opened in the actual browser. In my case, it did.
handles = browser1.window_handles
browser1.switch_to.window(handles[0])
browser1.switch_to.window(handles[1])

#browser1.quit()
#browser2.quit()