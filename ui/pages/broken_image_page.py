from playwright.sync_api import expect, Page, Locator
from ui.pages.base_page import BasePage

class BrokenImagePage(BasePage):


    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.broken_image_url = base_url + "/broken_images"
        self.all_images: Locator = page.locator("img")

    def check_broken_image(self):
        expect(self.page).to_have_url(self.broken_image_url)

    def open_broken_image(self):
        self.page.goto(self.broken_image_url)
        self.check_broken_image()

    def broken_image_count(self) -> int:
        broken_count = 0
        images = self.all_images.all()

        for img in images:
            is_broken = img.evaluate("node => node.naturalWidth === 0")
            if is_broken:
                broken_count += 1

        return broken_count
