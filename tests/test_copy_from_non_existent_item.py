import pytest
from pages.new_item_page import NewItemPage

@pytest.fixture
def item_name():
    return "test"


@pytest.mark.tc_id("TC_02.001_09")
def test_copy_from_non_existent_item(logged_in_driver, item_name):
    driver = logged_in_driver
    item_page = NewItemPage(driver)
    item_page.open()
    item_page.enter_name(item_name)
    item_page.enter_copy_from_name("non_existent")
    item_page.click_ok()

    assert item_page.copy_from_error_is_displayed(), "Error 'No such job' is not displayed"

    item_page.dashboard()

    assert not item_page.is_item_present_on_dashboard(item_name), f"Item '{item_name}' should NOT be on dashboard"

