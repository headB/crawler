# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BtouPipeline(object):

    def __init__(self,dpool):
      self.dpool = dpool


    def from_settings(cls,settings):
     dbparams=dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=False,
        )
     dbpool=adbapi.ConnectionPool('MySQLdb',**dbparams)
     return cls(dbpool)



    def process_item(self, item, spider):
        query=self.dbpool.runInteraction(self._conditional_insert,item)
        query.addErrback(self._handle_error,item,spider)
        return item

    def _conditional_insert(self,tx,item):
        #print item['name']
        sql="insert into testpictures(name,url) values(%s,%s)"
        params=(item["name"],item["url"])
        tx.execute(sql,params)

    def _handle_error(self, failue, item, spider):
        print(failue)
