import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.mark.tc_id("TC_02_001_01")
def test_new_item_page_accessible(logged_in_driver, driver):
    driver = logged_in_driver

    driver.find_element(By.LINK_TEXT, "New Item").click()
    assert "Enter an item name" in driver.page_source
