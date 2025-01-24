"""
\\\\\\\\Date:24-01-2025\\\\\\\\\
Basic programs:
Reverse
Count
Sum and difference
Odd and even 
Max and Min
Sorting and Searching
Subarrays and subsequences
Roation
"""
#reverse
l=[3,1,2]
l.reverse()#chanes the original list
print(*l,sep=",")# here * unpacking operator
"""
output:
2,1,3
"""
l=[3,1,2]
print(*reversed(l))#it doesnot chage the original list
print(*l)
"""
ouput:
2 1 3
"""
#note:****similarly sort and sorted****
#1.WAP to print list of values in reverse order without using inbuilt function and slice operation.
l=[3,1,2]
for i in range(len(l)-1,-1,-1):
  print(l[i],end=' ')
"""
ouput:
2 1 3
"""
WAP to change list of values to reverse order 
l=[3,1,2,5,6,4]#[3,1,2,5,6]
n=len(l)
for i in range(n//2):
  l[i],l[n-i-1]=l[n-i-1],l[i]
print(*l)#6 5 2 1 3

"""
output:
4 6 5 2 1 3
"""
#Wipro
#1.
def bucketID(x):
  res=0
  while x!=0:
    res+=x%10
    x//=10
  return res
N=int(input())#no.of packets
l=list(map(int,input().split()))#nfiles with space 
for x in l:
  print(bucketID(x),end=' ')#bucket id  is the sum of the size of files
"""
output:
2
11 22
2 4 
"""
#In an online maths tutorial a student is given a list n numbers fromthis the student is requied to sum each element in the list such that the element int the output list will be equal to the first element until the ith element is first
def sm(l):
  res=0
  for i in l:
    res+=i
    print(res,end=' ')

n=int(input())
l=list(map(int,input().split()))#nfiles with space 

















  
