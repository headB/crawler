# -*- coding: utf-8 -*-
import pymysql

def conn():
  conn = pymysql.connect(
        host='192.168.113.2',
	db='crawl',
        user='crawl',
        password='kumanxuan123!',
        charset='utf8',
        #use_unicode=False,
        )
  return conn

crawlDB = conn()
DBcn = crawlDB.cursor()
DBcn.execute('select * from site')
result = DBcn.fetchall()
print(result)
DBcn.close()

