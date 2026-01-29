# QA Automation Assignment

This repository contains UI and API automation tests using Python and Playwright.

## Prerequisites
* Python 3.8+
* pip

## Installation
1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Install Playwright browsers:
    ```bash
    playwright install chromium
    ```

## How to Run
### Run All Tests
```bash
pytest

Run Only UI Tests
Bash
pytest -m ui
Run Only API Tests
Bash
pytest -m api
Reporting
To generate and view the HTML report (including screenshots on failure):

Bash
pytest --html=report.html
Open report.html in any browser to view results.