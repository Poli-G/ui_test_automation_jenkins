import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.login_page import LoginPage

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