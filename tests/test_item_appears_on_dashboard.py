import pytest
from pages.new_item_page import NewItemPage

@pytest.mark.tc_id("TC_02.001_08")
def test_item_appears_on_dashboard(logged_in_driver, duplicate_item_exists):
    item_page = NewItemPage(logged_in_driver)
    assert item_page.is_item_present_on_dashboard("duplicate_item"), "Item not found on Dashboard"






