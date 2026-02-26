# Selenium Automation Framework

[![Selenium Automation CI](https://github.com/je80sand/selenium_automation_project/actions/workflows/test.yml/badge.svg)](https://github.com/je80sand/selenium_automation_project/actions/workflows/test.yml)
![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Pytest](https://img.shields.io/badge/Pytest-Automation-green)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**By Jose Sandoval**

A production-style Selenium automation framework built with **Python + Pytest**, featuring **Page Object Model (POM)** design, **environment-based configuration**, **parallel execution**, **automatic reruns for stability**, and **CI automation via GitHub Actions**.

---

## Highlights

- Page Object Model (POM) architecture  
- Clean, scalable project structure (`src/`, `tests/`)  
- Environment-based configuration (`dev` / `prod`)  
- Parallel execution with `pytest-xdist`  
- Automatic reruns with `pytest-rerunfailures`  
- HTML reporting with `pytest-html`  
- GitHub Actions CI integration  
- Automatic screenshots on failure  

---

## Project Structure

```
selenium_automation_project/
├─ .github/workflows/
│ └─ test.yml
├─ src/
│ ├─ config/
│ │ ├─ __init__.py
│ │ └─ settings.py
│ ├─ pages/
│ ├─ utils/
│ └─ __init__.py
├─ tests/
│ ├─ conftest.py
│ ├─ test_access_control.py
│ ├─ test_invalid_login.py
│ ├─ test_logout.py
│ └─ test_secure_area_assertions.py
├─ reports/
├─ pytest.ini
├─ requirements.txt
└─ README.md
```

---

## Requirements

- Python 3.12+
- Google Chrome
- Virtual environment recommended

---

## Quick Start

Clone the repository:

```
git clone https://github.com/je80sand/selenium_automation_project.git
cd selenium_automation_project
```

Create and activate virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run tests:

```
pytest
```

---

## Professional Test Runs

Run tests in parallel:

```
pytest -n auto --dist=loadfile
```

Run with automatic reruns:

```
pytest --reruns 1 --reruns-delay 2
```

Parallel + reruns (CI-style):

```
pytest -n auto --dist=loadfile --reruns 1 --reruns-delay 2
```

Generate HTML report:

```
pytest --html=reports/report.html --self-contained-html
```

---

## Markers

Run smoke tests only:

```
pytest -m smoke
```

---

## CI Pipeline

Workflow file:

```
.github/workflows/test.yml
```

On every push:
- Sets up Python
- Installs dependencies
- Installs Chrome
- Runs pytest (parallel + reruns)
- Fails build if tests fail

---

## What This Project Demonstrates

- Framework architecture design
- Scalable automation structure
- CI/CD implementation
- Parallel execution optimization
- Flaky test mitigation
- Reporting and debugging strategy
- Professional documentation standards

---

## Author

Jose Sandoval  
Automation / QA / Python

---

## License

MIT