import pytest
from pages.new_item_page import NewItemPage


@pytest.mark.tc_id("TC_02_001_03")
def test_create_item_name_accepted(logged_in_driver):
    driver = logged_in_driver
    item_page = NewItemPage(driver)

    item_page.open()
    item_page.enter_name("project_123")
    item_page.select_freestyle_project()
    item_page.click_ok()

    assert item_page.is_configure_page_loaded()
