from playwright.sync_api import Page, expect
from pages.directory_page import DirectoryPage
from pages.login_page import LoginPage
import pytest

#-----------------------Test Cases-----------------------------------------------
#Fixture for login. Runs initially before executing the tests. The fixture is set to autouse so that it runs automatically for all tests in the module.
@pytest.fixture(scope="module",autouse=True)
def suite_setup(page):
    page.goto("/web/index.php/auth/login")
    login_page=LoginPage(page)
    login_page.login("Admin", "admin123")
    page.wait_for_timeout(3000)  # wait 3 seconds
    assert login_page.is_login_success()
    yield

#Fixture for directory page. Navigates to the directory page and returns the DirectoryPage object for use in tests.
@pytest.fixture(scope="module")
def directory_page(page):
    page.goto(DirectoryPage.URL)
    directory_page=DirectoryPage(page)
    yield directory_page

def test_employee_count_in_directory(directory_page: DirectoryPage):
    """ Verify that the number of employee cards displayed in the directory matches the number of records shown on the page """
    directory_page.wait_for_page_load()
    assert directory_page.get_employee_count() >= directory_page.get_num_of_records()

def test_open_employee_card(directory_page: DirectoryPage):
    """ Verify that clicking on an employee card opens the employee's profile and displays the sidebar """
    directory_page.wait_for_page_load()
    directory_page.open_employee_card()
    expect(directory_page.side_bar).to_be_visible()