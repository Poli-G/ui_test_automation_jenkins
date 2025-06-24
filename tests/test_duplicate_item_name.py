import pytest
from pages.new_item_page import NewItemPage

@pytest.mark.tc_id("TC_02.001_06")
def test_duplicate_item_name(logged_in_driver, duplicate_item_exists):
    driver = logged_in_driver
    item_page = NewItemPage(driver)

    item_page.open()
    item_page.enter_name("duplicate_item")

    error_text = item_page.error_message_text()

    assert error_text is not None
    assert "A job already exists with the name" in error_text
    assert item_page.is_ok_button_disabled()
