import openpyxl

wb = openpyxl.Workbook("demo.xlsx")

hoja1 = wb.create_sheet("productos")

hoja1["A1"] = 10
a1 = hoja1["A1"]
print(a1.value)