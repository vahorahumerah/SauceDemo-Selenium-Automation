# 🧪 SauceDemo Selenium Automation

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium)](https://www.selenium.dev/)
[![GitHub](https://img.shields.io/badge/Repository-GitHub-black?logo=github)](https://github.com/vahorahumerah/SauceDemo-Selenium-Automation)

## 📌 Overview

**SauceDemo Selenium Automation** is a **Web UI Test Automation project** developed using **Python** and **Selenium WebDriver**.

The project automates key functional scenarios of the **SauceDemo e-commerce application** and validates the complete user journey from **Login → Inventory → Cart → Checkout → Order Placement**.

This project demonstrates practical knowledge of **QA Automation, Functional Testing, Selenium WebDriver, Python, Web Element Locators, Explicit Waits, Assertions, and End-to-End Testing**.

---

## 🌐 Application Under Test

**Application:** SauceDemo  
**URL:** [https://www.saucedemo.com/](https://www.saucedemo.com/)

---

## 🛠️ Technology Stack

| Technology / Tool | Purpose |
|---|---|
| **Python** | Programming Language |
| **Selenium WebDriver** | Web UI Automation |
| **Google Chrome** | Browser |
| **Visual Studio Code** | Development Environment |
| **Git** | Version Control |
| **GitHub** | Source Code Management |

---

## 🧪 Test Coverage

### 1️⃣ Login Testing

- Launch the SauceDemo application
- Enter valid username and password
- Click the **Login** button
- Verify successful navigation to the **Inventory page**

### 2️⃣ Inventory Testing

- Verify the **Inventory page** is displayed
- Verify products are available
- Validate product listing after successful login

### 3️⃣ Add to Cart Testing

- Select a product from the Inventory page
- Click the **Add to Cart** button
- Verify that the product is successfully added to the cart

### 4️⃣ Cart Testing

- Open the **Shopping Cart**
- Verify the selected product is displayed
- Validate cart product information

### 5️⃣ Checkout Testing

- Navigate to the **Checkout page**
- Verify the **Checkout: Your Information** page
- Enter customer information
- Continue to the **Order Overview** page

### 6️⃣ Order Placement Testing

- Verify order information
- Click the **Finish** button
- Verify the order confirmation message
- Validate successful order placement

---

## 🔄 End-to-End Test Flow

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
```

---

## 📂 Project Structure

```text
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
```

---

## ⚙️ Automation Approach

The automation scripts use **Selenium WebDriver** to interact with web elements and validate application behavior.

### Key Automation Techniques

- **ID and Class Name locators**
- **Explicit waits using `WebDriverWait`**
- **Expected Conditions**
- **Element visibility validation**
- **Element clickability validation**
- **Text-based assertions**
- **End-to-End workflow automation**

Explicit waits are used to improve synchronization between the automation script and the web application.

---

## 🔐 Test Credentials

The project uses the publicly available SauceDemo test account.

**Username:** `standard_user`  
**Password:** `secret_sauce`

> These credentials are used only for testing the SauceDemo demo application.

---

## ✅ Test Execution Results

The implemented automation scenarios were executed successfully.

| Test Scenario | Result |
|---|:---:|
| **Login Test** | ✅ **PASS** |
| **Inventory Test** | ✅ **PASS** |
| **Add to Cart Test** | ✅ **PASS** |
| **Cart Test** | ✅ **PASS** |
| **Checkout Test** | ✅ **PASS** |
| **Order Placement Test** | ✅ **PASS** |

### 💻 Execution Output

```text
LOGIN TEST: PASS
INVENTORY PAGE TEST: PASS
ADD TO CART TEST: PASS
CART PRODUCT TEST: PASS
CHECKOUT PAGE TEST: PASS
ORDER PLACEMENT TEST: PASS
```

---

## 🎥 Automation Demo

A video demonstration of the Selenium automation workflow is available here:

### 👉 [▶️ Watch Selenium Automation Demo](https://drive.google.com/file/d/185W4S5LRE3ETEDP6LUmlfBF5290aciJm/view?usp=sharing)

The demonstration covers the automated SauceDemo workflow from **Login through successful Order Placement**.

---

## 🎯 Skills Demonstrated

### QA & Testing

- **Functional Testing**
- **Manual Testing**
- **Test Case Design**
- **Test Execution**
- **End-to-End Testing**
- **Validation**
- **Defect Identification**

### Automation

- **Selenium WebDriver**
- **Python**
- **Web Element Locators**
- **Explicit Waits**
- **Assertions**
- **Browser Automation**

### Development Tools

- **Visual Studio Code**
- **Git**
- **GitHub**
- **Google Chrome**

---

## 💻 Installation & Setup

### 1. Install Python

Install **Python 3.x** from:

[Python Official Website](https://www.python.org/)

### 2. Install Selenium

```bash
pip install selenium
```

### 3. Clone the Repository

```bash
git clone https://github.com/vahorahumerah/SauceDemo-Selenium-Automation.git
```

### 4. Navigate to the Project Directory

```bash
cd SauceDemo-Selenium-Automation
```

### 5. Run an Individual Test

```bash
python login_test.py
```

### 6. Run Order Placement Test

```bash
python order_test.py
```

---

## 🚀 Future Enhancements

The project can be further enhanced by implementing:

- **Pytest Test Framework**
- **Page Object Model (POM)**
- **Reusable Automation Functions**
- **Centralized WebDriver Configuration**
- **Automated HTML Test Reports**
- **Screenshots on Test Failure**
- **Parameterized Test Data**
- **CI/CD Integration**

---

## 📊 Project Status

**✅ Completed**

This project demonstrates an **end-to-end Selenium WebDriver automation workflow** for the SauceDemo application using Python.

---

## 👩‍💻 Author

### **Humerah Vahora**

**B.Tech Information Technology**  
**Anand Agricultural University, Gujarat, India**

🔗 **GitHub:** [github.com/vahorahumerah](https://github.com/vahorahumerah)

🔗 **Selenium Project:** [SauceDemo-Selenium-Automation](https://github.com/vahorahumerah/SauceDemo-Selenium-Automation)
