from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome
driver = webdriver.Chrome()

# Open SauceDemo
driver.get("https://www.saucedemo.com/")

# Maximize browser
driver.maximize_window()

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Wait
time.sleep(2)

# Verify Inventory page
inventory_title = driver.find_element(By.CLASS_NAME, "title").text

if inventory_title == "Products":
    print("INVENTORY PAGE TEST: PASS")
else:
    print("INVENTORY PAGE TEST: FAIL")

# Close browser
driver.quit()