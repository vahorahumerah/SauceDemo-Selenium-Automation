from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Open SauceDemo
driver.get("https://www.saucedemo.com/")

# Maximize browser
driver.maximize_window()

# Enter username
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# Enter password
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Click Login
driver.find_element(By.ID, "login-button").click()

# Wait for page to load
time.sleep(2)

# Verify Inventory page
if "inventory" in driver.current_url:
    print("LOGIN TEST: PASS")
else:
    print("LOGIN TEST: FAIL")

# Close browser
driver.quit()