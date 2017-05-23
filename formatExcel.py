import openpyxl
from numbers import Number

wb = openpyxl.load_workbook('similarity_copy1.xlsx')
sheet = wb.get_sheet_by_name('ClassSimSparse')

for row in sheet.iter_rows():
	for cell in row:
		if isinstance(cell.value, Number):
			if cell.value < 0.1:
				print("here")
				cell.value = 0


wb.save('similarity.xlsx')
