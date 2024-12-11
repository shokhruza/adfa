# import csv
#
# with open('employee_file2.csv', mode='w') as csv_file:
#     fieldnames = ['emp_name', 'dept', 'birth_month']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'emp_name': 'John Smith', 'dept': ' Accounting', 'birth_month': 'November'})
#     writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})


# import csv
#
# with open('employee_file2.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file, delimiter=',')
#     print(list(csv_reader))


import json
import csv
import openpyxl

# path = "task2.xlsx"
# wb_obj = openpyxl.load_workbook(path)
# sheet_obj = wb_obj.active
# cell_obj = sheet_obj.cell(row=1, column=1)
# print(cell_obj.value)
