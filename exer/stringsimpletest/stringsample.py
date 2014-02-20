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
    print 'test #1 for is_alpha:'
    print ' str.isalpha(''): ',str.isalpha('')
    print ' is_alpha(''): ',is_alpha('')
    print ' str.isalpha("asdfd"): ',str.isalpha("asdfd")
    print ' is_alpha("asdfd"): ',is_alpha("asdfd")
    print ' str.isalpha("asd d"): ',str.isalpha("asd d")
    print ' is_alpha("asd d"): ',is_alpha("asd d")
    print r' str.isalpha("asd\d"): ',str.isalpha("asd\d")
    print r' is_alpha("asd\d"): ',is_alpha("asd\d")
    print ' str.isalpha("asd123"): ',str.isalpha("asd123")
    print ' is_alpha("asd123"): ',is_alpha("asd123")
    print ' str.isalpha("Ssdfd"): ',str.isalpha("Ssdfd")
    print ' is_alpha("Ssdfd"): ',is_alpha("Ssdfd")

    print '\n'
    print 'test #2 for is_alnum:'
    print ' str.isalnum(''): ',str.isalnum('')
    print ' is_alnum(''): ',is_alnum('')
    print ' str.isalnum("12345"): ',str.isalnum("12345")
    print ' is_alnum("12345"): ',is_alnum("12345")
    print ' str.isalnum("123 5"): ',str.isalnum("123 5")
    print ' is_alnum("123 5"): ',is_alnum("123 5")
    print r' str.isalnum("123\5"): ',str.isalnum("123\5")
    print r' is_alnum("123\5"): ',is_alnum("123\5")
    print ' str.isalnum("123d"):i ',str.isalnum("123d")
    print ' is_alnum("123d"): ',is_alnum("123d")
    print ' str.isalnum("123dD"): ',str.isalnum("123dD")
    print ' is_alnum("123dD"): ',is_alnum("123dD")
    print r' str.isalnum("123\dD"): ',str.isalnum("123\dD")
    print r' is_alnum("123\dD"): ',is_alnum("123\dD")

    print '\n'
    print 'test #3 for startswith'
    print ' "asdf".startswith("asd"): ',"asdf".startswith("asd")
    print ' startswith("asdf","asd"): ',startswith("asdf","asd")
    print ' "asdf".startswith("as1"): ',"asdf".startswith("as1")
    print ' startswith("asdf","as1"): ',startswith("asdf","as1")
    print r' "asdf".startswith("as\\1"): ',"asdf".startswith("as\1")
    print r' startswith("asdf","as\\1"): ',startswith("asdf","as\1")
    print r' "asd\\fdfg".startswith("asd\\fd"): ', "asd\fdfg".startswith("asd\fd")
    print r' startswith("asd\\fdfg","asd\\fd"): ', startswith("asd\fdfg","asd\fd")    

    print '\n'
    print 'test #4 for is_in'
    print ' "asdf" in "uasdffg" :', "asdf" in "uasdffg"
    print ' is_in("uasdffg", "asdf")', is_in("uasdffg", "asdf")
    print r' "\na1" in "ad\na1ff" : ',"\na1" in "ad\na1ff"
    print r' is_in("ad\nalff","\na1")', is_in("ad\na1ff","\na1")
    print ' "Asd" in "asdf" : ', "Asd" in "asdf"
    print ' is_in("asdf","Asd")', is_in("asdf","Asd")

if __name__ == '__main__':
    Test()
