import proxy_module

def main():
    import urllib2
    #page = proxy_module.main("http://www.hindilinks4u.net/")
    page = urllib2.urlopen("http://www.hindilinks4u.net/")
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page)
    tag_ul = soup.find_all("ul", attrs={"class":"xoxo blogroll"})
    soup = BeautifulSoup(str(tag_ul[2]))
    ml_mn = soup.find_all("a")
    import re
    start_urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', str(ml_mn).strip("[]"))
    try:
        f = open("page1.csv","a+")
        html  = f.read()
        start_urls = list(set(start_urls) - set(html.replace(' ','').replace("\n",'').split(",")))
        f.close()
    except:
        pass

    f =  open("page1.csv","a+")
    print >> f, str(start_urls).strip("[]").replace("'",'')
    print start_urls
    f.close()





if __name__=="__main__":
    main()
