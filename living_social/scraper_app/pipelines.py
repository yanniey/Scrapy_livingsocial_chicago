# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker 
# to create the connection
from models import Deals, db_connect, create_deals_table


class LivingSocialPipeline(object):
	"For storing scraped items in database"
	def __init__(self):
		"""
		Initializes the class by defining engine, deals table and connecting to db with defined engine.
		Creates deals table.
		"""
		engine = db_connect()
		create_deals_table(engine)
		self.Session = sessionmaker(bind=engine)

	def process_item(self, item, spider):
		""" 
		Save deals in the database.
		This method is called for every item pipeline component.
		"""
		session = self.Session()
		deal = Deals(**item) 
		#Deals model

		try:
			session.add(deal) 
			# add `deal` to database
			session.commit() 
			# save the addition
		except:
			session.rollback() 
			# undo
			raise
		finally:
			session.close()

		return item

