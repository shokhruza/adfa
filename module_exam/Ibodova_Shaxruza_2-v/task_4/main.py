""""""
"""
                         Multithreading haqida aniroq ma'lumot!
CPU:
    1 -> threading
    2 -> multiprocesssing
    3 -> multithreading
"""


import requests
import aiohttp
import asyncio
import json
import csv


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main():
    url = "https://jsonplaceholder.typicode.com/photos"
    data = await fetch_data(url)
    return data


a = asyncio.run(main())

with open("exam.csv", 'w') as f:
    fieldnames = list(a[0].keys())
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(a)
