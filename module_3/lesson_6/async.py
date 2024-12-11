# import asyncio
# import httpx


# async def requests_get():
#     async with httpx.AsyncClient() as client:
#         response = await client.get("https://telegra.ph/file/23fff68fcbf36e8adabdd.png")
#     return response.content
#
#
# photo_text = asyncio.run(requests_get())
# with open("rasm.png",'wb') as f:
#     f.write(photo_text)


# async def g():
#     result = 10 + 10
#     return result
#
#
# print(asyncio.run(g()))

# async def b():
#     result = 20 + 20
#     return result
#
#
# async def a():
#     result = await b()
#     return result
#
#
# print(asyncio.run(a()))


import shutil
import asyncio

# # Word fayli nomi
word_file = "task_photo.doc"
#
# # Rasmdagi fayl nomi
image_file = "path/to/image/image.png"
#
# # Rasmdagi faylni pycharmga ko'chirib olish
shutil.copy(image_file, "path/to/pycharm/image.png")


async def requests_get():
    async with word_file as client:
        response = await shutil.copy(image_file)

    return response.content


photo_text = asyncio.run(requests_get())
with open("path/to/image/image.png", 'rb') as f:
    f.write(photo_text)
