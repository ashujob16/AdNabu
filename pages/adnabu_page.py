from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdnabuPage(BasePage):

    ENTER_PASSWORD = (By.NAME, "password")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Enter']")
    SEARCH_ICON = (By.CSS_SELECTOR, "summary[aria-label='Search']")
    ENTER_TEXT = (By.NAME, "q")
    SEARCH_BUTTON = (By.XPATH, "//button[@class='search__button field__button']")
    SELECT_PRODUCT = (By.XPATH, "//a[@id='CardLink--7801364480090']")
    ADD_TO_CART = (By.XPATH, "//button[@name='add']")

    def enter_password(self, password):
        self.type(self.ENTER_PASSWORD, password)

    def click_enter_button(self):
        self.click(self.ENTER_BUTTON)

    def click_search_icon(self):
        self.click(self.SEARCH_ICON)

    def enter_text(self, text):
        self.type(self.ENTER_TEXT, text)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    def select_product(self):
        self.click(self.SELECT_PRODUCT)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)
