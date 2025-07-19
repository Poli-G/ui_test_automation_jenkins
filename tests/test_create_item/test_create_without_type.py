import pytest


@pytest.mark.tc_id("TC_02.001_07")
def test_create_without_type(new_item_page_and_name):
    item_page, _ = new_item_page_and_name

    assert item_page.is_ok_button_disabled, "Expected OK button to be disabled for invalid item name"
