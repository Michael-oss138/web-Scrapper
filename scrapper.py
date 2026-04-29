from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

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

    def get_first_job(self):
        driver = self.driver
        job_cards = driver.find_elements(By.CSS_SELECTOR, "article, .job, .job-card, li")

        print(f"Found {len(job_cards)} potential job cards")

        if not job_cards:
            print("No job cards found. Selector needs adjustment.")
            return

        job = job_cards[0]

        try:
            title = job.text  

            link = ""
            try:
                link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
            except:
                pass

            print("\n FIRST JOB FOUND")
            print("Title/Text:", title)
            print("Link:", link)

        except Exception as e:
            print("Error extracting job:", e)