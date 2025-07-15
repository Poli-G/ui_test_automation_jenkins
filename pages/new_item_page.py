from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from locators.locators import NewItemPageLocators, DashboardPageLocators
import random


class NewItemPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_new_item_page_to_load(self):
        self.wait.until(
            EC.presence_of_element_located(NewItemPageLocators.NEW_ITEM_HEADER),
            message="New Item page did not load"
        )

    def open(self):
        self.driver.get("http://localhost:8080/newJob")
        self.wait_for_new_item_page_to_load()

    def dashboard(self):
        self.driver.get("http://localhost:8080")

    def createItempage(self):
        self.driver.get(("http://localhost:8080/view/all/createItem")
                        )

    @staticmethod
    def generate_test_item_name(prefix="test_item"):
        return f"{prefix}_{random.randint(1000, 9999)}"

    @staticmethod
    def generate_invalid_item_name():
        return "invalid_name!"

    def clear_name_field(self):
        name_field = self.wait.until(
            EC.presence_of_element_located(NewItemPageLocators.ITEM_NAME_FIELD)
        )
        name_field.clear()

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
        ok_button = self.wait.until(
            EC.element_to_be_clickable(NewItemPageLocators.OK_BUTTON)
        )
        ok_button.click()

    def is_configure_page_loaded(self):
        try:
            self.wait.until(EC.url_contains("configure"))
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
                EC.presence_of_element_located(NewItemPageLocators.OK_BUTTON)
            )
            return button.get_attribute("disabled") is not None
        except TimeoutException:
            return False

    def error_message_text(self):
        error = self.wait.until(
            EC.visibility_of_element_located(NewItemPageLocators.ITEM_NAME_DUPLICATE_ERROR_MESSAGE)
        )
        return error.text.strip()

    def is_item_present_on_dashboard(self, item_name):
        try:
            item_locator = DashboardPageLocators.ITEM_LINK(item_name)
            return self.driver.find_element(*item_locator).is_displayed()
        except NoSuchElementException:
            return False

    def enter_copy_from_name(self, name):
        copy_from_field = self.wait.until(
            EC.presence_of_element_located(NewItemPageLocators.COPY_FROM_FIELD)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", copy_from_field)

        copy_from_field.clear()
        if name:
            copy_from_field.send_keys(name)

    def copy_from_error_is_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(NewItemPageLocators.COPY_FROM_ERROR_MESSAGE)
            )
            return True
        except TimeoutException:
            return False
