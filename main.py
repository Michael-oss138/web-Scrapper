from scrapper import JobScraper

url = "https://www.globaljobs.org/"

def main():
    scrapper = JobScraper()

    try:
        print("Starting scraper...")

        scrapper.open_site(url)

        input("\n Press ENTER to inspect page...")

        jobs = scrapper.get_first_job()

        if jobs:
            scrapper.save_to_csv(jobs)
        else:
            print("No jobs found")
            input("\n Press ENTER to close browser...")

    except Exception as e:
        print(" Error:", e)

    finally:
        print(" Closing browser...")
        scrapper.close()


if __name__ == "__main__":
    main()