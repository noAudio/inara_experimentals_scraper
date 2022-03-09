import json
from typing import Any, Dict
import requests
from bs4 import BeautifulSoup


class ExperimentalsScraper:
    url: str
    page: requests.Response
    soup: BeautifulSoup
    experimentals: Dict[str, Dict[str, str]] = {}
    experimentalsJson: str

    def __init__(self, url: str) -> None:
        # Set up script
        self.url = url
        self.getPage()
        self.setExperimentals()
        self.toJson()

    def getPage(self) -> None:
        # Download page using requests then set to [page] property.
        if self.url == None:
            print("Undefined url.")
            pass

        self.page = requests.get(self.url)

    def setExperimentals(self) -> None:
        # Iterate over elements to extract the information.
        if self.page == None:
            print("Page has not been downloaded.")
            pass

        self.soup = BeautifulSoup(self.page.content, "html.parser")
        # Find the main content div
        div = self.soup.find("div", class_="mainblock")

        # Get all child elements, they contain the needed data.
        children: Any = div.findChildren("div", recursive=False)

        # Loop over the children and get the data
        for child in children:
            titleElement: Any = child.find("div", class_="blocktoggletrigger")
            title: str = titleElement.text
            materialElements: Any = child.find_all(
                "span", class_="materialnamewithcount"
            )
            materials: Dict[str, str] = {}

            for material in materialElements:
                name = material.find("a", class_="inverse")
                amount = material.find("span", class_="materialcount")
                materials[name.text] = amount.text

            self.experimentals[title] = materials

    def toJson(self) -> None:
        # Convert the data in the dictionary into json format.
        if self.experimentals == None:
            print("Scraping incomplete")
            pass
        self.experimentalsJson = json.dumps(self.experimentals)
