import httpx
import asyncio


# category_id = input(" Category_ig: >>> ")
# response = httpx.get("http://10.10.2.186:8000/categories/{category_id}")
# data = response.json()
# for key, val in data.items():
#     print(key, val)

class UI:
    def category_list(self):
        response = httpx.get("http://10.10.2.186:8000/categories")
        data = response.json()
        for category in data:
            print(f"{category.get('id')} {category.get('name')}")

    def category_detail(self):
        category_id = input(" Category_id: >>> ")
        response = httpx.get(f"http://10.10.2.186:8000/categories/{category_id}")
        data = response.json()
        for key, val in data.items():
            print(key, val)

    def main(self):
        menu = """
        1)category list
        2)category detail
        0)exit
        >>>"""
        key = input(menu)
        match key:
            case "1":
                self.category_list()
            case "2":
                self.category_detail()
            case "0":
                return


UI().main()
