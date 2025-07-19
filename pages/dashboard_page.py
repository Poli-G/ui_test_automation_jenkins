import locators.locators
from locators.locators import ItemPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_item_present(self, item_name):
        locator = ItemPageLocators.ITEM_ROW_BY_NAME
        formatted_locator = (locator[0], locator[1].format(item_name=item_name))
        try:
            self.wait.until(EC.presence_of_element_located(formatted_locator))
            return True
        except:
            return False

    def delete_item(self, item_name):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        item_locator = (
            locators.locators.ItemPageLocators.ITEM_ROW_BY_NAME[0],
            locators.locators.ItemPageLocators.ITEM_ROW_BY_NAME[1].format(item_name=item_name)
        )

        try:
            item_element = wait.until(EC.presence_of_element_located(item_locator))
            ActionChains(driver).move_to_element(item_element).perform()

            arrow_locator = (locators.locators.ItemPageLocators.ITEM_DROPDOWN_BUTTON[0], locators.locators.ItemPageLocators.ITEM_DROPDOWN_BUTTON[1].format(item_name=item_name))
            arrow_element = wait.until(EC.element_to_be_clickable(arrow_locator))

            arrow_element.click()
            delete_item_locator = (locators.locators.ItemPageLocators.ITEM_DELETE_OPTION[0], locators.locators.ItemPageLocators.ITEM_DELETE_OPTION[1].format(item_name=item_name))

            delete_element = wait.until(EC.element_to_be_clickable(delete_item_locator))
            delete_element.click()

            confirm_button_locator = locators.locators.ItemPageLocators.ITEM_CONFIRM_DELETE_BUTTON
            confirm_button = wait.until(EC.element_to_be_clickable(confirm_button_locator))
            confirm_button.click()

            print(f"Item '{item_name}' deleted successfully")

        except Exception as e:
            print(f"Error deleting item '{item_name}': {e}")
            driver.save_screenshot(f"delete_error_{item_name}.png")
            raise

    def delete_item_if_exists(self,name):
        if self.is_item_present(name):
            self.delete_item(name)