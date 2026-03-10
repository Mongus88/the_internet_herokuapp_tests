from playwright.sync_api import expect, Page, Locator
from ui.pages.base_page import BasePage

class DynamicallyLoaded(BasePage):

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.dynamic_loading_1_url = base_url + "/dynamic_loading/1"
        self.start_button: Locator = page.get_by_role("button", name="Start")
        self.text_1: Locator = page.locator("#finish")

    def check_dynamic_loading(self):
        expect(self.page).to_have_url(self.dynamic_loading_1_url)

    def open_dynamic_loading(self):
        self.page.goto(self.dynamic_loading_1_url)
        self.check_dynamic_loading()

    def start_button_click(self):
        self.start_button.click()