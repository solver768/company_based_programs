s=str()#''
#strings
''' class string{
    str(){
    pass
    }
}
'''
s=input()
#using character
for c in s:
  print(c,end='')
print()
#using location
for i in range(0,len(s),1):
  print(s[i],end='')
#output
"""
Hello everyone
Hello everyone
Hello everyone
"""

#string object is immutable

#converting string to list and list to string
s=input()#input=hi!
l=list(s)
l[1]='a'
print(*s,sep='')
#str_sep.join(iterable)
print(''.join(l))
#output
"""
hi!
hi!
ha!
"""
#converting sentence to list and list to sentence
s='python is a programming language'#input().split()
s=s.split()
print(' '.join(s))
#output
#python is a programming language


#question
"""
A company provides data encryption to its clients' data. The data sent over the network is in the form of a string 
The encryption algorithm used by the company adds a key value in the ASCII value of each character of the data string
and forms the encrypted string This string is then sent over the network to provide security.
"""
#concept of ascii
"""
ch=input()
print(ord(ch))#print ascii value
#ouput:
e
101

print(chr(ord(ch)))#print character of ascii value
#output
d
100
d

#wap to encrpyt the string by using key value
"""
n=int(input("Key:"))
s=input("data:")
for ch in s:
  print(chr(ord(ch)+n),end=" ")

#output
'''
Key:5
data:Hello John!
Mjqqt%Otms&
'''
"""
The games developer,"GamingFun",has decided to develop a word game.In the first round, the game screen will display 
multiple words. The length of the starting word of the next round will display multiple words. The length of the starting
word of the next round will be equal to the last word of the previous round. To design the game, the developers need to
know the length of the last word in the previous round.
input:
the input consists of a string  with spaces separated words representing the words displayed on the game screen.
ouput:
Print an interger value representing the length of the last word of the previous round.
"""
s=input()
s=s.split()
w=s[-1]
print(len(w))

#output
"""
Hello Hi welcome bye
3
"""

#reverse a string
s="python"
print(s[::-1])
print(*reversed(s),sep="")
#ouput:
"""
nohtyp
nohtyp
"""

      
#wap to reverse a string without changing positions of words
s='python is easy'
s=s.split()
for ch in s:
  print(ch[::-1],end='')
#output:nohtypsiysae  

"""
string case operation:
upper(),lower(),title(),capitalize(),swapcase()
case checking
isupper() islower() istitle() isspace()
character checking
isalpha(),isdigit(),isnumeric(),isalnum()




