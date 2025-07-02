'''
读取excel文件
'''
import xlrd

wb = xlrd.open_workbook('无标题.xls')
sheetnames = wb.sheet_names()
print(sheetnames)
sheet = wb.sheet_by_name(sheetnames[0])
print(sheet.nrows, sheet.ncols)

for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        value = sheet.cell(row, col).value
        if row > 0:
            if col == 0:
                value = xlrd.xldate_as_tuple(value, 0)
                value = f'{value[0]}年{value[1]:>02d}月{value[2]:>02d}日'
            else:
                value = f'{value:.2f}'
        print(value, end='\t')
    print()