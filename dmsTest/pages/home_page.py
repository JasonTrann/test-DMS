from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    CART_BTN = (By.XPATH, "//a[@class='shopping_cart_link']")
    SWAG_LAB_LOGO = (By.XPATH, "//div[@class='primary_header']//div[@class='app_logo']")
    HAMBURGER_MENU_BTN = (By.XPATH, "//div[@class='bm-burger-button']//button[@id='react-burger-menu-btn']")
    LOG_OUT_BTN = (By.CSS_SELECTOR, "#logout_sidebar_link")

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def click_cart_button(self):
        print("CLick Cart Button")
        self.find_element(*self.CART_BTN).click()

    def is_home_page_displayed(self):
        print("Check if Home Page is displayed")
        try:
            self.wait_element(*self.SWAG_LAB_LOGO)
            return True
        except TimeoutException:
            return False

    def click_hamburger_menu_button(self):
        print("CLick Hamburger Button")
        self.find_element(*self.HAMBURGER_MENU_BTN).click()

    def click_log_out_button(self):
        print("CLick Log Out Button")
        self.find_element(*self.LOG_OUT_BTN).click()