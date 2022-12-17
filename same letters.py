a=["mahalakshmi"]
b=["sreekanya"]
def fun (a,b):
    i=0
    c=[]
    while i<len(a):
        if a[i] in b:
            c.append (a[i])
        i=i+1
    print(c)
fun("mahalakshmi","sreekanya")