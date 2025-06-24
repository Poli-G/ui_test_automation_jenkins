import pytest
from pages.new_item_page import NewItemPage


@pytest.mark.tc_id("TC_02.001_04")
def test_create_item_negative(logged_in_driver):
    driver = logged_in_driver
    item_page = NewItemPage(driver)

    item_page.open()
    item_page.enter_name("test@job!")

    assert item_page.error_message_is_displayed, "Expected error message to be displayed for invalid item name"
    assert item_page.is_ok_button_disabled(), "Expected OK button to be disabled for invalid item name"

