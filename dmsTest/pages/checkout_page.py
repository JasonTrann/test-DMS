from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import users
from selenium.common.exceptions import TimeoutException


class CheckOutPage(BasePage):
    YOUR_CART_TEXT = (By.XPATH, "//span[contains(text(),'Your Cart')]")
    CHECKOUT_BTN = (By.XPATH, "//div[@id='cart_contents_container']//div[@class='cart_footer']//button[@id='checkout']")
    FIRST_NAME_INFO = (By.XPATH, "//div[@class='checkout_info']//input[@id='first-name']")
    LAST_NAME_INFO = (By.XPATH, "//div[@class='checkout_info']//input[@id='last-name']")
    ZIP_CODE_INFO = (By.XPATH, "//div[@class='checkout_info']//input[@id='postal-code']")
    CONS_BTN = (By.XPATH, "//div[@class='checkout_buttons']//input[@id='continue']")
    CHECK_OUT_YOUR_INFO_TEXT = (By.XPATH, "//span[contains(text(),'Checkout: Your Information')]")
    CHECK_OUT_OVERVIEW_TEXT = (By.XPATH, "//span[contains(text(),'Checkout: Overview')]")
    FINISH_BTN = (By.XPATH, "//div[@class='cart_footer']//button[@id='finish']")
    BACK_HOME_BTN = (By.XPATH, "//h2[normalize-space()='THANK YOU FOR YOUR ORDER']/following-sibling::button[@id='back-to-products']")
    THANK_YOU_TEXT = (By.XPATH, "//h2[normalize-space()='THANK YOU FOR YOUR ORDER']")

    def __init__(self, driver):
        super(CheckOutPage, self).__init__(driver)

    def is_check_out_page_displayed(self):
        print("Check if Check Out Page is displayed")
        try:
            self.wait_element(*self.YOUR_CART_TEXT)
            self.wait_element(*self.CHECKOUT_BTN)
            return True
        except TimeoutException:
            return False

    def click_check_out_button(self):
        print("CLick Check Out Button")
        self.find_element(*self.CHECKOUT_BTN).click()

    def enter_first_name_checkout_info(self, first_name):
        print("Input First Name")
        self.find_element(*self.FIRST_NAME_INFO).send_keys(first_name)

    def enter_last_name_checkout_info(self, last_name):
        print("Input Last Name")
        self.find_element(*self.LAST_NAME_INFO).send_keys(last_name)

    def enter_zip_code_checkout_info(self, zip_code):
        print("Input Zip Code")
        self.find_element(*self.ZIP_CODE_INFO).send_keys(zip_code)

    def click_continue_button(self):
        print("Click Continue Button")
        self.find_element(*self.CONS_BTN).click()

    def is_check_out_step_one_page_displayed(self):
        print("Check if Check Out Step One Page is displayed")
        try:
            self.wait_element(*self.CHECK_OUT_YOUR_INFO_TEXT)
            self.wait_element(*self.CONS_BTN)
            return True
        except TimeoutException:
            return False

    def is_check_out_step_two_page_displayed(self):
        print("Check if Check Out Step Two Page is displayed")
        try:
            self.wait_element(*self.CHECK_OUT_OVERVIEW_TEXT)
            self.wait_element(*self.FINISH_BTN)
            return True
        except TimeoutException:
            return False

    def click_finish_button(self):
        print("Click Finish Button")
        self.find_element(*self.FINISH_BTN).click()

    def is_check_out_complete_page_displayed(self):
        print("Check if Check Out Complete Page is displayed")
        try:
            self.wait_element(*self.THANK_YOU_TEXT)
            self.wait_element(*self.BACK_HOME_BTN)
            return True
        except TimeoutException:
            return False

    def click_back_home_button(self):
        print("Click BAck Home Button")
        self.find_element(*self.BACK_HOME_BTN).click()

    def input_check_out_info_and_click_continue(self, user):
        user = users.get_user(user)
        print(user)
        self.enter_first_name_checkout_info(user["first_name"])
        self.enter_last_name_checkout_info(user["last_name"])
        self.enter_zip_code_checkout_info(user["zip_code"])
        self.click_continue_button()
