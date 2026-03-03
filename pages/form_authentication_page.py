from playwright.sync_api import expect, Page, Locator
from .base_page import BasePage

class FormAuthenticationPage(BasePage):

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.login_url = base_url + "/login"
        self.username_input: Locator = page.get_by_label("username")
        self.password_input: Locator = page.get_by_label("password")
        self.login_button = page.get_by_role("button", name="login")
        self.error_message: Locator = page.locator("#flash")

    def form_authentication_check(self):
        expect(self.page).to_have_url(self.login_url)

    def open_form_authentication(self):
        self.page.goto(self.login_url)
        self.form_authentication_check()

    def username_fill(self, keyword):
        self.username_input.fill(keyword)

    def password_fill(self, keyword):
        self.password_input.fill(keyword)

    def login_button_click(self):
        self.login_button.click()


