import pytest
from pages.dashboard_page import DashboardPage

@pytest.mark.tc_id("TC_02.001_02")
def test_create_new_freestyle_project(logged_in_driver, test_item):
    driver = logged_in_driver
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_item_present(test_item)

