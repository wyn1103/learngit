# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test23(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.cnki.net/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_23(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()
        self.assertEqual(u"中国知网—用户登录", driver.title)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("wyn20152015")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("wa1234")
        self.assertEqual(u"欢迎wyn20152015 wyn20152015 的朋友！", driver.find_element_by_css_selector("div.wrapper.section1").text)
        driver.find_element_by_id("submittext").click()
        driver.find_element_by_id("highSearch").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp |  | 30000]]
        try: self.assertEqual(u"文献来源： 模糊 精确", driver.find_element_by_id("joursource_1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("txt_1_value1").click()
        driver.find_element_by_id("txt_1_value1").click()
        driver.find_element_by_id("txt_1_value1").clear()
        driver.find_element_by_id("txt_1_value1").send_keys("USBKey")
        Select(driver.find_element_by_id("txt_2_sel")).select_by_visible_text(u"摘要")
        driver.find_element_by_id("txt_2_value1").click()
        driver.find_element_by_id("txt_2_value1").clear()
        driver.find_element_by_id("txt_2_value1").send_keys("USBKey")
        driver.find_element_by_id("publishdate_from").click()
        driver.find_element_by_id("publishdate_from").clear()
        driver.find_element_by_id("publishdate_from").send_keys("2016-01-01")
        driver.find_element_by_id("publishdate_to").click()
        driver.find_element_by_id("publishdate_to").clear()
        driver.find_element_by_id("publishdate_to").send_keys("2017-12-01")
        driver.find_element_by_id("btnSearch").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframeResult | ]]
        driver.find_element_by_link_text(u"基于TrueCrypt和USBKEY的整盘加密系统设计与实现").click()
        driver.find_element_by_link_text(u"基于USBKEY的可信启动的研究与实现").click()
        driver.find_element_by_link_text(u"WSS在基于浏览器和USBKey的数字证书签发系统中的研究与应用").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("loginOut").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
