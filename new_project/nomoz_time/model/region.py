from httpx import get
from bs4 import BeautifulSoup


class Region:
    def __init__(self, link=None):
        self.link = link

    def dictrict_list(self):
        html = get(self.link).text
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.find_all("div", {"class": "col-xl-4 col-xs-12 py-1"})
        districts = []
        for pas, row in enumerate(rows, 1):
            district = {
                "id": pas,
                "link": row.find("a")["href"],
                "name": row.find("a").text
            }
            districts.append(district)
        return districts


    def region_list(self):
        html = get(self.link).text
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.find_all("div", {"class": "col-xl-4 col-xs-12 py-1"})
        regions = []
        for pas, row in enumerate(rows, 1):
            region = {
                "id": pas,
                "link": row.find("a")["href"],
                "name": row.find("a").text
            }
            regions.append(region)
        return regions
