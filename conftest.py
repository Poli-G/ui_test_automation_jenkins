import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.login_page import LoginPage
from pages.new_item_page import NewItemPage
from pages.item_configuration_page import ItemConfigurationPage
import random
from pages.dashboard_page import DashboardPage

from selenium.webdriver.support import expected_conditions as EC


# Загрузка .env файла
load_dotenv()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, firefox, edge")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)

    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.open(os.getenv("JENKINS_URL"))
    login_page.login(
        os.getenv("JENKINS_USERNAME"),
        os.getenv("JENKINS_PASSWORD")
    )
    return driver


@pytest.fixture
def duplicate_item_exists(logged_in_driver):
    driver = logged_in_driver
    item_page = NewItemPage(logged_in_driver)
    item_page.open()
    duplicate_item_name = "duplicate_item"
    item_page.enter_name(duplicate_item_name)
    item_page.select_freestyle_project()
    item_page.click_ok()

    config_page = ItemConfigurationPage(driver)
    config_page.click_submit_button()
    driver.get("http://localhost:8080/")
    yield duplicate_item_name
    driver.get("http://localhost:8080/")
    DashboardPage(driver).delete_item(duplicate_item_name)

@pytest.fixture
def test_item(logged_in_driver):
    driver = logged_in_driver
    item_page = NewItemPage(driver)
    item_page.open()
    item_name = NewItemPage.generate_test_item_name()
    item_page.enter_name(item_name)
    item_page.select_freestyle_project()
    item_page.click_ok()

    config_page = ItemConfigurationPage(driver)
    config_page.click_submit_button()

    driver.get("http://localhost:8080/")
    yield item_name
    DashboardPage(driver).delete_item(item_name)

@pytest.fixture
def cleanup_item(logged_in_driver):
    driver = logged_in_driver
    items_to_delete = []

    yield items_to_delete  # test will fill this list

    config_page = ItemConfigurationPage(driver)
    config_page.click_submit_button()
    dashboard_page = DashboardPage(driver)

    driver.get("http://localhost:8080/")
    for item_name in items_to_delete:
        dashboard_page.delete_item(item_name)


