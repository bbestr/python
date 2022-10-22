from pymysql import connect

conn = connect(host='localhost',port=3306,user='root',passwd='123456',database='biyesheji',charset='utf8')

cur = conn.cursor()

class JD:
    def __init__(self):
        self.conn = connect(host='localhost', port=3306, user='root', passwd='123456', database='biyesheji', charset='utf8')

        self.cur = self.conn.cursor()
    def __del__(self):
        self.conn.close()
        self.cur.close()
    def show_type(self):
        sql = "select distinct(cate_name) from goods;"
        self.shuchu(sql)
    def shuchu(self,sql):
        cur.execute(sql)
        for i in cur.fetchall():
            print(i)
    def show_brand(self):

        sql = "select distinct(brand_name) from goods;"
        self.shuchu(sql)
    def show_all(self):
        sql = "select * from goods;"
        self.shuchu(sql)
    def search(self):
        num = input("输入查询的商品品牌")

        sql = "select * from goods where brand_name= '%s'" % num
        self.shuchu(sql)
    def insert(self):
        sql = "insert into goods values(27,'250','平板','亚索',9999,1,0)"
        self.cur.execute(sql)
        self.conn.commit()
    def run(self):
        while True:
            print("京东商城")
            print("1.所有商品信息")
            print("2.所有商品分类")
            print("3.所有商品品牌分类")
            print("4.查询指定商品信息")
            num = int(input("输入你的操作"))
            if num == 1:
                self.show_all()
            elif num == 2:
                self.show_type()
            elif num == 3:
                self.show_brand()
            elif num == 4:
                self.search()
            else:
                print("输入有误重新输入")
if __name__ == '__main__':
    jd = JD()
    jd.run()

    jd.__del__()




