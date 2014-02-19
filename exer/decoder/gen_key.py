import sys
comargs = sys.argv
fileName = comargs[1]

class Key(dict):
    def __init__ (self):
        import random
        self.numList = []
        while len(self.numList) <26:
            num = random.randint(0,26)
            if num not in self.numList:
                self.numList.append(num)
        self.K = {}
        for i in range(65,91):
            item = i-65
            keys = chr(i)
            self.K[keys] = self.numList[item]

def saveKey(n):
    import pickle
    f1 = file(fileName, 'wb')
    pickle.dump(n, f1, True)
    f1.close 

def loadKey(File):
    import pickle
    f2 = file(File, 'rb')
    n = pickle.load(f2)
    f2.close
    return n
    
def main():
    n = Key()
    saveKey(n.K)

def Test():
    print 'These are obtained from',comargs[1],'after running all necessary steps: '
    main()
    print loadKey(fileName)

if __name__ == '__main__':
    Test()

