"""wap to print subsequences in given array""" 
from itertools import combinations 
l=[1,2,3]
n=len(l)
for i in range(1,n+1):
  for c in combinations(l,i):
    print(*c)
"""
output:
15
"""
"""
you are given a list with N elements and a number M from  that you have to find the good sequences possible.
A good sequences of intergers is a non-empty sequence such that the sum is divisible by M
output:
Number of good sequences are possible in the given array

"""
# good sequences sum is divisible by M
from itertools import combinations 
n,m=map(int,input().split())
l=list(map(int,input().split())
count=0
for i in range(1,n+1):
  for c in combinations(l,i):
    if(sum(c)%m==0:
      count+=1
print(count)
"""
input:
5 3
1 2 3 6 9
output:
15
"""

"""
Wap to read and print nested list values
"""
r,c=map(int,input().split())
l=[]
for i in range(r):
  l.append(list(map(int,input().split())))
for i in range(r):
  for j in range(c):
    print(l[i][j])
  print()
"""
input:
2 3
1 2 3
4 5 6
output:
1 2 3
4 5 6
"""
"""
Wap to print nested list values
"""
l=[[1,2,3],[4,5,6]]
for i in range(r):
  for j in range(c):
    print(l[i][j])
  print()
"""
output:
1 2 3
4 5 6
"""
"""
Wap to print water image of a matrix
"""
r,c=map(int,input().split())
l=[]
for i in range(r):
  l.append(list(map(int,input().split())))
for i in range(r-1,-1,-1):
  for j in range(l[i][j]):
    print(c)
  print()
"""
input:
2 3
1 2 3
4 5 6
output:
4 5 6
1 2 3 
"""
"""
Wap to print mirror image of a matrix
"""
r,c=map(int,input().split())
l=[]
for i in range(r):
  l.append(list(map(int,input().split())))
for i in range(r):
  for j in range(c-1,-1,-1):
    print(l[i][j])
  print()
"""
input:
2 3
1 2 3
4 5 6
output:
3 2 1 
6 5 4
"""

"""
Wap to print transpose of a matrix
"""
r,c=map(int,input().split())
l=[]
for i in range(r):
  l.append(list(map(int,input().split())))
for i in range(c):
  for j in range(r):
    print(l[j][i],end=" ")
  print()
