from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import users
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePage):
    USER_NAME = (By.XPATH, "//input[@id='login-button']/preceding-sibling::div//input[@id='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='login-button']/preceding-sibling::div//input[@id='password']")
    LOGIN_BTN = (By.XPATH, "//div[@class='login-box']//input[@id='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//h3[contains(text(),'Epic sadface: Sorry, this user has been locked out')]")

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)  # Python2 version

    def is_login_page_displayed(self):
        print("Check if Login Page is displayed")
        try:
            self.wait_element(*self.USER_NAME)
            self.wait_element(*self.PASSWORD)
            self.wait_element(*self.LOGIN_BTN)
            return True
        except TimeoutException:
            return False

    def enter_email(self, email):
        self.find_element(*self.USER_NAME).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.LOGIN_BTN).click()

    def login(self, user):
        user = users.get_user(user)
        print(user)
        self.enter_email(user["user_name"])
        self.enter_password(user["password"])
        self.click_login_button()

    def is_error_msg_displayed(self):
        print("Check if Error Message is displayed")
        try:
            self.wait_element(*self.ERROR_MESSAGE)
            return True
        except TimeoutException:
            return False
