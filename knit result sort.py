import urllib2
from bs4 import BeautifulSoup
sc=[]
t=int(raw_input('number of tests:>>'))
while(t>0):
    class stud(object):
        roll=1
        score=0
        name='a'
        checked=0
    stude=[]
    ind=0
    inpute=raw_input('roll number range>>').strip()
    inpute2=inpute.split()
    l=int(inpute2[0])
    r=int(inpute2[1])
    print 'getting data for given range..'
    for j in range(l,r+1,1):
        if j==16163:
            continue
        elif j in range(13645,14100):
            continue
        elif j in range(14652,15100):
            continue
        elif j in range(15658,16100):
            continue
        link='http://knit.ac.in/coe/ODD_2016/odx51fsp741g.asp?rollno='+str(j)
        page=urllib2.urlopen(link)
        soup=BeautifulSoup(page,'html.parser')
        string=[]
        td=soup.find_all("td",width="50%")
        for item in td:
            string.append(item.get_text().strip())
        if len(string)==0:
            continue
        stude.append(stud())
        stude[ind].roll=j
        stude[ind].name=str(string[1])
        table=soup.find_all("table")
        tbody=[]
        for item in table:
            tbody.append(item.find_all('td'))
        td=[]
        for i in range(len(tbody)):
            for item in tbody[i]:
                td.append(item.get_text().strip())      
        score=str(td[len(td)-3:len(td)-2])
        sc.append(int(score[3:6]))
        stude[ind].score=int(score[3:6])
        print j,stude[ind].name,'\t\t\t',stude[ind].score
        ind=ind+1
    print 'sorting.....'
    sc.sort(reverse=True)
    print 'getting rank...'
    i=1;
    for item in sc:
        for ind in range(0,len(stude)):
            if stude[ind].score==item and stude[ind].checked==0:
                stude[ind].checked=1
                print i,stude[ind].roll,stude[ind].name,'\t\t\t',stude[ind].score
                i=i+1
    t=t-1        
