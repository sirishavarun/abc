import pymysql
mysql = pymysql.connect(
    user='siri',
    password=1234,
    port='',
    database='mydatabase'
)
table = mysql.cursor()
sql= mysql.execute(CREATE TABLE details(sno int AUTO INCREMENT PRIMARY KEY, name varchar(20), address varchar(20) ))
print(sql)
