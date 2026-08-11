import pytest
from pages.login_page import LoginPage

#Login URL of the OrangeHRM demo site
BASE_URL="https://opensource-demo.orangehrmlive.com/"

#Custom fixture for browser.
@pytest.fixture(scope="session")
def browser(playwright):
    browser=playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

#Custom fixture for page.
@pytest.fixture(scope="module")   #Scope is set as module so as to reuse the page for multipl tests on the same page
def page(browser):
    context = browser.new_context(base_url=BASE_URL)
    page=context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def authenticated_state(browser):
    context = browser.new_context(base_url=BASE_URL)
    page = context.new_page()
    page.goto("/web/index.php/auth/login")
    login_page = LoginPage(page)
    login_page.login("Admin", "admin123")
    page.wait_for_url("**/dashboard/index")
  
    state = context.storage_state()  # captures cookies
    context.close()
    return state

@pytest.fixture(scope="session")
def api_request_context(playwright, authenticated_state):
    request_context = playwright.request.new_context(
        base_url="https://opensource-demo.orangehrmlive.com",
        storage_state=authenticated_state,
    )
    yield request_context
    request_context.dispose()

@pytest.fixture(scope="session")
def candidate_client(api_request_context):
    from api.candidate_client import CandidateClient
    return CandidateClient(api_request_context)