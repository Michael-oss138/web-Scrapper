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
        print("Page Title:", self.driver.title)

    def debug_page(self):
        print("\n PAGE SNAPSHOT:")
        print(self.driver.page_source[:1500])

    def get_first_job(self):
        driver = self.driver

        # NEW STRATEGY: get all links, not fake job-card selectors
        links = driver.find_elements(By.TAG_NAME, "a")

        print(f"Total links found: {len(links)}")

        for link in links:
            text = (link.get_attribute("inner text") or "").strip()
            href = link.get_attribute("href")

            print(f"TEXT: {text[:40]} | LINK: {href}")
            input("\n🛑 Inspect these links. Press ENTER to continue...")
            if not href or not text:
                continue

            # filter meaningful links
            if href and "job" in href.lower() and len(text) > 5:
                print("\n FIRST JOB-LIKE ITEM FOUND")
                print("Title:", text)
                print("Link:", href)
                return

        print(" No meaningful job links found")

    def close(self):
        self.driver.quit()