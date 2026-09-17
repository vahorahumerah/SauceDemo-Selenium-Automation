from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
time.sleep(10)
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

try:
    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Login
    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for Inventory
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

    # Checkout
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "checkout")
        )
    ).click()

    # IMPORTANT: wait for actual checkout form
    first_name = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "first-name")
        )
    )

    # Customer information
    first_name.send_keys("Humerah")

    last_name = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "last-name")
        )
    )
    last_name.send_keys("Vahora")

    postal_code = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "postal-code")
        )
    )
    postal_code.send_keys("388001")

    # Continue
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "continue")
        )
    ).click()

    # Wait for Overview
    finish_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "finish")
        )
    )

    # Finish order
    finish_button.click()
    time.sleep(5)

    # Verify confirmation
    confirmation = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    ).text

    if confirmation == "Thank you for your order!":
        print("ORDER PLACEMENT TEST: PASS")
    else:
        print("ORDER PLACEMENT TEST: FAIL")

finally:

    driver.quit()