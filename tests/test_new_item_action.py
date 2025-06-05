import pytest
import random
from pages.new_item_page import NewItemPage


@pytest.mark.tc_id("TC_02.001_02")
def test_create_new_freestyle_project(logged_in_driver):
    driver = logged_in_driver
    item_page = NewItemPage(driver)

    item_page.open()
    item_name = f"test_item_{random.randint(1000, 9999)}"
    item_page.enter_name(item_name)
    item_page.select_freestyle_project()
    item_page.click_ok()

    assert item_page.is_general_section_visible()
