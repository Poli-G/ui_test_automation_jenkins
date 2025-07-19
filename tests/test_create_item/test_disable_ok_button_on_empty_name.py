import pytest


@pytest.mark.tc_id("TC_02.001_05")
@pytest.mark.parametrize("new_item_page_and_name", ["empty"], indirect=True)
def test_disable_ok_button_on_empty_name(new_item_page_and_name):
    item_page, _ = new_item_page_and_name
    assert item_page.is_ok_button_disabled(), "Expected OK button to be disabled when name is empty"

