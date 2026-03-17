import pytest
from playwright.sync_api import expect

from ui.pages.challenging_dom_page import ChallengingDom


def test_blue_button_click(page, base_url):

    challenging_dom_page = ChallengingDom(page, base_url)
    challenging_dom_page.monkey_patching()
    challenging_dom_page.open_challenging_dom()
    initial_value = challenging_dom_page.initial_value()
    challenging_dom_page.click_blue_button()
    new_value = challenging_dom_page.new_value()

    assert(initial_value != new_value)

def test_red_button_id_refresh(page, base_url):
    challenging_dom_page = ChallengingDom(page, base_url)
    challenging_dom_page.open_challenging_dom()
    initial_red_button_id = challenging_dom_page.read_red_button_id()
    challenging_dom_page.click_red_button()
    new_red_button_id = challenging_dom_page.read_red_button_id()

    assert(initial_red_button_id != new_red_button_id)

def test_green_button_css_class(page, base_url):
    challenging_dom_page = ChallengingDom(page, base_url)
    challenging_dom_page.open_challenging_dom()

    assert(challenging_dom_page.read_green_button_css_class() == "button success")

