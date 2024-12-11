# /// 1
# range(start , end , step) clone generatorda yaratish
# def range_clone(start, end, step):
#     current = start
#     while current <= end:
#         yield current
#         current += step
#
#
# for i in range_clone(0, 10, 2):
#     print(i)


# /// 2
# date1 = "1997-03-09"    date2 = "2021-08-05"
# shu oralig'da nech kun farq borligini topuvchi dastur tuzing

# import datetime
#
# date1 = "1997-03-09"
# date2 = "2021-08-05"
#

# date1 = datetime.datetime(1997, 3, 9)
# date2 = datetime.datetime(2021, 8, 5)
# print(date2-date1)



# /// 3
# 4 ta function yaratilsin !
# 1-si function 3 secund , 2-si function 4 secund , 3-si function 6 secund, 4-si function 8 secund
# va bu yaratilgan functionlarni bir vaqtda minimum vaqtda ishini tugatadigan dastur tuzulsin


# import threading
# import os
# import time
#
#
# def function1():
#     time.sleep(3)
#     print("function1", os.getpid())
#
#
# def function2():
#     time.sleep(4)
#     print("function2", os.getpid())
#
#
# def function3():
#     time.sleep(6)
#     print("function3", os.getpid())
#
#
# def function4():
#     time.sleep(8)
#     print("function4", os.getpid())
#
#
# f = [function1, function2, function3, function4]
# start = time.time()
# threads = []
# for i in f:
#     t = threading.Thread(target=i)
#     t.start()
#     threads.append(t)
#     for thread in threads:
#         thread.join()
#
# print(time.time() - start)


# /// 4
# async , Multithreading , Multiprocessing bir biridan farqi aniqroq yoritilsin
# async request yuboradigan function yaratilsin (aiohttp) :
# https://jsonplaceholder.typicode.com/     posts, comments , users, albums , photos , todos
# import requests
# import aiohttp
# import asyncio
#
#
# async def fetch_data(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.json()
#
#
# async def main():
#     url = "https://jsonplaceholder.typicode.com/posts"
#     data = await fetch_data(url)
#     print(data)
#
#
# asyncio.run(main())


# import time
# import httpx
# import asyncio
# import json
# res = ["photos","albums","posts","todos","users","comments"]
#
# now_time = time.time()
# async  def requests_get():
#     async with httpx.AsyncClient() as client:
#         for i in res:
#             response = await client.get(f"https://jsonplaceholder.typicode.com/{i}")
#         return response.json()
#
# a = asyncio.run(requests_get())
# for i in res:
#     with open(f"{i}.json", 'w') as f:
#         json.dump(a,f,indent=3)
# print(time.time()-now_time)


# /// 5
# LinkedList : Node class yarating
# https://jsonplaceholder.typicode.com/comments shu linkdan malumotlarni olib LinkedList hosil qilinsin

# import httpx
# import json
#
#
# class Node:
#     def __init__(self, value=None, next=None):
#         self.next = next
#         self.value = value
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = Node()
#
#     def append1(self, data):
#         data = Node(data)
#         start = self.head
#         while start.next:
#             start = start.next
#         start.next = data
#
#     def printer(self):
#         start = self.head
#         l = []
#         while start.next:
#             # l.append(start.next.value)
#             print(start.next.value)
#             start = start.next
#         return l
#
#
# link = "https://jsonplaceholder.typicode.com/comments"
#
# res = httpx.get(link)
# res = res.json()
#
# a = LinkedList()
# for i in res:
#     a.append1(i)
# a.printer()

#  /// 6
# yangi todos.xlsx excel filega https://jsonplaceholder.typicode.com/todos
# datasi bilan to'ldiriladigan qilinsin ! yaratiladigan barcha narsala ascyn qilib yaratilsin

# import requests
# import pandas as pd
#
# def get_todos():
#     try:
#         response = requests.get('https://jsonplaceholder.typicode.com/todos')
#         todos = response.json()
#         return todos
#     except Exception as e:
#         print("Xato: ", e)
#         return None
#
# def write_to_excel(todos):
#     try:
#         df = pd.DataFrame(todos)
#         df.to_excel('todos.xlsx', index=False)
#         print("Ma'lumotlar Excel fayliga yozildi.")
#     except Exception as e:
#         print("Xato: ", e)
#
# def main():
#     todos = get_todos()
#     if todos:
#         write_to_excel(todos)
#
# if __name__ == "__main__":
#     main()

# /// 7
# binary search algoritimni codini

# find = 45
# l = [11, 15, 20, 30, 45, 50, 78]
# L = 0
# H = len(l) - 1
# while L <= H:
#     mid = (L + H) // 2
#     if l[mid] == find:
#         print(mid)
#         break
#     if l[mid] > find:
#         H = mid - 1
#     else:
#         L = mid + 1
# else:
#     print("Not found")

# insertion sort
# def insertion_sort(array):
#     # Loop from the second element of the array until
#     # the last element
#     for i in range(1, len(array)):
#         # This is the element we want to position in its
#         # correct place
#         key_item = array[i]
#
#         # Initialize the variable that will be used to
#         # find the correct position of the element referenced
#         # by `key_item`
#         j = i - 1
#
#         # Run through the list of items (the left
#         # portion of the array) and find the correct position
#         # of the element referenced by `key_item`. Do this only
#         # if `key_item` is smaller than its adjacent values.
#         while j >= 0 and array[j] > key_item:
#             # Shift the value one position to the left
#             # and reposition j to point to the next element
#             # (from right to left)
#             array[j + 1] = array[j]
#             j -= 1
#
#         # When you finish shifting the elements, you can position
#         # `key_item` in its correct location
#         array[j + 1] = key_item
#
#     return array

# def search(arr, curr_index, key):
#     if curr_index == -1:
#         return -1
#     if arr[curr_index] == key:
#         return curr_index
#     return search(arr, curr_index-1, key)

# binary search
# def binary_search(arr, low, high, x):
#     # Check base case
#     if high >= low:
#
#         mid = (high + low) // 2
#
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid
#
#         # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)
#
#         # Else the element can only be present in right subarray
#         else:
#             return binary_search(arr, mid + 1, high, x)
#
#     else:
#         # Element is not present in the array
#         return -1
#
#
# # Test array
# arr = [2, 3, 4, 10, 40]
# x = 10
#
# # Function call
# result = binary_search(arr, 0, len(arr) - 1, x)
#
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")

# def my_filter(function, iterable):
#     for item in iterable:
#         if function(item):
#             yield item
#
# # Örnek kullanım
# def is_even(x):
#     return x % 2 == 0
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = my_filter(is_even, numbers)
# print(list(even_numbers))  # Çıktı: [2, 4, 6, 8, 10]
