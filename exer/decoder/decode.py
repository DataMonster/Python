import gen_key
import sys
comargs = sys.argv
inName = comargs[1]
keyName = comargs[2]

def decode(text):
    if type(text) == list:
        Re = []
        result = ''
        keys = gen_key.loadKey(keyName)
        for i in text:
            num = len(i)
            for alpha,number in keys.iteritems():
                if num == number:
                    Re.append(alpha)
        for item in Re:
            result = result + item
        return result
    else: 'please enter a valid text file'

def loadMessage(fileN):
    import pickle
    f2 = file(fileN+'.pkl', 'rb')
    mes = pickle.load(f2)
    f2.close
    return mes

def Test():
    print '\n'
    print ' The key of this encode: ', gen_key.loadKey(keyName)
    mess = loadMessage(inName)
    print ' Load the encoded text from file -', inName, '- :', mess

    print ' The decoded message is : '
    print decode(mess)
    print '\n'

if __name__ == '__main__':
    Test()

