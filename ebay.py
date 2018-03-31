from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .urls import get_ebaylogin_url
from .urls import get_ebaylogin_url_rate
import random
import time
import random

class ebay:

    def __init__(self, headless=False):
        # chrome initialization
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)
        if headless:
            options.add_argument('headless')
            options.add_argument('window_size=1024x768')
        self.driver = webdriver.Chrome('./chromedriver.exe',
                                       chrome_options=options)
        #for windows use chromedriver.exe

    def login(self, user, passwd):
        self.driver.get(get_ebaylogin_url())
        user_field = self.driver.find_element_by_xpath("//input[@id='userid']")
        passwd_field = self.driver.find_element_by_xpath("//input[@id='pass']")
        ActionChains(self.driver).move_to_element(
            user_field).click().send_keys(user).perform()
        ActionChains(self.driver).move_to_element(
            passwd_field).click().send_keys(passwd).perform()
        self.driver.find_element_by_id('sgnBt').click()

    def rate(self):
        self.driver.get(get_ebaylogin_url_rate())
        ammount200 = self.driver.find_elements_by_name('itemsPerPageDrpDwn-menu-button')
        ActionChains(self.driver).move_to_element(ammount200).click()
        makelist200 = self.driver.find_element_by_xpath("//*[@id='itemsPerPageDrpDwn-menu']/li[4]")
        ActionChains(self.driver).move_to_element(makelist200).click()
        time.sleep(20)
        #cause when your internet sucks this will take time
        self.driver.find_element_by_id('grid-table-bulk-checkbox').click()
        time.sleep(3)
        self.driver.find_element_by_id('gridSummary-wrapper-id-w11').click()

    def reallyrate(self, ratings):
        self.driver.find_element_by_id('commenttype2').click()
        indi = self.driver.find_element_by_id('customcomment')
        ActionChains(self.driver).move_to_element(indi).click().send_keys(random.choice(ratings)).perform()
        time.sleep(10)
        self.driver.find_element_by_name('LeaveFeedback').click()

    def close(self):
        self.driver.close()
