import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import ssl

def scrape():
    news_url="https://www.google.com/alerts/feeds/15698275311523445965/7583103859544372464"
    ssl._create_default_https_context = ssl._create_unverified_context
    Client=urlopen(news_url)
    xml_page=Client.read()
    Client.close()

    soup_page=soup(xml_page,"xml")
    news_list=soup_page.findAll("entry")
    data = []
    for news in news_list:
        title = news.title.text
        link = news.link['href']
        date = news.published.text
        data.append({ "title": title, "link": link, "date": date })

    #print (data)
    return data
    # Print news title, url and publish date
    # for title in news_list:
    #     print(news.title.text)
    #     print(news.link.text)
    #     print(news.pubDate.text)
    #     print("-"*60)
