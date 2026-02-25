# Selenium Automation Project

![Tests](https://github.com/je80sand/selenium_automation_project/actions/workflows/test.yml/badge.svg)

## Overview

This project demonstrates a production-style Selenium automation framework built using Python and Pytest. It follows automation engineering best practices including Page Object Model (POM), parallel execution, headless execution, HTML reporting, and CI pipeline integration.

The framework automates real-world login functionality using:

https://the-internet.herokuapp.com/login

This repository reflects how automation frameworks are structured in professional QA environments.

---

## Tech Stack

- Python 3.12+
- Selenium 4
- Pytest
- pytest-html
- pytest-xdist
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
│
├── .github/
│ └── workflows/
│ └── test.yml
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Features

- Valid login test
- Invalid login validation
- Logout test
- Page Object Model structure
- Fixture-based WebDriver setup
- Environment-aware execution (local + headless)
- Parallel test execution
- HTML report generation
- CI pipeline with artifact upload

---

# Run Locally

## 1. Create Virtual Environment

```bash
python -m venv .venv
```

## 2. Activate Environment

Mac/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

## Run Normally (Visible Browser)

```bash
pytest -v
```

## Run in Headless Mode

```bash
HEADLESS=1 pytest -v
```

---

# Parallel Execution (pytest-xdist)

Run tests in parallel (auto-detect CPU cores):

```bash
pytest -n auto --dist loadfile -v
```

Run parallel + headless (CI-style):

```bash
HEADLESS=1 pytest -n auto --dist loadfile -v
```

The `--dist loadfile` flag keeps test files grouped per worker for Selenium stability.

---

# Generate HTML Report

```bash
mkdir -p reports
HEADLESS=1 pytest -n auto --dist loadfile --html=reports/report.html --self-contained-html -v
```

Open report (Mac):

```bash
open reports/report.html
```

---

# CI Pipeline (GitHub Actions)

Every push to `main` automatically:

- Sets up Python
- Installs dependencies
- Installs Google Chrome
- Runs tests in headless mode
- Executes tests in parallel
- Generates HTML report
- Uploads report as downloadable artifact

To view CI results:

1. Go to GitHub
2. Click **Actions**
3. Open latest workflow run
4. Download the HTML report artifact

---

# Why This Project Matters

This project demonstrates:

- Automation framework architecture
- Real-world login validation
- Cross-environment execution (local + CI)
- Production-grade Chrome configuration
- Parallel test execution
- Clean separation of concerns using Page Object Model
- CI-first automation mindset

The goal was not just to automate a login test, but to demonstrate real-world automation engineering principles.

---

# Author

Jose Sandoval  
Python Automation | Selenium | QA Engineering