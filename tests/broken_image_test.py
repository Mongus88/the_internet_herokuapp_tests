from playwright.sync_api import expect

from pages.broken_image_page import BrokenImagePage


def test_check_broken_image(page, base_url):

    broken_image_page = BrokenImagePage(page, base_url)
    broken_image_page.open_broken_image()
    found_broken_image = broken_image_page.broken_image_count()

    expect(broken_image_page.all_images.first).to_be_visible()
    assert found_broken_image == 0, f"Találtam {found_broken_image} törött képet az oldalon!"