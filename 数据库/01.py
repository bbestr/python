from pymysql import *

conn = connect(host='localhost',port=3306,user='root',passwd='123456',database='biyesheji',charset='utf8')

cur = conn.cursor()

cur.execute("select * from goods;")

print(cur.fetchall())
