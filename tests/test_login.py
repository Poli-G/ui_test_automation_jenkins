import os

import pytest
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()


@pytest.mark.tc_id("TC_01.001_01")
def test_login(driver):
    url = os.getenv("JENKINS_URL")
    username = os.getenv("JENKINS_USERNAME")
    password = os.getenv("JENKINS_PASSWORD")

    login_page = LoginPage(driver)
    login_page.open(url)
    login_page.login(username, password)

    assert "Dashboard" in driver.title
