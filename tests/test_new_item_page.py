import pytest
from pages.new_item_page import NewItemPage


@pytest.mark.tc_id("TC_02_001_01")
def test_new_item_page_accessible(logged_in_driver, driver):
    driver = logged_in_driver
    item_page = NewItemPage(driver)

    item_page.open()
    assert item_page.is_enter_item_name_visible()
