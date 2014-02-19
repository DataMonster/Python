import gen_key
import sys
comargs = sys.argv
outName = comargs[1]
keyName = comargs[2]
Message = comargs[3]

def encode(text):
    if type(text) == str and text.isalpha():
        text=text.upper()
        message = list(text)
        length = len(message)
        n = gen_key.loadKey(keyName)
        Result = []
        for item in message:
            result = []
            times = n[item]
            for t in range(0,times):
                result.append('a')
            Result.append(result)
        return Result
    else: return 'please enter a text message with all alphabets'

def saveMessage(mes,fileN):
    import pickle
    f1 = file(fileN+'.pkl', 'wb')
    pickle.dump(mes, f1, True)
    f1.close 

def loadMessage(fileN):
    import pickle
    f2 = file(fileN+'.pkl', 'rb')
    mes = pickle.load(f2)
    f2.close
    return mes

def Test():
    print '\n'
    print ' The key of this encode: ', gen_key.loadKey(keyName)
    print ' Encode the message (', Message,') ', encode(Message)
    mes = encode(Message)
    saveMessage(mes,outName)
    print ' View the information in the file -', outName,'- which save the encoded message: '
    print ' With pickle.load method'
    print loadMessage(outName)
    print '\n'

if __name__ == '__main__':
    Test()
   
