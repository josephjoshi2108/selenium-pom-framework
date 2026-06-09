# selenium-pom-framework# Selenium POM Test Automation Framework

This project is a basic UI test automation framework built using Selenium WebDriver, Pytest, and the Page Object Model pattern in Python.

## Application Under Test

Website: https://www.saucedemo.com/

SauceDemo is a public demo e-commerce application used for automation practice.

## Tools Used

* Python
* Selenium WebDriver
* Pytest
* Page Object Model
* Google Chrome

## Project Structure

```
selenium-pom-framework/
│
├── pages/
│   ├── login_page.py
│   └── inventory_page.py
│
├── tests/
│   └── test_login.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

## Framework Design

The framework follows the Page Object Model pattern.

Each page has a separate class that stores:

* Locators
* Page actions
* Reusable methods

This makes the framework easy to read, reuse, and maintain.

## Test Cases

The framework includes three end-to-end test cases:

1. Valid login test
2. Invalid login error message test
3. Add item to cart test

## Setup Instructions

Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

## How to Run Tests

Run all tests using:

```
python -m pytest
```

If Anaconda base environment causes issues, run:

```
./venv/bin/python -m pytest
```

## Expected Result

```
3 passed
```

## Notes

Google Chrome should be installed on the machine before running the tests.
