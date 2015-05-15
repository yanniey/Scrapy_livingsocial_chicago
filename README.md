# Data scraping with Scrapy (Python)
### 5/14/15 

Use [Scrapy](http://scrapy.org/) to scrape deals info from [LivingSocial's Chicago page](https://www.livingsocial.com/cities/6-chicago) 

### Steps:

1. Config Scrappy spider to crawl and parse HTML
2. Set up Postgre database to store the parsed data
3. Create a pipeline to connect parsed data and dtabase with [SQLAlchemy](http://www.sqlalchemy.org/) ORM


### Result:

PSQL db: 

![postgres sql screenshot](https://github.com/yanniey/Scrapy_livingsocial_chicago/blob/master/PSQL%20screenshot.png?raw=true)

Json output:

![Json output](https://github.com/yanniey/Scrapy_livingsocial_chicago/blob/master/output.png?raw=true)
