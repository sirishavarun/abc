import pymysql
mysql = pymysql.connect(
    user='siri',
    password=1234,
    port='',
    database='mydatabase'
)
sql = mysql.cursor()
sql.execute()
