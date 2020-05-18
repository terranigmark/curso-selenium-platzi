import unittest
from selenium import webdriver
from time import sleep

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_link_text('Add/Remove Elements')
        excercise.click()

    def test_go_to_excercise(self):
        pass

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

