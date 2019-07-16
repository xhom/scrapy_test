# coding=UTF-8

import pymysql
pymysql.install_as_MySQLdb() # 用pymysql替代MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class DBSave:

    def __init__(self, table_name, maxLength=512):
        self.cursor = None
        self.db = None
        self.tableCreated = False
        self.table_name = table_name
        self.maxLength = maxLength
        self.init_conn()

    def init_conn(self):
        if not self.cursor:
            self.db = pymysql.connect("localhost", "test", "123456", "test", charset='utf8')
            self.cursor = self.db.cursor()

    def create_table(self,item):
        self.cursor.execute("DROP TABLE IF EXISTS "+self.table_name)
        create_table_sql = "CREATE TABLE "+self.table_name+"("
        create_table_sql += "id BIGINT(11) PRIMARY KEY AUTO_INCREMENT,"
        for field in item:
            create_table_sql += (field + " VARCHAR("+str(self.maxLength)+"),")
        create_table_sql = create_table_sql[0:len(create_table_sql)-1]
        create_table_sql += ")"

        print "建表sql：",create_table_sql
        self.cursor.execute(create_table_sql)

    def insert(self,item):
        if self.tableCreated == False:
            self.create_table(item)
            self.tableCreated = True
        insert_sql = "INSERT INTO "+self.table_name+"("
        keys, values = "", ""
        for key in item:
            keys += key+','
            values += '"'+str(item[key])+'",'
        keys = keys[0:len(keys)-1]
        values = values[0:len(values)-1]
        insert_sql += keys+") VALUES("
        insert_sql += values+")"

        try:
            print "写入sql:", insert_sql
            self.cursor.execute(insert_sql)
            self.db.commit()  # 提交
            print '数据写入成功'
        except Exception, e:
            self.db.rollback()  # 回滚
            print '数据写入失败,已回滚', e

    def close_conn(self):
        # 关闭游标&数据库
        self.cursor.close()
        self.db.close()