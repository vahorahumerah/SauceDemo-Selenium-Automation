from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Open Chrome
driver = webdriver.Chrome()

# Create explicit wait
wait = WebDriverWait(driver, 10)

# Open SauceDemo
driver.get("https://www.saucedemo.com/")

# Maximize browser
driver.maximize_window()

# Login
wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Wait for Inventory page
wait.until(EC.url_contains("inventory"))

# Find Backpack Add to Cart button
add_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack")
    )
)

# Click Add to Cart
add_button.click()

# Verify button changed to Remove
remove_button = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "remove-sauce-labs-backpack")
    )
)
time.sleep(5)

if remove_button.is_displayed():
    print("ADD TO CART TEST: PASS")
else:
    print("ADD TO CART TEST: FAIL")

# Close browser
driver.quit()