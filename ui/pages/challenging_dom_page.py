from playwright.sync_api import expect, Page, Locator

from ui.pages.base_page import BasePage


class ChallengingDom(BasePage):

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.challenging_dom_url = base_url + "/challenging_dom"
        self.blue_button: Locator = page.locator(".large-2.columns a").nth(0)
        self.red_button: Locator = page.locator(".large-2.columns a").nth(1)
        self.green_button: Locator = page.locator(".large-2.columns a").nth(2)

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

    def read_red_button_id(self):
        return self.red_button.get_attribute("id")

    def read_green_button_css_class(self):
        return self.green_button.get_attribute("class")

    def monkey_patching(self):
        self.page.add_init_script("""
            window.__canvasNumber = "Nincs adat elcsípve";

        function intercept(text) {
            if (text && text.length > 0) {
                window.__canvasNumber = text;
            }
        }

        const origFill = CanvasRenderingContext2D.prototype.fillText;
        CanvasRenderingContext2D.prototype.fillText = function(text, ...args) {
            intercept(text);
            return origFill.call(this, text, ...args);
        };

        const origStroke = CanvasRenderingContext2D.prototype.strokeText;
        CanvasRenderingContext2D.prototype.strokeText = function(text, ...args) {
            intercept(text);
            return origStroke.call(this, text, ...args);
        };
    """)

    def initial_value(self):
        initial_value = self.page.evaluate("window.__canvasNumber")
        return initial_value

    def new_value(self):
        self.page.wait_for_load_state("networkidle")
        new_value = self.page.evaluate("window.__canvasNumber")
        return new_value