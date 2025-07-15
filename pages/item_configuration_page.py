from locators.locators import ItemConfigurationPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ItemConfigurationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def wait_until_general_section_visible(self):
        self.wait.until(
            EC.presence_of_element_located(ItemConfigurationPageLocators.CONFIGURATION_PAGE_TITLE)
        )

    def is_general_section_visible(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(ItemConfigurationPageLocators.CONFIGURATION_PAGE_TITLE)
            )
            return True
        except:
            return False

    def click_submit_button(self):
        save_button = self.wait.until(
            EC.element_to_be_clickable(ItemConfigurationPageLocators.SAVE_BUTTON)
        )
        save_button.click()

