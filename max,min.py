# a=[1,2,3,4,5,6,7]
def fun(a,b):
    i=0
    max=0
    min=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        if a[i]<min:
            min=a[i]
        i=i+1
fun([1,2,3,4,5])