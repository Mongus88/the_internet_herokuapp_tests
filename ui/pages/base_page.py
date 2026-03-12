from playwright.sync_api import expect, Page


class BasePage:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def base_page_check(self):
        expect(self.page).to_have_url(self.base_url)

    def open_base_page(self):
        self.page.goto(self.base_url)
        self.base_page_check()