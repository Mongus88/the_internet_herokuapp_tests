from playwright.sync_api import expect

from ui.pages.dynamic_loaded_page import DynamicallyLoaded


def test_dynamic_loaded(page, base_url):

    dynamic_loaded_page = DynamicallyLoaded(page, base_url)
    dynamic_loaded_page.open_dynamic_loading()
    dynamic_loaded_page.start_button.click()

    expect(dynamic_loaded_page.text_1).to_be_visible(timeout=10_000)
    expect(dynamic_loaded_page.text_1).to_have_text("Hello World!")