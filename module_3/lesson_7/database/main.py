import httpx
import asyncio

# category_id = input(" Category_ig: >>> ")
news = httpx.get("https://kun.uz")
data = news.json()
for category in data:
    print(f"{category.get('file_path')} {category.get('name')}")

# photo_text = asyncio.run(requests_get())
with open("news..json", 'w') as f:
    f.write(data)
