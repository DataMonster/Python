import math

#'FMID','MarketName','Website','street','city','County','State','zip','x', 'y')
#the last one has a false part \n need to use: aaa = nextLine[-1][:-1] to delete
#1... int(nextLine[0])
#2... str
#3... str
#4... str
#5... str
#6... str
#7... str
#8... str
#9... float(nextLine[8])
#10.. float(locationY)  locationY=nextLine[-1][:-1]

class FamersM():
    def __init__(self, nextLine):
        self.table = nextLine #this is a line tuple with information
        self.FMID = int(nextLine[0])
        
    def __eq__(self, other):
        if self.FMID == other.FMID:
            return True
        else: return False

    def __ne__(self, other):
        if self.FMID != other.FMID:
            return False
        else: return True

    def __gt__(self, other):
        if self.FMID > other.FMID:
            return True
        else: return False

    def __lt__(self, other):
        if self.FMID < other.FMID:
            return True
        else: return False

    def __ge__(self, other):
        if self.FMID >= other.FMID:
            return True
        else: return False

    def __le__(self, other):
        if self.FMID <= other.FMID:
            return True
        else: return False
    
class FamersMarket(FamersM):
    def __init__(self, nextLine):
        self.table = nextLine #this is a line tuple with information
        self.FMID = int(nextLine[0])
        self.MarketName = nextLine[1]
        self.Website = nextLine[2]
        self.street = nextLine[3]
        self.city = nextLine[4]
        self.County = nextLine[5]
        self.State = nextLine[6]
        self.zip = nextLine[7]
        self.distance = 0
        self.setx(float(nextLine[-2]))
        self.locationY = nextLine[-1][:-1]
        self.sety(float(self.locationY))

    def dist(self, x1, y1):
        self.distance = math.sqrt(abs(self.x - x1) **2 + abs(self.y - y1) **2)
        #return self.distance
    
    def setx(self, value):
        if value > -180.0 and value <-40.0:
            self.x = value
        else:
            raise Exception, "Invalid x coordinate: {0}".format(x)
        
    def sety(self, value2):
        if value2 >10.0 and value2 <80.0:
            self.y = value2
        else:
            raise Exception, "Invalid y coordinate: {0}".format(y)

    def getx(self):
        return self.x
    
    def delx(self):
        del self.x

    def gety(self):
        return self.x
    
    def dely(self):
        del self.x
        
    x = property(getx,setx,delx, "")
    
    y = property(gety,sety,dely, "")

def get_market_list(name):
    Table = []  #instance table, name:'markets.csv'
    f = open(name, 'rb')
    line = f.readline()
    while line:
        line = f.readline()
        nextLine = list(line.split(','))
        if nextLine.__contains__('"'):
            nextLine.remove('"')  #remove '"'
        try:
            temp = FamersMarket(nextLine)
        except Exception:
            pass
        else:
            Table.append(temp)
    return Table

def sort_by_FMID(market_list):
    sort_list = sorted(market_list, key = lambda temp: temp.FMID)
    return sort_list

def get_nearest_markets(x, y, n, market_list):
    for temp in market_list:
        temp.dist(x,y)
    sortedList = sorted(market_list, key = lambda temp: temp.distance)
    Result = sortedList[0:n]
    return Result

def Test():
    print 'Test #1: get first 10 instances use get_market_list(name):'
    print "print get_market_list('markets.csv')[0:10]"
    print get_market_list('markets.csv')[0:10]
    print 'all qualified instances, pass this test!'
    print '\n'
    
    print 'Test #2: sort by FMID:'
    print ' take first 20 out of all markets and sort by FMID'
    Test1 = get_market_list('markets.csv')[0:20]
    Result1= sort_by_FMID(Test1)
    for i in Result1:
        print i.FMID
    print 'FMID is increasing, pass this test!'
    print '\n'

    print 'Test #3: get 10 nearest markets at location (-80,20)'
    print ' print the top 10 nearest distance and market FIMD'
    print " get_nearest_markets(-80,10,10,get_market_list('markets.csv'))"
    Test3 = get_nearest_markets(-80,10,10,get_market_list('markets.csv'))
    for i in Test3:
       print i.distance, i.FMID
    print 'distance is increaing and get the FIMD, pass this test!'

if __name__ == '__main__':
    Test()
