from playwright.sync_api import expect

from ui.pages.javascript_alerts_page import JavaScriptAlerts


def test_js_alert(page, base_url):

    javascript_alerts_page = JavaScriptAlerts(page, base_url)
    javascript_alerts_page.open_javascript_alerts()

    def handle_dialog(dialog):
        assert dialog.message == "I am a JS Alert"
        dialog.accept()

    page.once("dialog", handle_dialog)

    javascript_alerts_page.click_js_alert()

    expect(javascript_alerts_page.result_text).to_have_text("You successfully clicked an alert")

def test_js_confirm(page, base_url):

    javascript_alerts_page = JavaScriptAlerts(page, base_url)
    javascript_alerts_page.open_javascript_alerts()

    def handle_dialog(dialog):
        assert dialog.message == "I am a JS Confirm"
        dialog.accept()

    page.once("dialog", handle_dialog)

    javascript_alerts_page.click_js_confirm()

    expect(javascript_alerts_page.result_text).to_have_text("You clicked: Ok")

def test_js_prompt(page, base_url):

    javascript_alerts_page = JavaScriptAlerts(page, base_url)
    javascript_alerts_page.open_javascript_alerts()

    text = "alma"

    def handle_dialog(dialog):
        assert dialog.message == "I am a JS prompt"

        dialog.accept(text)

    page.once("dialog", handle_dialog)

    javascript_alerts_page.click_js_prompt()

    expect(javascript_alerts_page.result_text).to_have_text(f"You entered: {text}")

