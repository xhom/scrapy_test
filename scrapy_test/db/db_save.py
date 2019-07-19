# coding=UTF-8

import sys
import pymysql

pymysql.install_as_MySQLdb() # 用pymysql替代MySQLdb

reload(sys)
sys.setdefaultencoding("gbk") # 设置编码

class DBSave:
    ip = "localhost"
    user = "test"
    password = "123456"
    dbName = "test"

    def __init__(self, table_name, maxLength=512):
        self.db = None
        self.cursor = None
        self.tableCreated = False
        self.table_name = table_name
        self.maxLength = maxLength
        self.init_conn()

    def init_conn(self):
        if not self.cursor:
            self.db = pymysql.connect(self.ip, self.user, self.password, self.dbName, charset='utf8')
            self.cursor = self.db.cursor()

    def create_table(self,item):
        self.cursor.execute("DROP TABLE IF EXISTS "+self.table_name)
        create_table_sql = "CREATE TABLE "+self.table_name+"("
        create_table_sql += "id BIGINT(11) PRIMARY KEY AUTO_INCREMENT,"
        for field in item:
            create_table_sql += (field + " VARCHAR("+str(self.maxLength)+"),")
        create_table_sql = create_table_sql[0:len(create_table_sql)-1]
        create_table_sql += ")"

        print "CREATE TABLE SQL：",create_table_sql
        self.cursor.execute(create_table_sql)

    def insert(self,item):
        if self.tableCreated == False:
            self.create_table(item)
            self.tableCreated = True
        insert_sql = "INSERT INTO "+self.table_name+"("
        keys, values = "", ""
        for key in item:
            keys += key+','
            values += '"'+item[key]+'",'
        keys = keys[0:len(keys)-1]
        values = values[0:len(values)-1]
        insert_sql += keys+") VALUES("
        insert_sql += values+")"

        try:
            print "INSERT SQL:", insert_sql
            self.cursor.execute(insert_sql)
            self.db.commit()  # 提交
            print 'INSERT SUCCESS.'
        except Exception, e:
            self.db.rollback()  # 回滚
            print 'INSERT FAILED AND ROLLBACK: ', e

    def close_conn(self):
        # 关闭游标&数据库
        self.cursor.close()
        self.db.close()