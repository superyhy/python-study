'''
查询数据导出Excel
'''
import openpyxl
import pymysql

connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345', database='py_study',
                          charset='utf8mb4')

# 创建Excel文件
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = '字典表信息'
sheet.append(('id', '父编码', '名称', '编号', '值'))
try:
    with connect.cursor() as cursor:
        cursor.execute('select id,parent_code,name,code,value from dict')
        # 抓取数据
        row = cursor.fetchone()
        while row:
            sheet.append(row)
            row = cursor.fetchone()
    workbook.save('dict.xlsx')
except pymysql.MySQLError as error:
    print('导出异常', error)
finally:
    connect.close()