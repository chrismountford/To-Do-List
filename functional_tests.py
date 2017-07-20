from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retreive_it_later(self):

        # User goes to homepage
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(3)

        # Page title has 'To-Do' in the title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Asked to enter a to-do item straight away
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Types in first to-do
        input_box.send_keys('Buy peacock feathers')

        # When Enter is hit, the page updates
        input_box.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # Another to-do prompt
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)

        # Page updates again and the page shows the last two items
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # The site has generated a unique URL for the user
        self.fail('Finish the test!')

        # Visiting the URL takes the user to their to-do list


if __name__ == '__main__':
    unittest.main()
