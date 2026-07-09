from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.leave_page import LeavePage
import pytest

@pytest.fixture(scope="module",autouse=True)
def test_suite_setup(page):
    page.goto("/web/index.php/auth/login")
    login_page=LoginPage(page)
    login_page.login("Admin","admin123")
    page.wait_for_timeout(3000)  # wait 3 seconds
    assert login_page.is_login_success()

def test_leave_search(page):
    """ Verify that the user can search for leave requests with status and leave type """
    leave_page = LeavePage(page)
    leave_page.page_goto()
    leave_page.check_pending_leave_request("CAN - FMLA", "Taken","Cancelled")
    page.wait_for_timeout(3000)  # wait 3 seconds
    expect(leave_page.search_results).to_be_visible()