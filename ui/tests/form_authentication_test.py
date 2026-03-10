from playwright.sync_api import expect

from ui.pages.form_authentication_page import FormAuthenticationPage


def test_login(page, base_url):

    form_authentication_page = FormAuthenticationPage(page, base_url)
    form_authentication_page.open_form_authentication()
    form_authentication_page.fill_username("alma")
    form_authentication_page.fill_password("1234")
    form_authentication_page.click_login_button()

    expect(form_authentication_page.error_message).to_be_visible()
    expect(form_authentication_page.error_message).to_contain_text("Your username is invalid!")
    expect(form_authentication_page.error_message).to_have_class("flash error")