from playwright.sync_api import Page,expect
from pages.login_page import LoginPage

#---------------------------------------Testcases----------------------------------------------------------
def test_login(page):
    """Verify user is able to login successfully"""
    page.goto("/web/index.php/auth/login")
    login_page=LoginPage(page)
    login_page.login("Admin", "admin123")
    page.wait_for_timeout(3000)  # wait 3 seconds
    assert login_page.is_login_success()