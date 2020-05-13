# -*- coding: utf-8 -*-

# !!! # Crawl responsibly by identifying yourself (and your website/e-mail) on the user-agent
USER_AGENT = 'TweetScraper'

# settings for spiders
BOT_NAME = 'TweetScraper'
LOG_LEVEL = 'INFO'
DOWNLOAD_HANDLERS = {'s3': None,} # from http://stackoverflow.com/a/31233576/2297751, TODO

SPIDER_MODULES = ['TweetScraper.spiders']
NEWSPIDER_MODULE = 'TweetScraper.spiders'
ITEM_PIPELINES = {
    'TweetScraper.pipelines.ProcessText': 50,
    # 'TweetScraper.pipelines.SaveToFilePipeline':100,
    'TweetScraper.pipelines.SaveToMongoPipeline':100, # replace `SaveToFilePipeline` with this to use MongoDB
    # 'TweetScraper.pipelines.SavetoMySQLPipeline':100, # replace `SaveToFilePipeline` with this to use MySQL
}

# DOWNLOAD_DELAY = 120

# settings for where to save data on disk
SAVE_TWEET_PATH = './Data/tweet/'
SAVE_USER_PATH = './Data/user/'

# settings for mongodb
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "COVIDTweets"        # database name to save the crawled data
MONGODB_TWEET_COLLECTION = "tweet" # collection name to save tweets
MONGODB_USER_COLLECTION = "user"   # collection name to save users

#settings for mysql
MYSQL_SERVER = "localhost"
MYSQL_DB     = "twitter"
MYSQL_TABLE  = "scraper" # the table will be created automatically
MYSQL_USER   = "root"        # MySQL user to use (should have INSERT access granted to the Database/Table
MYSQL_PWD    = "password"        # MySQL user's password
