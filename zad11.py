from openpyxl import Workbook
import csv

wb = Workbook()
ws = wb.active
ws.title = "Blank"



exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)

with open('example.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        ws.append(row)


wb.save(filename = 'plik.xlsx')





