import pytest


@pytest.mark.tc_id("TC_02.001_09")
def test_copy_from_non_existent_item(new_item_page_and_name):
    item_page, item_name = new_item_page_and_name
    item_page.copy_from("non_existent")

    assert item_page.copy_from_error_is_displayed(), "Error 'No such job' is not displayed"

    dashboard_page = item_page.dashboard()

    assert not dashboard_page.is_item_present(item_name), f"Item '{item_name}' should NOT be on dashboard"

