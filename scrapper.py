from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


class JobScraper:
    def __init__(self):
        options = Options()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def open_site(self, url):
        self.driver.get(url)

        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        print("Page loaded successfully")

    def get_driver(self):
        return self.driver

    def close(self):
        self.driver.quit()