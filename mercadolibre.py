import unittest
from pyunitreport import HTMLTestRunner
from time import sleep
from selenium import webdriver

class TestingMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "./chromedriver")
        driver = self.driver
        driver.get('https://www.mercadolibre.com')
        driver.maximize_window()

    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        location = driver.find_element_by_partial_link_text('Bogotá D.C.')
        location.click()
        sleep(3)

        condition = driver.find_element_by_partial_link_text('Nuevo')
        condition.click()
        sleep(3)

        order_menu = driver.find_element_by_class_name('ui-dropdown__link')
        order_menu.click()
        higher_price = driver.find_element_by_css_selector('#inner-main > aside > section.view-options > dl > div > div > div > div > ul > li:nth-child(3) > a')
        higher_price.click()
        sleep(3)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'/html/body/main/div[2]/div/section/ol/li[{i + 1}]/div/div[2]/div/h2/a/span').text
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(f'/html/body/main/div[2]/div/section/ol/li[{i + 1}]/div/div[2]/div/div[1]/div/span[2]').text
            prices.append(article_price)
        
        print(articles, prices)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'ml-report'))