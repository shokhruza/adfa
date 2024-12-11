# matrix=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
#
# print("Matrix= ", matrix)


# /// 1-savol

# row = int(input("Enter the number of rows: "))
# column = int(input("Enter the number of columns: "))
#
# matrix=[]
# print("Enter the entries row wise: ")
#
# for row in range(row):
#     a=[]
#     for column in range(column):
#         a.append(int(input()))
#     matrix.append(a)


# x=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# row = column = 1
# x[row][column] = 11
# print(x)


# x = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# result = []
#
# for row in reversed(x):
#     result.append(row[::-1])
#
# for row in result:
#     print(row)


# x = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# result = []
#
# for row in x:
#     row.reverse()
#
# for row in x:
#     print(row)


import json
import csv

# file_path = "C:/Users/HP Victus/PycharmProjects/python_P21/module_3/lesson_8/centers.json"
#
# with open(file_path, mode='r') as f:
#     data = json.load(f)
#
# with open("center.csv", 'w') as f:
#     fieldnames = list(data[0].keys())
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)

import openpyxl

# path = "task1.xls"
# wb_obj = openpyxl.load_workbook(path)
# sheet_obj = wb_obj.active
# cell_obj = sheet_obj.cell(row=1, column=1)
# print(cell_obj.value)



with open('cars.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    fieldnames = list(csv_reader[0].keys())
    writer = json.DictWriter(csv_reader, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(csv_reader)

with open("cars.json", 'w') as f:
    data = json.load(f)
