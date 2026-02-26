# Selenium Automation Framework (Python + Pytest + POM)

![CI](https://github.com/je80sand/selenium_automation_project/actions/workflows/test.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pytest](https://img.shields.io/badge/Pytest-Framework-brightgreen)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-orange)
![Parallel](https://img.shields.io/badge/Execution-Parallel-blueviolet)

A production-style Selenium automation framework built using **Python, Pytest, and Page Object Model (POM)** architecture.

This project demonstrates real-world automation structure including:

- Explicit waits for stability  
- Assertion-heavy validation  
- Access control testing  
- Parallel test execution  
- GitHub Actions CI integration  
- HTML reporting artifacts  

---

## 🚀 Tech Stack

- Python 3.12  
- Selenium WebDriver  
- Pytest  
- pytest-xdist (parallel execution)  
- pytest-html (report generation)  
- GitHub Actions (CI/CD)  

---

## 📂 Project Structure

```
selenium_automation_project/
├── src/
│ └── pages/
│ ├── login_page.py
│ └── secure_page.py
├── tests/
│ ├── test_invalid_login.py
│ ├── test_login_real_world.py
│ ├── test_logout.py
│ ├── test_access_control.py
│ └── test_secure_area_assertions.py
├── reports/
├── pytest.ini
└── README.md
```

---

## ▶️ Run Tests Locally

Activate virtual environment:

```
source venv/bin/activate
```

Run all tests:

```
pytest -v
```

Run in parallel:

```
pytest -n auto -v
```

Generate local HTML report:

```
pytest --html=reports/report.html --self-contained-html
```

---

## ✅ What Is Validated

✔ Invalid login shows correct error message  
✔ Valid login redirects to `/secure`  
✔ Secure page header + flash message verified  
✔ Logout redirects back to login page  
✔ Direct access to `/secure` without login is blocked  
✔ Logout confirmation message verified  

---

## 🟢 Continuous Integration

Every push to `main` automatically:

- Installs dependencies  
- Runs tests headless  
- Runs tests in parallel  
- Uploads HTML test report as artifact  

View CI runs:  
GitHub → Repository → Actions tab  

---

## 📌 Resume Bullet

Built a production-style Selenium automation framework using Python and Pytest with Page Object Model architecture, explicit waits, CI automation via GitHub Actions, parallel test execution, and HTML reporting artifacts.