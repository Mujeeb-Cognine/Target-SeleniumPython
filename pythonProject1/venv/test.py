from selenium import webdriver
import re
import time


class AmazonSearch:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.driver.maximize_window()

    def search_amazon(self, search_query):

    self.driver.get("https://www.amazon.com/")
    search_box = self.driver.find_element_by_id("twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys(search_query)
    search_box.submit()
    time.sleep(2)


def get_titles(self):
    titles = self.driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
    titles_text = [title.text for title in titles]
    return titles_text


def close_browser(self):
    self.driver.quit()


# Example usage:
if __name__ == "__main__":
    amazon = AmazonSearch("path_to_chromedriver.exe")
    amazon.search_amazon("laptop")
    titles = amazon.get_titles()

    # Search and replace operation
    replaced_titles = [re.sub(r'\b([A-Za-z]+)\b', r'Replacement_\1', title) for title in titles]

    # Grouping and capturing
    grouped_titles = [re.search(r'(Replacement_\w+)\s(\d+)', title).groups() for title in replaced_titles if
                      re.search(r'(Replacement_\w+)\s(\d+)', title)]

    # Creating and using modules
    # Assuming 'mymodule.py' contains additional functionalities
    # import mymodule

    # Working with packages
    # Assuming 'mypackage' is a custom package with additional functionalities
    # from mypackage import some_module

    # Class usage
    # Custom class and its method calls are demonstrated above

    amazon.close_browser()
