from selenium.webdriver.common.by import By


class NewItemPageLocators:
    NEW_ITEM_LINK = (By.LINK_TEXT, "New Item")
    DASHBOARD_LINK = (By.XPATH, "//a[text() = 'Dashboard']")
    ITEM_NAME_FIELD = (By.ID, "name")
    FREESTYLE_PROJECT_OPTION = (By.XPATH, "//li[@class='hudson_model_FreeStyleProject']")
    OK_BUTTON = (By.ID, "ok-button")
    CONFIGURE_HEADER = (By.XPATH, "//h1[normalize-space()='Configure']")
    GENERAL_OR_CONFIGURE_SECTION = (By.XPATH, "//form[@name='config']")
    ITEM_NAME_ERROR_MESSAGE = (By.XPATH, '//div[@id="itemname-invalid"]')
    ITEM_NAME_DUPLICATE_ERROR_MESSAGE = (By.XPATH, '//div[@class = "input-validation-message"]')
