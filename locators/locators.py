from selenium.webdriver.common.by import By


class NewItemPageLocators:
    NEW_ITEM_LINK = (By.LINK_TEXT, "New Item")
    NEW_ITEM_HEADER = (By.XPATH, '// h1[text() = "New Item"]')
    DASHBOARD_LINK = (By.XPATH, "//a[text() = 'Dashboard']")
    ITEM_NAME_FIELD = (By.ID, "name")
    FREESTYLE_PROJECT_OPTION = (By.XPATH, "//li[@class='hudson_model_FreeStyleProject']")
    OK_BUTTON = (By.ID, "ok-button")
    CONFIGURE_HEADER = (By.XPATH, "//h1[normalize-space()='Configure']")
    GENERAL_OR_CONFIGURE_SECTION = (By.XPATH, "//form[@name='config']")
    ITEM_NAME_ERROR_MESSAGE = (By.XPATH, '//div[@id="itemname-invalid"]')
    ITEM_NAME_DUPLICATE_ERROR_MESSAGE = (By.XPATH, '//div[@class = "input-validation-message"]')
    COPY_FROM_FIELD = (By.ID, "from")
    COPY_FROM_ERROR_MESSAGE = (By.XPATH, '//h1[contains(text(),"Error")]/following-sibling::p')


class DashboardPageLocators:
    @staticmethod
    def ITEM_LINK(name):
        return (By.LINK_TEXT, name)


class ItemConfigurationPageLocators :
    CONFIGURATION_PAGE_TITLE = (By.XPATH, "//li[normalize-space()='Configuration']")
    SAVE_BUTTON = (By.NAME, "Submit")


class ItemPageLocators:
    ITEM_ROW_BY_NAME = (By.XPATH, "//span[normalize-space()='{item_name}']")
    ITEM_DROPDOWN_BUTTON: tuple[str, str] = (By.XPATH, '//button[contains(@class, "jenkins-menu-dropdown-chevron") '
                                                       'and contains(@data-href, "{item_name}")]')
    ITEM_DELETE_OPTION = (By.XPATH, "//button[contains(@href,'/job/{item_name}/doDelete')]")
    ITEM_CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[@data-id='ok']")
