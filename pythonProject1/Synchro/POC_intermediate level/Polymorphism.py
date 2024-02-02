from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.common.by import By


class AmazonAutomation(ABC):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    @abstractmethod
    def search_product(self, product):
        pass

    @abstractmethod
    def display_titles(self):
        pass

    def close_browser(self):
        self.driver.quit()


class LaptopSearch(AmazonAutomation):
    def search_product(self, product):
        self.driver.get("https://www.amazon.in")
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(product)
        search_box.submit()

    def display_titles(self):
        results = self.driver.find_elements(By.CSS_SELECTOR, ".s-result-item .a-text-normal")
        for result in results[:5]:
            print(result.text)


def main():
    laptop_search = LaptopSearch()
    laptop_search.search_product("laptop")
    laptop_search.display_titles()
    laptop_search.close_browser()


if __name__ == "__main__":
    main()
