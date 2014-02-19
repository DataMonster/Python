import crawl
import sys
comargs = sys.argv
inUrl = comargs[1]
depth = int(comargs[2])

def startswith(str0,prefix):
    import re
    length = len(prefix)
    s = str0[0:length]
    temp = re.compile(s)
    result =temp.match(prefix)
    if result and result.end() == length:
        return True
    else:
        return False

def is_alpha(s):
    import re
    if s.__contains__("\\"):
        return False
    else:
        alpha = re.compile("[A-z]+")
        result = alpha.search(s)
        
        if not result or result.end() != len(s):
            return False
        else:
            return True

def is_alnum(s):
    import re    
    length = len(s)
    if length != 0:
        matchlist = list(s)
        count = 0
        alpha = re.compile("[a-zA-Z0-9]")
        for item in matchlist:
            if alpha.search(item):
                count = count +1
        if count == length:
            return True
        else:
            return False
    else:
        return False

def is_in(s1,s2):
    import re
    p1 = re.compile(s2)
    if p1.search(s1):
        return True
    else:
        return False

def Test():
    TITLE, URL = crawl.crawl(inUrl,depth)
    for i in range(0,len(URL)):
        print "Title: ", TITLE[i], "\t", "URL: ", URL[i]
        print ' Check the correctness of this Title:'
        print '  is_alpha(TITLE[i]) and TITLE[i].isalpha(): '
        print '  ',is_alpha(TITLE[i]),TITLE[i].isalpha()
        print '  is_alnum(TITLE[i]) and TITLE[i].isalnum(): '
        print '  ',is_alnum(TITLE[i]), TITLE[i].isalnum()
        print '  startswith(TITLE[i],TITLE[i]) and TITLE[i].startswith(TITLE[i]):'
        print '  ',startswith(TITLE[i],TITLE[i]), TITLE[i].startswith(TITLE[i])
        print '  is_in(TITLE[i],TITLE[i]) and TITLE[i] in TITLE[i]'
        print '  ',is_in(TITLE[i],TITLE[i]), TITLE[i] in TITLE[i]
        print '\n'
    
    
if __name__ == '__main__':
    Test()
