# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 15)
# driver.get("https://www.instacart.com/")
#
# iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[tabindex='0']")))
# driver.switch_to.frame(iframe)
#
# if iframe is not None:
#     time.sleep(10)
#     print("Iframe with specified tabindex found")
#     # print(driver.page_source)
#     checkBox = driver.find_element(By.XPATH, "//*[@type='checkbox']")
#     if checkBox is not None:
#         print("found")
#         driver.execute_script("arguments[0].click();", checkBox)
#     else:
#         print("not found")
# else:
#     print("Iframe with specified tabindex not found")
# time.sleep(20)


import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        self.assertTrue(main_page.is_title_matches(), "python.org title doesn't match.")
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_results_found(), "No results found.")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

