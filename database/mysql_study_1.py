import openpyxl
import pymysql

parent_code = input('父code：')
name = input('字典名称：')
code = input('字典代码：')
value = input('字典值：')

connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345', database='py_study',
                          charset='utf8mb4')

'''
单条数据插入
'''
try:
    # 获取游标对象
    with connect.cursor() as cursor:
        # 发送sql指令
        affected_row = cursor.execute('insert into dict(parent_code,name,code,value) values (%s,%s,%s,%s)',
                                      (parent_code, name, code, value))
        if affected_row == 1:
            print('新增一条数据')
    connect.commit()
except pymysql.MySQLError as error:
    connect.rollback()
    print('数据库异常', error)
finally:
    connect.close()
