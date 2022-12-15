import requests
from bs4 import BeautifulSoup
coun=0
list_headlink=[]
list_summary=[]
list_headline=[]
coun_line=0
coun_link=0
coun_s=0
for i in range(1,18):

    website=requests.get(f"https://coreyms.com/page/{i}").content
    soup =BeautifulSoup(website,'html.parser')

    articles=soup.find_all('iframe',{'class':'youtube-player'})
    for article in articles :
        headlink = article.attrs['src']
        #print(headlink)
        list_headlink.append(headlink)

        coun_link += 1

    articles=soup.find_all('a',{'class':'entry-title-link'})
    for article in articles :
        headline = article.text
        list_headline.append(headline)
        coun_line += 1

    articles=soup.find_all('div',{'class':'entry-content'})
    for article in articles :
        summary = article.p.text
        list_summary.append(summary)
        coun_s+=1


    for x in range(len(list_headlink)):
        print(list_headline[x])
        print(" ")
        print(list_summary[x])
        print(" ")
        print(list_headlink[x])
        print(" ")
        print(" ")
        print(" ")


