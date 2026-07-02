from playwright.sync_api import Page
import re
class DirectoryPage:
    URL = "/web/index.php/directory/viewDirectory"
    
    def __init__(self, page:Page):
        self.page=page
        self.employee_cards=page.locator(".oxd-grid-item.oxd-grid-item--gutters")
        self.employees=page.locator(".orangehrm-horizontal-padding")
        self.employees_profile_pic=self.page.locator(".orangehrm-profile-picture-img")

    @property
    def side_bar(self):
        return self.page.locator(".orangehrm-corporate-directory-sidebar")

#-----------------------------------Actions--------------------------------------
    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")

    def scroll_to_bottom(self) -> None:
        #Method to scroll the inner container to the bottom until all employee cards are loaded
        scroll_container = self.page.locator(".orangehrm-container")
        
        previous_count = 0
        while True:
            # Scroll the inner container to its bottom
            scroll_container.evaluate("el => el.scrollTo(0, el.scrollHeight)")
            self.page.wait_for_timeout(1000) # wait to allow new cards to load
            
            current_count = self.employee_cards.count()
            if current_count == previous_count:
                break
            previous_count = current_count
    
    def get_employee_count(self):
        self.scroll_to_bottom()
        return self.employee_cards.count()
        
    def get_num_of_records(self):
        text=self.employees.inner_text()
        match = re.search(r'\d+', text)
        return int(match.group()) if match else 0
    
    def open_employee_card(self):
        self.employees_profile_pic.first.click()


#-----------------------State Check-------------------------------------------------------------



    