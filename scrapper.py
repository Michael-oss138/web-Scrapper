from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time 


class JobScrapper:
    def __init__(self):
        options = Options()
        options.add_arguement("--start-maximized")

        self.driver = webdriver.Chrome(options=options)

    def open_site(self, url):
        self.driver.get(url)
        time.sleep(3)

    def close(self):
        self.driver.quit()