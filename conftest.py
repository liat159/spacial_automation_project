import pytest

from api.reqres_api import ReqResAPI
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# --- API Fixtures ---


@pytest.fixture(scope="session")
def api_context(playwright):

    browser = playwright.chromium.launch(headless=True)

    context = browser.new_context(
        base_url="https://jsonplaceholder.typicode.com",  # אופציונלי: הגדרת URL בסיס
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    api_request_context = context.request

    yield api_request_context

    # סגירה מסודרת
    context.close()
    browser.close()


@pytest.fixture
def reqres_api(api_context):
    return ReqResAPI(api_context)

# --- UI Fixtures ---


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)
