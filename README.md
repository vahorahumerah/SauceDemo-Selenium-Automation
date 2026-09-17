# SauceDemo Selenium Automation

## Overview

SauceDemo Selenium Automation is a Web UI Test Automation project developed using **Python and Selenium WebDriver**. The project automates key functional scenarios of the SauceDemo e-commerce application and validates the complete user journey from login to successful order placement.

This project demonstrates practical knowledge of **QA Automation, Functional Testing, Selenium WebDriver, Python, Web Element Locators, Explicit Waits, Assertions, and End-to-End Test Execution**.

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
End-to-End workflow automation

Explicit waits are used to improve synchronization between the automation script and the web application.

Test Credentials

The SauceDemo public test account is used for automation.

Username: standard_user
Password: secret_sauce

Test Execution Results

The implemented automation scenarios were executed successfully.

Test Scenario	Result
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
🎥 Automation Demo

## 🎥 Automation Demo

A video demonstration of the Selenium automation workflow is available below.

[▶️ Watch Selenium Automation Demo](https://drive.google.com/file/d/185W4S5LRE3ETEDP6LUmlfBF5290aciJm/view?usp=sharing)

The demonstration covers the automated SauceDemo workflow from login through successful order placement.
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
Google Chrome
Installation

Install Python 3.x and Google Chrome before running the project.

Install Selenium
pip install selenium
Clone the Repository
git clone https://github.com/vahorahumerah/SauceDemo-Selenium-Automation.git
Navigate to the Project Directory
cd SauceDemo-Selenium-Automation
Run an Individual Test
python login_test.py
Run Order Placement Test
python order_test.py
Future Enhancements

The project can be further enhanced by implementing:

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

This project demonstrates an end-to-end Selenium WebDriver automation workflow for the SauceDemo application using Python.

Author

Humerah Vahora

B.Tech Information Technology
Anand Agricultural University, Gujarat, India
