import pytest
from playwright.sync_api import sync_playwright

#Login URL of the OrangeHRM demo site
BASE_URL="https://opensource-demo.orangehrmlive.com/"

#Custom fixture for browser.
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        yield browser
        browser.close()

#Custom fixture for page.
@pytest.fixture(scope="module")   #Scope is set as module so as to reuse the page for multipl tests on the same page
def page(browser):
    context = browser.new_context(base_url=BASE_URL)
    page=context.new_page()
    yield page
    context.close()