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

l1=[1,2,3,4,5,6]
l2=[9,2,3,4,5,6]
union=list(set().union(l1,l2))
print("the union of two list" , union)


n=input("enter the numbers :")
l=input("enter the numbers :")
union=list(set().union(n,l))
print("the union of two list", union)




l1 = []
num1 = int(input('Enter size of list 1: '))
for n in range(num1):
    numbers1 = int(input('Enter any number:'))
    l1.append(numbers1)
 
l2 = []
num2 = int(input('Enter size of list 2:'))
for n in range(num2):
    numbers2 = int(input('Enter any number:'))
    l2.append(numbers2)
 
union = list(set().union(l1,l2))
 
print('The Union of two lists is:',union)
