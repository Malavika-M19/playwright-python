from playwright.sync_api import Page

class LeavePage:
    URL= "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList"
    
    def __init__(self,page):
        self.page=page
        self.leave_list=page.get_by_role("listitem").filter(has_text="Leave List")
        self.leave_type_select=page.locator(".oxd-select-text-input")
        self.leave_type_can=["CAN Breavement", "CAN - FMLA", "CAN - Personal", "CAN - Matternity","CAN - Vacation" ]
        self.leave_type_us=["US Breavement", "US - FMLA", "US - Personal", "US - Matternity","US - Vacation" ]
        self.leave_type_selector=page.locator(".oxd-select-wrapper > .oxd-select-text > .oxd-select-text--after > .oxd-icon").first
        self.show_leave_with_status_selector=page.locator(".oxd-icon.bi-caret-down-fill.oxd-select-text--arrow").first
        self.leave_status=["Pending Approval", "Scheduled", "Taken","Cancelled"]
        self.search_leaves=page.get_by_text(" Search ")

    @property
    def search_results(self):
        return self.page.locator(".orangehrm-container")



#----------------------Actions---------------------------------------------------------------
    def page_goto(self):
        self.page.goto(self.URL)

    def check_pending_leave_request(self,leave_type, *status):
        #Status is multiselect and leave type is single select. This method will check if the leave type and status are valid and then select them and click search
        if leave_type not in self.leave_type_can and leave_type not in self.leave_type_us:
            raise ValueError(f"Invalid leave type: {leave_type}. Valid options are: {self.leave_type_can + self.leave_type_us}")
        if leave_type in self.leave_type_can:
            if all(s in self.leave_status for s in status):
                for s in status:
                    self.show_leave_with_status_selector.click()
                    self.page.get_by_role("option", name=s).click()
                self.leave_type_selector.click()
                self.leave_type_can=self.page.get_by_role("option", name=leave_type)
                self.leave_type_can.click()
                self.search_leaves.click()
            if leave_type in self.leave_type_us:
                if all(s in self.leave_status for s in status):
                    for s in status:
                        self.show_leave_with_status_selector.click()
                        self.page.get_by_role("option", name=s).click()
                    self.leave_type_selector.click()
                    self.leave_type_us=self.page.get_by_role("option", name=leave_type)
                    self.leave_type_us.click()
                    self.search_leaves.click()