from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(By.NAME, "j_username").send_keys(username)
        self.driver.find_element(By.NAME, "j_password").send_keys(password)
        self.driver.find_element(By.NAME, "Submit").click()
