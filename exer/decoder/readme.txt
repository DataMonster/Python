This is a simple decode and encode program.

#1. Use terminal, for gen_key:

zw2220:part3 zihanwang$ python gen_key.py 'key'
These are obtained from key after running all necessary steps: 
{'A': 18, 'C': 24, 'B': 4, 'E': 17, 'D': 1, 'G': 22, 'F': 25, 'I': 15, 'H': 12, 'K': 3, 'J': 11, 'M': 10, 'L': 6, 'O': 0, 'N': 8, 'Q': 23, 'P': 21, 'S': 26, 'R': 2, 'U': 20, 'T': 13, 'W': 9, 'V': 7, 'Y': 14, 'X': 5, 'Z': 16}

#2. For encode, use same key file 'key', test the message'iamatest':
zw2220:part3 zihanwang$ python encode.py 'out' 'key' 'iamatest'


 The key of this encode:  {'A': 18, 'C': 24, 'B': 4, 'E': 17, 'D': 1, 'G': 22, 'F': 25, 'I': 15, 'H': 12, 'K': 3, 'J': 11, 'M': 10, 'L': 6, 'O': 0, 'N': 8, 'Q': 23, 'P': 21, 'S': 26, 'R': 2, 'U': 20, 'T': 13, 'W': 9, 'V': 7, 'Y': 14, 'X': 5, 'Z': 16}
 Encode the message ( iamatest )  [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']]
 View the information in the file - out - which save the encoded message: 
 With pickle.load method
[['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']]


#3. For decode, use same key file 'key', test the text file 'out':
zw2220:part3 zihanwang$ python decode.py 'out' 'key'


 The key of this encode:  {'A': 18, 'C': 24, 'B': 4, 'E': 17, 'D': 1, 'G': 22, 'F': 25, 'I': 15, 'H': 12, 'K': 3, 'J': 11, 'M': 10, 'L': 6, 'O': 0, 'N': 8, 'Q': 23, 'P': 21, 'S': 26, 'R': 2, 'U': 20, 'T': 13, 'W': 9, 'V': 7, 'Y': 14, 'X': 5, 'Z': 16}
 Load the encoded text from file - out - : [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']]
 The decoded message is : 
IAMATEST


