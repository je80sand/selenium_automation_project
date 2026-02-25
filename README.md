[![Tests](https://github.com/je80sand/selenium_automation_project/actions/workflows/test.yml/badge.svg)](https://github.com/je80sand/selenium_automation_project/actions/workflows/test.yml)

# Selenium Automation Project

## Overview

This project demonstrates a production-style Selenium automation framework using:

- Python
- Pytest
- Page Object Model (POM)
- Headless execution
- HTML test reporting
- GitHub Actions CI

The framework automates real-world login functionality using:
https://the-internet.herokuapp.com/login

---

## Tech Stack

- Python 3.12+
- Selenium 4
- Pytest
- pytest-html
- WebDriver Manager
- GitHub Actions

---

## Framework Architecture

```
selenium_automation_project/
│
├── src/
│ └── pages/
│ └── login_page.py
│
├── tests/
│ ├── test_invalid_login.py
│ ├── test_login_real_world.py
│ └── test_logout.py
│
├── reports/
├── .github/workflows/test.yml
├── requirements.txt
└── pytest.ini
```

---

## Features

- Valid login test
- Invalid login test
- Logout test
- Headless browser execution
- HTML test report generation
- Continuous Integration via GitHub Actions
- Stable Chrome configuration for CI environments

---

## Run Locally

### 1️⃣ Create virtual environment

```bash
python -m venv .venv
```

### 2️⃣ Activate environment

Mac/Linux:
```bash
source .venv/bin/activate
```

Windows:
```bash
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run tests (visible browser)

```bash
pytest -v
```

### 5️⃣ Run tests (headless mode)

```bash
HEADLESS=1 pytest -v
```

### 6️⃣ Generate HTML report

```bash
mkdir -p reports
HEADLESS=1 pytest --html=reports/report.html --self-contained-html
```

Open the report (Mac):

```bash
open reports/report.html
```

---

## CI Pipeline

Every push to `main` automatically:

- Sets up Python
- Installs dependencies
- Installs Google Chrome
- Runs tests in headless mode
- Generates HTML report
- Uploads report artifact

---

## Why This Project Matters

This project demonstrates:

- Automation framework architecture
- Real-world login validation
- Cross-environment execution (local + CI)
- Production-grade Chrome stability configuration
- Clean separation of concerns using Page Object Model

---

## Author

Jose Sandoval  
Python Automation | Selenium | QA Engineering