# def my(a):
#     i=0
#     sum=0
#     while i<len(a):
#         sum=sum+a[i]
#         i=i+1
#     print(sum)
# my([2,3,4,5,6])

# def my(a):
#     b=a[::-1]
# my("1234abcd")

# a=int(input("enter the num"))
# i=1
# while i<=10:
#     print(a,"*",i,"=",a*i)
#     i=i+1

# a=int(input("enter the num"))
# i=10
# while i>=1:
#     print(a,"*",i,"=",a*i)
#     i=i-1

# a=int(input("enter the num"))
# i=0
# while i<=10:
#     b=int(input("enter the num"))
#     print(a,"*",i,"=",a*i)
#     print(b,"*",i,"=",b*i)
# i=i+1

# i=0
# while i<=10:
#     if i==3:
#         continue
#     if i==5:
#         pass
#     if i==7:
#         break
#     i=i+1
    

# upper=(input("enter the storong password"))
# if upper>="A" and upper<="Z":
#     print("upper case")
#     lower=int(input("enter the storng password"))
#     if lower>="a" and lower<="z":
#         print("lower")
#         ch=input("enter the special charecter")
#         if ch=="@" or ch=="#" or ch=="&":
#             print("special charecter")
#             num=int(input("enter the num"))
#             if len(num)<=6:
#                 print(upper+lower+ch+str(num))
#                 print("strong password")
#             else:
#                 print("nothing")
#         else:
#             print("nothing")
#     else:
#         print("nothing")
# else:
#     print("nothing")

a=input("enter the name: ")
i=0
c=0
while i<len(a):
    c=c+1
    i=i+1
if c%2==0:
    print(c,"-","even")
else:
    print(c,"-","odd")
  
# n=int(input("enter the num"))
# a=n//10
# b=a%10
# if n!=b:
#     print(b)
# else:
#     print(n)

# print('''qwertyuio
# qwertyui
# werty
# qwerty''')