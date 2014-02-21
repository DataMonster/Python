def zip(*arg):
    Result = []
    Check = 1
    #check if every item in arg has the same length
    for i in arg:
        if len(i) != len(arg[0]):
            print 'please make sure enter all items with the same length'
            Check = 0
            break
    while (Check):
        for j in range(0,len(arg[0])):
            result = ()
            for item in arg:
                result = result + (item[j],)
            Result.append(result)
        Check = 0
    return Result

def unzip(x):
    Length = len(x[0])
    result = ()
    LIST = []
    for i in range(0,len(x[0])):
        LIST.append([],)
    for item in x:
        for j in range(0,len(LIST)):
            LIST[j].append(item[j])
    for k in LIST:
        result = result + (k,)
    return result      

def Test():
    print '#1 test: '
    print ' zip([1,1,1],[2,2,2],[3,3,3],[4,4,4]) -->', zip([1,1,1],[2,2,2],[3,3,3],[4,4,4])
    print '\n'
    print ' unzip([(1,2,3,4,5),(2,3,4,5,6),(3,4,5,6,7)]) -->', unzip([(1,2,3,4,5),(2,3,4,5,6),(3,4,5,6,7)])
    print '\n'
    print '#2 test: unzip(zip([100,200,300],[200,300,400],[0,0,0]))'
    print unzip(zip([100,200,300],[200,300,400], [0,0,0]))
    print '\n'

if __name__ == '__main__':
    Test()


