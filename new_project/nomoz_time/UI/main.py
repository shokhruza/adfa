from new_project.nomoz_time.lang.main import data
from new_project.nomoz_time.model.region import Region
from new_project.nomoz_time.model.nomoz import Namoz

session_lang = "UZ"


class UI:
    def region(self):
        lang_data = data.get(session_lang)
        regions: list[dict] = Region(f"https://namozvaqti.uz/{session_lang.lower()}/viloyat ").region_list()
        for region in regions:
            print(" " * 5, f"{region.get('id')}) {region.get('name')}")
        key = input(f"{lang_data.get('Choose')} : ")
        link = regions[int(key) - 1].get("link")
        self.district(link)

    def district(self, region_name):
        lang_data = data.get(session_lang)
        districts = Region(link).dictrict_list()
        for district in districts:
            print(f"{district.get('id')}) {district.get('name')}")
        key = input(f"{lang_data.get('Choose')} : ")
        link = districts[int(key) - 1].get("link")
        self.show_time(link)

    def show_time(self, link):
        time = Namoz(link).time()
        for name, time in time.items():
            print("" * 10, f"{name}:{time}")

        self.main()

    def main(self):
        lang_data = data.get(session_lang)
        menu = f"""
        1) {lang_data.get("prayer")}
        2) {lang_data.get("suras")}
        3) {lang_data.get("language")}
        4) {lang_data.get("exit")}
        >>> """

        key = input(menu)
        match key:
            case "1":
                self.region()
            case "2":
                self.show_time()
            case "3":
                self.change_lang()
            case "4":
                return

    def change_lang(self):
        menu = """
        1) English   
        2) Uzbek  
        3) Russian
        """
        key = input(menu)
        match key:
            case "1":
                session_lang = "EN"
            case "2":
                session_lang = "UZ"
            case "3":
                session_lang = "RU"
        self.main()
