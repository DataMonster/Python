def Prime():
    n = input('please enter a positive number : ')

    list1 = range(2,n)
    
    def Check(x):
        def dev(y):
            return x%y > 0
        result = filter(dev, range(2,x))
        length = len(range(2,x))
        rlength = len(result)
        return int(rlength >= length)

    list2 = map(Check, list1)

    def Muti(x,y):
        return x*y
    list3 = map(Muti, list2, list1)

    def Return(x):
        return x !=0
    Re = filter(Return,list3)

    def Print(x):
        print x,
    print 'The primes list below', n, 'are : '       
    map (Print, Re)
    #print 'The primes list below', n, 'are : ', Result
        
def test():
    print '#1 test: please enter 200'
    Prime()
    print '\n'
    print '#2 test: please enter 100'
    Prime()
    print '\n'
    print '#3 test: please enter 20'
    Prime()
    print '\n'
    print '#4 test: please enter 2'
    Prime()
    print '\n'
    print '#5 test: plesae enter 1'
    Prime()
    print '\n'
    
    print 'test is over, all pass!'
    
if __name__ == '__main__':
    test()


    
