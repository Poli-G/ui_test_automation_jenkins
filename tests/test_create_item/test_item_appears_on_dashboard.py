import pytest
from pages.new_item_page import NewItemPage


@pytest.mark.tc_id("TC_02.001_08")
def test_item_appears_on_dashboard(new_item_page_and_name):
    item_page, item_name = new_item_page_and_name

    assert item_page.is_item_present_on_dashboard(item_name), "Item not found on Dashboard"
