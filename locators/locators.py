from selenium.webdriver.common.by import By


class NewItemPageLocators:
    NEW_ITEM_LINK = (By.LINK_TEXT, "New Item")
    ITEM_NAME_FIELD = (By.ID, "name")
    FREESTYLE_PROJECT_OPTION = (By.XPATH, "//li[@class='hudson_model_FreeStyleProject']")
    OK_BUTTON = (By.ID, "ok-button")
    CONFIGURE_HEADER = (By.XPATH, "//h1[normalize-space()='Configure']")
    GENERAL_OR_CONFIGURE_SECTION = (By.XPATH, "//form[@name='config']")
