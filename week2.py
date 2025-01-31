"""
Calculate and return the sum of difference of adjaacent positive list of numbers:
"""
n=int(input())
List=list(map(int,input().split()))
i=0
Sum=0
while(i<n-1):
    Sum+=abs(List[i]-List[i+1])
    i+=1
print(Sum)
"""
output:
5
10 12 14 13 10
8
"""
"""
TCS-WAP to print odd number of times occurence value in list
"""
def odd_occurence(l):
    res=0
    for ele in l:
        res=res^ele
    return res
n=int(input())
l=list(map(int,input().split()))
print(odd_occurence(l))
"""
output:
8
5 2 5 3 3 2 3
3
"""
"""
i-.wap  to seggegate even and odd values in an array with o(n) time complexity and o(1) constant space(order is not constraint)
i/p:1 2 3 4 5 6
o/p:2 4 6 1 3 5
"""
def segregate(l):
  s,e=0,len(l)-1
  while(s<e):
    if(l[s]%2==1):
      if(l[e]%2==0):
        l[s],l[e]=l[e],l[s]
        s+=1
        e-=1
      else:
        e-=1
    else:
      s+=1
  return l
l=list(map(int,input().split()))
print(seggregate(l))

"""
#WAP to check given array tyoe is even or odd or mixed 
i/p:2 4 6 8,
o/p:even
i/p:1 3 5 7,
o/p:odd
i/p:1 2 3 4
o/p:mixed

"""
def Check(l):
  o=e=0
  for x in l:
    if(x%2==0):
      e+=1
    else:
      o+=1
  if(e == len(l)):
    return "even"
  elif o==len(l) :
    return "odd"
  else:
    return "mixed"
l=list(map(int,input().split()))
print(Check(l))

