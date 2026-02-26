# Selenium Automation Framework  
### By Jose Sandoval

A scalable, production-style Selenium automation framework built with Python and Pytest.

This project demonstrates real-world automation engineering practices including:

- Page Object Model (POM) architecture
- Environment-based configuration (dev/prod)
- Parallel test execution
- Automatic test reruns
- HTML reporting
- GitHub Actions CI integration
- Clean, modular project structure

---

## Tech Stack

- Python 3.12
- Selenium
- Pytest
- pytest-xdist (parallel execution)
- pytest-rerunfailures
- pytest-html
- GitHub Actions (CI/CD)

---

## Project Structure

```
selenium_automation_project/
│
├── .github/workflows/
│ └── test.yml
│
├── reports/
│
├── src/
│ ├── config/
│ │ ├── __init__.py
│ │ └── settings.py
│ │
│ ├── pages/
│ │ ├── __init__.py
│ │ ├── login_page.py
│ │ └── secure_area_page.py
│ │
│ └── utils/
│ └── __init__.py
│
├── tests/
│ ├── conftest.py
│ ├── test_invalid_login.py
│ ├── test_logout.py
│ ├── test_login_real_world.py
│ └── test_secure_area_assertions.py
│
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Key Features

### Page Object Model (POM)
All UI interactions are abstracted into reusable page classes for maintainability and scalability.

### Environment Configuration
Supports environment switching using `.env.dev` and `.env.prod`.

Environment variables:
- BASE_URL
- HEADLESS
- ENV

### Parallel Execution
Tests run in parallel using pytest-xdist:

```
pytest -n auto
```

### Automatic Reruns
Failed tests automatically rerun once to reduce flakiness.

Configured in pytest.ini:
```
--reruns 1 --reruns-delay 2
```

### HTML Reporting
Generates a professional HTML test report:

```
pytest --html=reports/report.html --self-contained-html
```

Report location:
```
/reports/report.html
```

### Continuous Integration (CI)

GitHub Actions automatically:

- Installs dependencies
- Sets up Chrome
- Runs full test suite
- Fails build if tests fail

CI runs on every push to main.

---

## How To Run Locally

### Clone Repository

```
git clone https://github.com/je80sand/selenium_automation_project.git
cd selenium_automation_project
```

### Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```
pip install -r requirements.txt
```

### Run All Tests

```
pytest
```

### Run Tests in Parallel

```
pytest -n auto
```

### Run Smoke Tests Only

```
pytest -m smoke
```

---

## Example Output

```
5 passed in 17.79s
Generated html report: reports/report.html
```

---

## Real-World Test Coverage Includes

- Valid login flow
- Invalid login handling
- Logout validation
- Secure area access verification
- Assertion-heavy secure page validation

---

## Why This Project Matters

This framework mirrors how real QA Automation / SDET teams structure test automation:

- Modular architecture
- Environment-based configuration
- CI/CD integration
- Parallelization for speed
- Flakiness mitigation
- Reporting for stakeholders

It is designed to be production-ready, scalable, and extensible.

---

## Author

Jose Sandoval  
Python Automation Engineer (Aspiring)

---

## Future Enhancements

- Dockerized test execution
- Screenshot capture on failure
- Logging framework integration
- Test tagging strategy for pipelines
- Artifact upload of HTML reports in CI