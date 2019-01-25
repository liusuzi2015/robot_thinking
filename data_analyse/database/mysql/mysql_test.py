import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="1234",  # 数据库密码
    port = 3207,
    database = 'test',
    charset = 'utf8'
)

print(mydb)
