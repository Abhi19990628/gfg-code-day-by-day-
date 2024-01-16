# a=[]
# n=int(input("enter no "))
# for x in range (0, n):
#     element=int(input("number"))
#     a.append(element)
    
# temp=a[0]
# a[0]=a[n-1]
# a[n-1]=temp
# print("new list is")
# print(a)

a=[1,3,5,6,4]
temp=a[0]
a[0]=a[-1]
a[-1]=temp
print("new list is")
print(a)