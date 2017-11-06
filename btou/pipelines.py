# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

def dbhandle():
      conn = pymysql.connect(
        host='192.168.113.2',
        user='crawl',
        db='crawl',
        password='kumanxuan123!',
        charset='utf8',
        #use_unicode=False
        )
      return conn



class BtouPipeline(object):

    #def __init__(self,dpool):
    #  self.dpool = dpool


    #def from_settings(cls,settings):
    # dbparams=dict(
    #        host=settings['MYSQL_HOST'],
    #        db=settings['MYSQL_DBNAME'],
    #        user=settings['MYSQL_USER'],
    #        passwd=settings['MYSQL_PASSWD'],
    #        charset='utf8',
    #        cursorclass=MySQLdb.cursors.DictCursor,
    #        use_unicode=False,
    #    )
    # dbpool=adbapi.ConnectionPool('MySQLdb',**dbparams)
    # return cls(dbpool)

    def process_item(self, item, spider):
        #query=self.dbpool.runInteraction(self._conditional_insert,item)
        #query.addErrback(self._handle_error,item,spider)
        dbObject = dbhandle()
	cursor = dbObject.cursor()
	sql = 'insert into page(title,keyword,tid,h2) values(%s,%s,1,%s)'
	try:
	 #pass
	 cursor.execute(sql,(item['title'],item['h1'],item['h2']))
	 dbObject.commit()
	except Exception,e:
	 print(e)
	dbObject.rollback()


	return item

