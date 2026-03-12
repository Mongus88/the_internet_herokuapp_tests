import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="session")
def base_url():
    return "https://the-internet.herokuapp.com/"

@pytest.fixture
def navigate_to(page: Page, base_url):
    def _navigate(path: str):
        page.goto(f"{base_url}{path}")
    return _navigate