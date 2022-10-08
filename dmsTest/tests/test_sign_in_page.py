import unittest

from pages.checkout_page import CheckOutPage
from tests.base_test import BaseTest
from pages.home_page import *
from pages.login_page import *
from time import sleep


# If you want to run it, you should type: python <module-name.py>

class TestSignInPage(BaseTest):

    def test_sign_in_with_valid_user(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        checkout_page = CheckOutPage(self.driver)

        login_page.is_login_page_displayed()
        login_page.login("valid_user")
        home_page.is_home_page_displayed()
        home_page.click_cart_button()
        checkout_page.is_check_out_page_displayed()
        checkout_page.click_check_out_button()
        checkout_page.is_check_out_step_one_page_displayed()
        checkout_page.input_check_out_info_and_click_continue("valid_user")
        checkout_page.is_check_out_step_two_page_displayed()
        checkout_page.click_finish_button()
        checkout_page.is_check_out_complete_page_displayed()
        checkout_page.click_back_home_button()
        home_page.is_home_page_displayed()
        home_page.click_hamburger_menu_button()
        sleep(1)
        home_page.click_log_out_button()
        login_page.is_login_page_displayed()

    def test_sign_in_with_locked_user(self):
        login_page = LoginPage(self.driver)

        login_page.is_login_page_displayed()
        login_page.login("locked_user")
        login_page.is_error_msg_displayed()