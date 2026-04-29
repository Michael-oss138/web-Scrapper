from scrapper import JobScraper

URL = "https://globaljobs.org"

def main():
    scrapper = JobScraper()

    try:
        scrapper.open_site(URL)

        input("Press ENTER to extract job")
        scrapper.get_first_job()

        input("Press Enter to close browser")

    except Exception as e:
        print("Error:", e)
    finally:
        scrapper.close()

if __name__ == "__main__":
    main()