from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_see_dashboard(self):
        # Check if localhost returns the index page
        self.browser.get('http://localhost:8000')

        # In this page, the user receives the project's name
        self.assertIn('{{ cookiecutter.project_name }}', self.browser.title)

        self.fail('Finish the test!')

class AccessibilityTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_visual_impaired(self):
        # Check if all images have `alt` attribute
        images = self.browser.find_elements_by_tag_name('img')
        self.assertTrue(
            all(image.get_attribute('alt') != '' for image in images), 'Image without `alt` attribute'
        ) 

        self.fail('Finish the test!')


if __name__ == "__main__":
    unittest.main(warnings='ignore')
