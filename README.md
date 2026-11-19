# Beginner Selenium + Python + PyTest Project

This is a simple beginner project. It automates two login test cases on the public demo website https://www.saucedemo.com/.

## What it tests
1. Valid login: checks that the Products page appears.
2. Invalid login: checks that an error message appears.

Demo username: `standard_user`
Demo password: `secret_sauce`

These are public demo credentials. Do not use personal credentials.

## What you need
- Python 3.10 or newer
- Google Chrome
- Internet connection

## Install and run (Windows)

Open this folder in VS Code or PyCharm. In the terminal, run:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

Selenium 4 normally manages the Chrome driver automatically using Selenium Manager.

## Folder structure

```text
beginner_selenium_pytest_project/
├── pages/
│   └── login_page.py
├── tests/
│   └── test_login.py
├── conftest.py
└── requirements.txt
```

## Beginner concepts used
- `webdriver.Chrome()` opens Chrome.
- `find_element()` locates an element.
- `send_keys()` enters text.
- `click()` clicks a button.
- `assert` checks the expected result.
- A PyTest fixture starts and closes the browser.
- `LoginPage` is a simple example of Page Object Model (POM).

## Learn in this order
1. Run the tests and observe what happens.
2. Read `conftest.py` and understand `yield`.
3. Read `login_page.py` and understand each method.
4. Read `test_login.py` and understand each assertion.
5. Add one more test yourself, such as checking the page title.

This is a learning project, not an advanced production framework. After understanding it, you can add explicit waits, more pages, cart tests and reports.
