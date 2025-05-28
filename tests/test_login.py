import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()


def test_login(driver):
    url = os.getenv("JENKINS_URL")
    username = os.getenv("JENKINS_USERNAME")
    password = os.getenv("JENKINS_PASSWORD")

    login_page = LoginPage(driver)
    login_page.open(url)
    login_page.login(username, password)

    assert "Dashboard" in driver.title
