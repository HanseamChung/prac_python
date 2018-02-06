arr=['A','B','C','D','E','F','G','H','I','J','K','L','M']
a= ['D', 'C', 'J', 'K', 'L']
b= ['B', 'E', 'H', 'L']
for i in range (0,4) :
    arr.remove(a[i])
    arr.remove(b[i])
print(arr)
