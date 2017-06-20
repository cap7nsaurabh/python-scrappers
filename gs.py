import urllib2
from bs4 import BeautifulSoup
t=int(raw_input('number of test cas>>'))
while(t>0):
    query=raw_input("query>>")
    query=query.strip()
    query=query.replace(' ','+')
    print 'loading...'
    html="https://www.google.co.in/search?site=&source=hp&q="+query+"&gws_rd=ssl"
    req=urllib2.Request(html,headers={'User-Agent':'Mozilla\5.0'})
    soup=BeautifulSoup(urllib2.urlopen(req).read(),"html.parser")
    h=soup.find_all('h3')
    lists=[]
    for item in h:
        lists.append(item.find_all('a'))
    link=[]
    print 'getting links...'
    for i in range(0,len(lists)):
        for item in lists[i]:
            link.append(item.get('href'))

    for i in range(0,len(link)):
        print i+1,":",link[i][7:]
    print 'sorting and stripping...\n'
    cite=soup.find_all('cite')
    link=[]
    for item in cite:
        link.append(item.get_text())
    for i in range(0,len(link)):
        print i+1,":",link[i],'\n'
    t=t-1
    

