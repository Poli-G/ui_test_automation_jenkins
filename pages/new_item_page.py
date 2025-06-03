from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewItemPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.find_element(By.LINK_TEXT, "New Item").click()

    def enter_name(self, name):
        name_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "name"))
        )
        name_field.clear()
        name_field.send_keys(name)

    def select_freestyle_project(self):
        self.driver.find_element(
            By.XPATH, "//li[@class='hudson_model_FreeStyleProject']"
        ).click()

    def click_ok(self):
        self.driver.find_element(By.ID, "ok-button").click()

    def is_configure_page_loaded(self):
        try:
            self.wait.until(EC.url_contains("configure"))
            return True
        except:
            return False

    def is_general_section_visible(self):
        try:
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(., 'General') or contains(., 'Configure')]")
                )
            )
            return True
        except:
            return False

    def is_enter_item_name_visible(self):
        return "Enter an item name" in self.driver.page_source
