import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import random

load_dotenv()


@pytest.mark.tc_id("TC_02.001_02")
def test_create_new_freestyle_project(logged_in_driver):
    driver = logged_in_driver

    driver.find_element(By.LINK_TEXT, "New Item").click()
    item_name = f"test_item_{random.randint(1000, 9999)}"
    driver.find_element(By.ID, "name").send_keys(item_name)
    driver.find_element(By.XPATH, "//span[contains(text(), 'Freestyle project')]").click()
    driver.find_element(By.ID, "ok-button").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(., 'General') or contains(., 'Configure')]"))
    )
    assert "Configure" in driver.page_source or "General" in driver.page_source
