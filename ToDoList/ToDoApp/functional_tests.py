# from selenium import webdriver

# browser = webdriver.Firefox(executable_path=r'F:\JOB\CIKLUM\ToDo_List\myenv\Lib\geckodriver.exe')
# browser.get('http://127.0.0.1:8000')
# # self.browser.get('http://127.0.0.1:8000')

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox(executable_path=r'F:\JOB\CIKLUM\ToDo_List\myenv\Lib\geckodriver.exe')

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://127.0.0.1:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)  
        self.fail('Finish the test!')  

        # She is invited to enter a to-do item straight away
        # [...rest of comments as before]

if __name__ == '__main__':  
    unittest.main()