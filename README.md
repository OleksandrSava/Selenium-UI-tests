# Selenium UI Tests

Compact Python Selenium UI test suite (pytest + Page Object Model) for automating E2E and smoke checks.

Quick start
1. git clone https://github.com/OleksandrSava/Selenium-UI-tests.git
2. cd Selenium-UI-tests
3. python -m venv .venv && source .venv/bin/activate
4. pip install -r requirements.txt
5. BASE_URL="https://staging.example.com" BROWSER=chrome HEADLESS=true pytest -q

Run with Docker
- docker-compose up --build
- or start a Selenium container: docker run -d -p 4444:4444 --shm-size=2g selenium/standalone-chrome:latest

Key env vars
- BASE_URL — application URL
- BROWSER — chrome|firefox (default: chrome)
- REMOTE_URL — remote WebDriver (optional)
- HEADLESS — true|false

Quick commands
- All tests: pytest
- Single file/folder: pytest tests/ui/
- Single test: pytest tests/ui/test_login.py::test_successful_login
- Parallel: pytest -n auto
- Allure report: pytest --alluredir=reports/allure

Project layout
- tests/ — test cases
- pages/ — Page Object classes
- fixtures/, utils/, reports/, requirements.txt, conftest.py

Notes
- Designed to run locally, in Docker, or in CI. Allure reporting and JUnit artifacts supported.
- License: MIT (add LICENSE file if missing)
