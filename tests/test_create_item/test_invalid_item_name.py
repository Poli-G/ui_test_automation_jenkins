import pytest


@pytest.mark.tc_id("TC_02.001_10")
@pytest.mark.parametrize("new_item_page_and_name", ["both"], indirect=True)
def test_invalid_item_name(new_item_page_and_name):
    item_page, valid_name, invalid_name = new_item_page_and_name

    assert item_page.is_ok_button_disabled(), "OK button should be disabled for invalid item name"

    item_page.clear_name_field()
    item_page.enter_name(valid_name)

    assert item_page.is_ok_button_disabled(), "OK button should still be disabled until item type is selected"

    item_page.select_freestyle_project()

    assert not item_page.is_ok_button_disabled(), ("OK button should be enabled after valid input and item type "
                                                   "selection")
