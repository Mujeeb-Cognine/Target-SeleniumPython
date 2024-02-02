import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager


class AmazonAutomation:

    driver = webdriver.Chrome()
    driver.maximize_window()

    def search_product(self, product):
        self.driver.get("https://www.amazon.in")
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(product)
        search_box.submit()

    def display_titles(self):
        result = self.driver.current_url
        print(self.driver.title)
        print("Current URL = ", result)

    def close_browser(self):
        self.driver.quit()


def main():
    amazon = AmazonAutomation()
    amazon.search_product("laptop")
    amazon.display_titles()
    amazon.close_browser()


if __name__ == "__main__":
    main()
    