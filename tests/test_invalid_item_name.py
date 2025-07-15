import pytest
from pages.new_item_page import NewItemPage
from pages.dashboard_page import DashboardPage

@pytest.fixture
def test_item(logged_in_driver):
    driver = logged_in_driver
    item_page = NewItemPage(driver)
    valid_name = NewItemPage.generate_test_item_name()
    invalid_name = NewItemPage.generate_invalid_item_name()

    yield valid_name, invalid_name


@pytest.mark.tc_id("TC_02.001_10")
def test_invalid_item_name(logged_in_driver, test_item):
    valid_name, invalid_name = test_item
    driver = logged_in_driver
    item_page = NewItemPage(driver)
    item_page.open()

    item_page.enter_name(invalid_name)

    assert item_page.is_ok_button_disabled(), "OK button should be disabled for invalid item name"

    item_page.clear_name_field()
    item_page.enter_name(valid_name)

    assert item_page.is_ok_button_disabled(), "OK button should still be disabled until item type is selected"

    item_page.select_freestyle_project()

    assert not item_page.is_ok_button_disabled(), "OK button should be enabled after valid input and item type selection"