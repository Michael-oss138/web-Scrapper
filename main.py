from scrapper import JobScraper

URL = "https://globaljobs.org"

scraper = JobScraper()

scraper.open_site(URL)

input("Press ENTER to close browser...")

scraper.close()