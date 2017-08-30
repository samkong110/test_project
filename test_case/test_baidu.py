#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):
    '''百度'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.baidu.com"

    def test_baidu(self):
	'''百度搜索:unittest'''
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title,u"unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

