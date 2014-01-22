# Scrapy settings for latest project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'latest'

SPIDER_MODULES = ['latest.spiders']
NEWSPIDER_MODULE = 'latest.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'latest (+http://www.yourdomain.com)'


DOWNLOADER_MIDDLEWARES = {'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
                          'latest.proxy_middle.ProxyMiddleware': 120,
                         }
