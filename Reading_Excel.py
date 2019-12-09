
import xlrd
loc = ("C:/Users/VSCBS/Downloads/FultonCounty/FultonTestData.xlsx")
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_name("GetPTO")
print(sheet.nrows)
# For row 0 and column 0
sheet.cell_value(0, 0)
for i in range(sheet.nrows):
    print(sheet.cell_value(i, 0))
