from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retreive_it_later(self):

        # User goes to homepage
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(3)

        # Page title has 'To-Do' in the title
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Asked to enter a to-do item straight away

        # Types in first to-do

        # When Enter is hit, the page updates

        # Another to-do prompt

        # Page updates again and the page shows the last two items

        # The site has generated a unique URL for the user

        # Visiting the URL takes the user to their to-do list


if __name__ == '__main__':
    unittest.main()
