import sys
comargs = sys.argv
inUrl = comargs[1]
depth = int(comargs[2])

def getPage(url):
    import urllib2
    res=urllib2.urlopen(url)
    return res.read()

def getNextLink(page, URL):
    import re
    #p1 = re.compile('<a.*(\W.)*.*href=', re.IGNORECASE)
    pat = r"<a\s*href=\s*('(.*?)'|\"(.*?)\")"
    p1 = re.compile(pat,re.IGNORECASE)
    p2 = re.compile(r"(\.)*http",re.IGNORECASE)
    startL = p1.search(page)
    if not startL: 
        return None, 0
    start_link = startL.start()
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote].strip()

    startU = p2.search(url)
    if not startU:
        if url[0] == "/":
            if URL[-1] == "/":
                url=URL+url[1:]
            else: url = URL+url
        elif url[0].isalpha():
            if URL[-1] == "/":
                url=URL+url
            else: url = URL+"/"+url    
        else : return None, end_quote
    return url, end_quote

def getAll(page,URL):
    links = []
    while True:
        url,endpos = getNextLink(page,URL)
        if endpos!=0:
            if url:
                links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def getTitle(page):
    import re
    p0 = re.compile('<!--',re.IGNORECASE)
    p00 = re.compile('-->',re.IGNORECASE)
    startC = p0.search(page)
    endC = p00.search(page)
    while startC and endC:
        page = page[:startC.start()]+page[endC.end():]
        startC = p0.search(page)
        endC = p00.search(page)
        
    p1 = re.compile('<title>', re.IGNORECASE)
    startT = p1.search(page)
    p2 = re.compile('</title>',re.IGNORECASE)
    endT = p2.search(page)
    if not startT or not endT: 
        return 'No Title'
    start_link = startT.start()
    start_quote = page.find('>', start_link)
    Title = page[start_quote + 1:endT.start()]
    return Title.strip()

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def crawlResult(seed,d):
    count = 0
    tocrawl = [seed]       
    crawled = []                       
    while tocrawl and count < d:
        newcrawl = []
        for Url in tocrawl:
            if Url not in crawled:
                try:
                    content = getPage(Url)
                    Links = getAll(content,Url)
                    union(newcrawl,Links)
                    crawled.append(Url)
                except: pass
        tocrawl = newcrawl
        count = count+1
    return crawled, tocrawl

def crawl(seed,d):
    count = 0
    tocrawl = [seed]        
    crawled = []
    TITLE = []
    URL = []
    while tocrawl and count < d:
        newcrawl = []
        for Url in tocrawl:
            if Url not in crawled:
                try:
                    content = getPage(Url)
                    Links = getAll(content,Url)
                    Title = getTitle(content)
                    union(newcrawl,Links)
                    crawled.append(Url)
                    TITLE.append(Title)
                    URL.append(Url)
                    #print "Title: ",Title, "\t", "URL: " ,Url
                except: pass
        tocrawl = newcrawl
        count = count+1
    return TITLE, URL        

def Test():
    TITLE, URL = crawl(inUrl,depth)
    for i in range(0,len(URL)):
        print "Title: ", TITLE[i], "\t", "URL: ", URL[i]

if __name__ == '__main__':
    Test()
