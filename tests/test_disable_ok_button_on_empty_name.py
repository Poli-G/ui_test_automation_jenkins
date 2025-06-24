import pytest
from pages.new_item_page import NewItemPage


@pytest.mark.tc_id("TC_02.001_05")
def test_disable_ok_button_on_empty_name(logged_in_driver, driver):
    driver = logged_in_driver
    item_page = NewItemPage(driver)

    item_page.open()
    item_page.enter_name("")
    assert item_page.is_ok_button_disabled(), "Expected OK button to be disabled when name is empty"