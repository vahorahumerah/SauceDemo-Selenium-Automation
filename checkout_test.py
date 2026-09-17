from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Login
wait.until(
    EC.visibility_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Inventory page
wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "title"))
)

# Add Backpack
wait.until(
    EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack")
    )
).click()

# Open Cart
wait.until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "shopping_cart_link")
    )
).click()

# Verify Cart
wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "inventory_item_name")
    )
)

# Click Checkout
wait.until(
    EC.element_to_be_clickable(
        (By.ID, "checkout")
    )
).click()

# Verify Checkout Information page
checkout_title = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "title")
    )
).text
time.sleep(5)

if checkout_title == "Checkout: Your Information":
    print("CHECKOUT PAGE TEST: PASS")
else:
    print("CHECKOUT PAGE TEST: FAIL")

# Close browser
driver.quit()