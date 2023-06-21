import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(autouse=True)
def playwright():
    with sync_playwright() as playwright:
        yield playwright
