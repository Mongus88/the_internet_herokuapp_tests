from playwright.sync_api import expect, Page, Locator

from ui.pages.base_page import BasePage


class JavaScriptAlerts(BasePage):

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.javascript_alerts_url = base_url + "/javascript_alerts"
        self.js_alert_button: Locator = page.get_by_role("button", name="Click for JS Alert")
        self.js_confirm_button: Locator = page.get_by_role("button", name="Click for JS Confirm")
        self.js_prompt_button: Locator = page.get_by_role("button", name="Click for JS Prompt")
        self.result_text: Locator = page.locator("#result")

    def check_javascript_alerts(self):
        expect(self.page).to_have_url(self.javascript_alerts_url)

    def open_javascript_alerts(self):
        self.page.goto(self.javascript_alerts_url)
        self.check_javascript_alerts()

    def click_js_alert(self):
        self.js_alert_button.click()

    def click_js_confirm(self):
        self.js_confirm_button.click()

    def click_js_prompt(self):
        self.js_prompt_button.click()

    def setup_dialog_handler(self, expected_msg):
        def validate_and_close(dialog):
            assert dialog.message == expected_msg
            dialog.accept()
        self.page.once("dialog", validate_and_close)