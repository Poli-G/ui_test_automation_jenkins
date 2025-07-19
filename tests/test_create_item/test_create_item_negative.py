import pytest
from pages.new_item_page import NewItemPage


@pytest.mark.tc_id("TC_02.001_04")
@pytest.mark.parametrize("new_item_page_and_name", ["invalid"], indirect=True)
def test_create_item_negative(new_item_page_and_name):
    item_page, invalid_name = new_item_page_and_name

    assert item_page.error_message_is_displayed, "Expected error message to be displayed for invalid item name"
    assert item_page.is_ok_button_disabled(), "Expected OK button to be disabled for invalid item name"


