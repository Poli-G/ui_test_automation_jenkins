import pytest
from pages.item_configuration_page import ItemConfigurationPage
from pages.new_item_page import NewItemPage


@pytest.mark.tc_id("TC_02_001_03")
def test_create_item_name_accepted(logged_in_driver, cleanup_item):
    driver = logged_in_driver
    item_page = NewItemPage(driver)
    item_page.open()

    item_name = item_page.generate_test_item_name()
    item_page.enter_name(item_name)
    item_page.select_freestyle_project()
    item_page.click_ok()

    config_page = ItemConfigurationPage(driver)
    config_page.wait_until_general_section_visible()
    assert config_page.is_general_section_visible()

    cleanup_item.append(item_name)