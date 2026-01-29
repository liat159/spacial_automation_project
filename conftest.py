import pytest
from playwright.sync_api import sync_playwright
from api.reqres_api import ReqResAPI
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# --- API Fixtures ---


@pytest.fixture(scope="session")
def api_context():
    with sync_playwright() as p:
        # Simple and clean context for standard APIs
        request_context = p.request.new_context()
        yield request_context
        request_context.dispose()


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
