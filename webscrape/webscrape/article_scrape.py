import requests
from bs4 import BeautifulSoup
def content_scrap(url,*kwargs):
    Data=[]
    # url is the target we want to open
    
    #open with GET method
    resp=requests.get(url)
    
    #http_respone 200 means OK status
    if resp.status_code==200:
    
        # we need a parser,Python built-in HTML parser is enough .
        soup=BeautifulSoup(resp.text,'html.parser')	
    
        # l is the list which contains all the text i.e news
        if len(kwargs)==3:
            l=soup.find_all(kwargs[0],{kwargs[1]:kwargs[2]})
        else:
            l=soup.find_all(kwargs[0])
        for i in range(len(l)):
          Data.append((l[i].text))
        return Data
    else:
        print("Status code return : ",str(resp.status_code))
        return 0
