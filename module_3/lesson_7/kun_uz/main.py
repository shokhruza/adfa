# import httpx
# from bs4 import BeautifulSoup
#
# response = httpx.get("https://kun.uz")
# kun_html = response.text
#
# soup = BeautifulSoup(kun_html, 'html.parser')
# rows = soup.find_all('div', {"class": "col-md-6"})
# for row in rows[:]:
#     title = row.find('a', {"class": "small-news__title"})
#     if title:
#         print(title.text)
#
#     print()
#     print()
















import asyncio
import httpx


# async def requests_get():
#     async with httpx.AsyncClient() as client:
#         response = await client.get("https://storage.kun.uz/source/10/jKanqzC8J1IAFvMqK0pMdzF8Ju0DCz8U.jpg")
#     return response.content
#
#
# photo_text = asyncio.run(requests_get())
# with open("../photo/rasm1.png", 'wb') as f:
#     f.write(photo_text)

# async def requests_get():
#     async with httpx.AsyncClient() as client:
#         response = await client.get("https://storage.kun.uz/source/10/yrr_coDcborb2Jqc0kcMK1p6wgyOTxKL.jpg")
#     return response.content
#
#
# photo_text = asyncio.run(requests_get())
# with open("../photo/rasm2.png", 'wb') as f:
#     f.write(photo_text)

# async def requests_get():
#     async with httpx.AsyncClient() as client:
#         response = await client.get("https://storage.kun.uz/source/10/dmaLXPORTwe7bpVVyJ7y9pjPc-JKNAT6.jpg")
#     return response.content
#
#
# photo_text = asyncio.run(requests_get())
# with open("../photo/rasm3.png", 'wb') as f:
#        f.write(photo_text)


async def requests_get():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://storage.kun.uz/source/10/Yx6NcuwVGWqKnFPguHgtXvuWcO7fXqh5.jpg")
    return response.content


photo_text = asyncio.run(requests_get())
with open("../photo/rasm4.png", 'wb') as f:
       f.write(photo_text)













