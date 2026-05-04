from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import csv


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

        jobs = []

        print(f"Total links found: {len(links)}")

        for link in links:
            #text = (link.get_attribute("inner text") or "").strip()
            href = link.get_attribute("href")

#            print(f"TEXT: {text[:40]} | LINK: {href}")
 #           input("\n🛑 Inspect these links. Press ENTER to continue...")
            if not href:
                continue

            # filter meaningful links
            if "/jobs/" in href :
                raw_title = href.split("/")[-1]
                title = raw_title.replace("-", " ")
                jobs.append({
                    "title": title,
                    "link": href
                })
        print(f" Extracted {len(jobs)} jobs")
        return jobs

            #if href and "job" in href.lower() and len(text) > 5:
               # print("\n FIRST JOB-LIKE ITEM FOUND")
                #print("Title:", text)
                #print("Link:", href)
                #return

       # print(" No meaningful job links found")
    def save_to_csv(self, jobs):
        filename = "jobs.csv"

        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "link"])
            writer.writeheader()
            writer.writerows(jobs)

        print(f" Jobs saved to {filename}")

    def close(self):
        self.driver.quit()