from playwright.sync_api import expect, Page, Locator

from ui.pages.base_page import BasePage


class ChallengingDom(BasePage):

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.challenging_dom_url = base_url + "/challenging_dom"
        self.blue_button: Locator = page.locator("a.button")
        self.red_button: Locator = page.locator("a.button alert")
        self.green_button: Locator = page.locator("a.button success")

    def check_challenging_dom(self):
        expect(self.page).to_have_url(self.challenging_dom_url)

    def open_challenging_dom(self):
        self.page.goto(self.challenging_dom_url)
        self.check_challenging_dom()

    def click_blue_button(self):
        self.blue_button.click()

    def click_red_button(self):
        self.red_button.click()

    def click_green_button(self):
        self.green_button.click()