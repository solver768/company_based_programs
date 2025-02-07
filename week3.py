#WAP to print maximum value in list without using inbuilt function 
import sys
def maxValue(l):
  m=-sys.maxsize-1
  for i in range(len(l)):
    if l[i]>m:
      mx1=l[i]
      return m
lst=[-2,4,-5]
#lst=list(map(int,input("Give your list:").split())
print(maxValue(lst))

#output:-2
#AMAZON WAP to print leaders of an array 
def mx(l):
  m=l[-1]
  print(m,end=' ')#1
  for i in range(len(l)-2,-1,-1):
    if l[i]>m:
      m=l[i]
      print(m,end=' ')
l=[8,3,51]
mx(l)
#output:1 5 8 
#WAP TO print second maximium value in an array
import sys
def maxValue(l):
	mx1,max2=-sys.maxsize-1,-sys.maxsize-1
	for i in range(len(l)):
		if l[i]>mx1:
			mx2=mx1
			mx1=l[i]
		elif l[i]>mx2 and l[i]<mx1:
			mx2=l[i]
	print(mx1,mx2)
lst=[-2,4,-5]
#lst=list(map(int,input("Give your list:").split())
maxValue(lst)
#output:4 -2
#WIPRO WAP to print number of values greater than element
def maxValue(l,n):
	for i in range(n):
		c=0
		for j in range(i+1,n):
			if(l[i]<l[j]):
				c+=1
		print(c,end=' ')
#n=int(input())
n=5
lst=[2,3,4,4,5]
#lst=list(map(int,input("Give your list:").split())
maxValue(lst,n)
#output:4 3 1 1 0 
max difference b/w adjacent values 
def maxValue(l):
	mx1,max2=-sys.maxsize-1,-sys.maxsize-1
	for i in range(len(l)):
    if abs(l[i]-l[i+1])>m:
      m=abs(l[i]-l[i+1])
	print(m)
lst=[-2,4,-5]
#lst=list(map(int,input("Give your list:").split())
maxValue(lst)
