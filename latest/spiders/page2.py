from scrapy.spider import BaseSpider
from scrapy.selector import Selector


import subprocess
import sys
import ast
from bs4 import BeautifulSoup
import re
import os.path

class DmozSpider(BaseSpider):
    name = "latest_page2"
    allowed_domains = ["hindilinks4u.net"]
    
    output = subprocess.check_output(['python', 'page1.py'])
    
    #start_urls = ast.literal_eval(output)
    #print start_urls, type(start_urls), len(start_urls) 
    #sys.exit()
    start_urls = ["http://www.hindilinks4u.net/2013/12/gori-tere-pyaar-mein-2013.html"]

    if os.path.isfile("page2_vidio.csv"):
        os.remove("page2_vidio.csv")

            
       
    def parse(self, response):
        self.sel = Selector(response)
        self.movie_link = response.url
        page = response.body
        soup = BeautifulSoup(page)
        data = soup.find_all("strong")
    
        for l in data:

            s = l.get_text().encode("ascii", "ignore")
            if re.search(r"Dailymotion", s):
                self.vidio_collecttion(l, "Dailymotion")     
                
            elif re.search(r"Youtube", s):
                self.vidio_collecttion(l, "yotube")




    def vidio_collecttion(self, l, typ):
    
        para = l.find_next("p")
        soup2 = BeautifulSoup(str(para))
        data2 = soup2.find_all("a")
        for m in data2:
            movie_link = str(self.movie_link)
            image_link = self.sel.xpath("/html/body/div/div[6]/div[3]/p/a/img")
            image_link = image_link.xpath('@src').extract()[0]
            movie_name = self.sel.xpath("/html/body/div/div[6]/h2/text()").extract()[0].encode("ascii","ignore")
            movie_name = unicode(str(movie_name), errors='ignore')
            watch = m.get_text().encode("ascii", "ignore")
            watch_link = m.get("href").encode("ascii", "ignore")
            f = open("page2.csv","a+")
            print >>f, ",".join([movie_link, image_link, movie_name, typ, watch , watch_link])
            f.close()
             
            
            f2 = open("page2_vidio.csv","a+")
            print >>f2, watch_link 
            f2.close()
            print movie_link, image_link, movie_name, typ, watch , watch_link
