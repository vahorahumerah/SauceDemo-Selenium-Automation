# SauceDemo Selenium Automation

## Overview

SauceDemo Selenium Automation is a web UI test automation project developed using **Python and Selenium WebDriver**. The project automates key functional scenarios of the SauceDemo e-commerce application and validates the complete user journey from login to successful order placement.

This project demonstrates practical experience in **QA Automation, functional testing, Selenium WebDriver, Python, web element locators, explicit waits, assertions, and end-to-end test execution**.

## Application Under Test

**Application:** SauceDemo  
**URL:** https://www.saucedemo.com/

## Technology Stack

- **Programming Language:** Python
- **Automation Tool:** Selenium WebDriver
- **Browser:** Google Chrome
- **IDE:** Visual Studio Code
- **Version Control:** Git
- **Repository:** GitHub

## Test Coverage

The following functional scenarios have been automated:

### 1. Login Testing
- Launch the SauceDemo application.
- Enter valid username and password.
- Click the Login button.
- Verify successful navigation to the Inventory page.

### 2. Inventory Testing
- Verify the Inventory page is displayed.
- Verify products are available.
- Validate product listing after successful login.

### 3. Add to Cart Testing
- Select a product from the Inventory page.
- Click the Add to Cart button.
- Verify that the product is successfully added to the cart.

### 4. Cart Testing
- Open the Shopping Cart.
- Verify the selected product is displayed.
- Validate the cart product information.

### 5. Checkout Testing
- Navigate to the Checkout page.
- Verify the Checkout Information page.
- Enter customer information.
- Continue to the Order Overview page.

### 6. Order Placement Testing
- Verify order information.
- Click the Finish button.
- Verify the order confirmation message.
- Validate successful order placement.

## End-to-End Test Flow

```text
Login
  ↓
Inventory
  ↓
Add Product to Cart
  ↓
Shopping Cart
  ↓
Checkout
  ↓
Customer Information
  ↓
Order Overview
  ↓
Place Order
  ↓
Order Confirmation
Project Structure
SauceDemo-Selenium-Automation/
│
├── login_test.py
├── inventory_test.py
├── add_to_cart_test.py
├── cart_test.py
├── checkout_test.py
├── order_test.py
│
└── README.md
Automation Approach

The automation scripts use Selenium WebDriver to interact with web elements and validate application behavior.

The project uses:

ID and Class Name locators
Explicit waits using WebDriverWait
Expected Conditions
Element visibility validation
Element clickability validation
Text-based assertions
End-to-end workflow automation

Explicit waits are used to improve synchronization between the automation script and the web application.

Test Credentials

The SauceDemo public test account is used for automation:

Username: standard_user
Password: secret_sauce

Test Execution Results

The implemented automation scenarios were executed successfully.

Test Case	Result
Login Test	PASS
Inventory Test	PASS
Add to Cart Test	PASS
Cart Test	PASS
Checkout Test	PASS
Order Placement Test	PASS
Execution Output
LOGIN TEST: PASS
INVENTORY PAGE TEST: PASS
ADD TO CART TEST: PASS
CART PRODUCT TEST: PASS
CHECKOUT PAGE TEST: PASS
ORDER PLACEMENT TEST: PASS
Demo Video

A demonstration of the Selenium automation execution is available here:

Watch Selenium Automation Demo

The video demonstrates the automated SauceDemo workflow from login through successful order placement.

Skills Demonstrated

QA & Testing

Functional Testing
Manual Testing
Test Case Design
Test Execution
End-to-End Testing
Validation
Defect Identification

Automation

Selenium WebDriver
Python
Web Element Locators
Explicit Waits
Assertions
Browser Automation

Development Tools

Visual Studio Code
Git
GitHub
Chrome
Installation

Install Python 3.x and Google Chrome before running the project.

Install Selenium using:

pip install selenium

Clone the repository:

git clone https://github.com/vahorahumerah/SauceDemo-Selenium-Automation.git

Navigate to the project directory:

cd SauceDemo-Selenium-Automation

Run an individual test:

python login_test.py

For example, to execute the complete order placement scenario:

python order_test.py
Future Enhancements

The current project can be further improved by implementing:

Pytest test framework
Page Object Model (POM)
Reusable automation functions
Centralized WebDriver configuration
Automated HTML test reports
Screenshots on test failure
Parameterized test data
CI/CD integration
Project Status

Completed

The project successfully demonstrates an end-to-end Selenium WebDriver automation workflow for the SauceDemo application.

Author

Humerah Vahora

B.Tech Information Technology
Anand Agricultural University, Gujarat, India
