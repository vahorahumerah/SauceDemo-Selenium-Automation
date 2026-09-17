from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Open Chrome
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Open SauceDemo
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Login
wait.until(
    EC.visibility_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Wait for Inventory page
wait.until(EC.url_contains("inventory"))

# Add Backpack
wait.until(
    EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack")
    )
).click()

# Click Cart
wait.until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "shopping_cart_link")
    )
).click()

# Verify Cart page
wait.until(EC.url_contains("cart"))

# Verify product name
product_name = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "inventory_item_name")
    )
).text
time.sleep(5)

if product_name == "Sauce Labs Backpack":
    print("CART PRODUCT TEST: PASS")
else:
    print("CART PRODUCT TEST: FAIL")

# Close browser
driver.quit()