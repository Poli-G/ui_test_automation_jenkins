from logging import error

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import NewItemPageLocators
from selenium.common.exceptions import TimeoutException



class NewItemPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost:8080/view/all/newJob")

    def dashboard(self):
        self.driver.get("http://localhost:8080")

    def enter_name(self, name):
        name_field = self.wait.until(
            EC.presence_of_element_located(NewItemPageLocators.ITEM_NAME_FIELD)
        )
        name_field.clear()
        if name:
            name_field.send_keys(name)

    def select_freestyle_project(self):
        self.driver.find_element(*NewItemPageLocators.FREESTYLE_PROJECT_OPTION).click()

    def click_ok(self):
        self.driver.find_element(*NewItemPageLocators.OK_BUTTON).click()

    def is_configure_page_loaded(self):
        try:
            self.wait.until(EC.url_contains("configure"))
            return True
        except:
            return False

    def is_general_section_visible(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(NewItemPageLocators.CONFIGURE_HEADER)
            )
            return True
        except:
            return False

    def is_enter_item_name_visible(self):
        return "Enter an item name" in self.driver.page_source

    @property
    def error_message_is_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(NewItemPageLocators.ITEM_NAME_ERROR_MESSAGE)
            )
            return True
        except:
            return False

    def is_ok_button_disabled(self):
        try:
            button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located (NewItemPageLocators.OK_BUTTON)
            )
            return button.get_attribute("disabled") is not None
        except TimeoutException:
            return False

    def error_message_text(self):
        error = self.wait.until(
            EC.visibility_of_element_located(NewItemPageLocators.ITEM_NAME_DUPLICATE_ERROR_MESSAGE)
        )
        return error.text.strip()










