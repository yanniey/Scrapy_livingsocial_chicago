# -*- coding: utf-8 -*-

# Scrapy settings for my_scrapper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'livingsocial'

SPIDER_MODULES = ['scraper_app.spiders']

ITEM_PIPELINES = ['scraper_app.pipelines.LivingSocialPipeline'] 
# from pipeline.py

DATABASE = {
	'drivername': 'postgres',
	'host': 'localhost',
	'port': '5432',
	'username': 'Anyi',
	'password': '',
	'database': 'scrape'   
	# this is what we created in Postgres shell with `postgres=# create database scrape;`
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'my_scrapper (+http://www.yourdomain.com)'
