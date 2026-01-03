# 🧪 Selenium Automation Framework (Python)

## 📌 Project Overview

This repository contains a **Selenium automation framework built using Python**, designed for learning and practicing **UI test automation** with modern best practices.

The framework uses:

* **Selenium WebDriver** for browser automation
* **PyTest** as the test execution framework
* **Allure Reports** for test reporting
* **Virtual Environment (`.venv`)** for dependency isolation

The project focuses on:

* Writing clean and maintainable test cases
* Using PyTest fixtures
* Running tests via command line
* Generating professional test reports using Allure

---

## 🧑‍💻 Author

**Prashant Kavinkar**

---

## 🛠 Tech Stack

| Tool        | Purpose              |
| ----------- | -------------------- |
| Python 3.14 | Programming language |
| Selenium    | Browser automation   |
| PyTest      | Test framework       |
| Allure      | Test reporting       |
| Git         | Version control      |
| PyCharm     | IDE                  |

---

## 📂 Project Structure

```
Python/
│
├── Src/
│   └── ex_01_Selenium_Basics/
│       ├── test_Selenium_01.py
│       └── conftest.py
│
├── allure-results/
│
├── .venv/
│
├── README.md
│
└── pytest.ini (optional)
```

### 🔍 Explanation

* **Src/**
  Contains all source code and test files

* **ex_01_Selenium_Basics/**
  Beginner-level Selenium test examples

* **test_Selenium_01.py**
  Test case to validate CURA Healthcare demo website

* **conftest.py**
  Central place for PyTest fixtures (browser setup & teardown)

* **.venv/**
  Python virtual environment (not committed to Git)

* **allure-results/**
  Stores raw Allure test execution results

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
cd Python
```

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv .venv
```

---

### 3️⃣ Activate Virtual Environment (macOS / Linux)

```bash
source .venv/bin/activate
```

Expected prompt:

```
(.venv) ➜ Python git:(main)
```

---

### 4️⃣ Install Dependencies

```bash
pip install selenium pytest allure-pytest
```

---

## ▶️ How to Run Tests

### Run a Single Test File

```bash
pytest Src/ex_01_Selenium_Basics/test_Selenium_01.py
```

---

### Run Tests with Allure Report

```bash
pytest Src/ex_01_Selenium_Basics/test_Selenium_01.py --alluredir allure-results
```

---

## 📊 Generate Allure Report

### Serve Report Locally

```bash
allure serve allure-results
```

This will:

* Generate HTML report
* Open it automatically in browser

---

## 🧪 Sample Test Scenario

* Launch Chrome browser
* Open CURA Healthcare demo website
* Capture page source
* Validate page title text
* Close browser

---

## ✅ Best Practices Followed

* PyTest fixtures for browser lifecycle
* Proper test naming conventions
* Virtual environment isolation
* Clean folder structure
* Git-ready repository layout

---

## 🚀 Future Enhancements

* Page Object Model (POM)
* Cross-browser testing
* Headless execution
* Screenshots on failure
* CI/CD integration (GitHub Actions)

---

## 📌 Notes

* Do not commit `.venv` to Git
* Ensure Chrome browser is installed
* Keep Selenium and browser versions compatible

---

## 📜 License

This project is created for **learning and educational purposes**.

---

