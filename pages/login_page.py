from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page:Page):
        self.page=page
        self.username=page.get_by_role("textbox",name="Username")
        self.password=page.get_by_role("textbox", name="Password")
        self.login_button=page.get_by_role("button", name="Login")

    @property
    def orange_logo(self):
        return self.page.locator('img[alt="client brand banner"]')
    
    @property
    def dashboard(self):
        return self.page.get_by_role("heading", name="Dashboard")


#-----------------------------------Actions--------------------------------------
    def login(self,username,password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

#----------------------------State Checks------------------------------------------
    def is_login_success(self):
        return self.orange_logo.is_visible() and self.dashboard.is_visible()