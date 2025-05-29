import pytest
from dotenv import load_dotenv
load_dotenv()
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage


load_dotenv()


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    login_page = LoginPage(driver)
    login_page.open(os.getenv("JENKINS_URL"))
    login_page.login(
        os.getenv("JENKINS_USERNAME"),
        os.getenv("JENKINS_PASSWORD")
    )

    yield driver
    driver.quit()
