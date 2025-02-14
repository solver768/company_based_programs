#program to find all the subarrays in list
l=list(map(int,input("\enter the list of elements:").split()))
n=len(l)
for i in range(n):
  for j in range(i+1,n+1):
    print(*l[i:j])
'''
enter the list of elements: 1 2 3
1
1 2
1 2 3
2
2 3
3

'''

'''
subarrays-only continuous memory locations values
subsequences -both continuous and non continuous memory
location values 
'''
