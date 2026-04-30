from scrapper import JobScraper

URL = "https://www.globaljobs.org/"

def main():
    scrapper = JobScraper()

    try:
        print("Starting scraper...")

        scrapper.open_site(URL)

        input("\n Press ENTER to inspect page...")

        scrapper.debug_page()

        input("\n Press ENTER to extract first job...")

        scrapper.get_first_job()

        input("\n Press ENTER to close browser...")

    except Exception as e:
        print(" Error:", e)

    finally:
        print(" Closing browser...")
        scrapper.close()


if __name__ == "__main__":
    main()