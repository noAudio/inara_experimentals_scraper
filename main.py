from experimentals_scraper import ExperimentalsScraper


def main():
    scraper: ExperimentalsScraper = ExperimentalsScraper(
        url="https://inara.cz/experimentaleffects/"
    )
    print(scraper.experimentalsJson)


if __name__ == "__main__":
    main()
