# largest value in  list 

list = [1,24,27,29,55,2,88,99]
list.sort()
print(list[-1],list[-2],list[-3])


#secound method 

list=(input("enter ther number is "))
print("largest number is :",max(list))

#third method is

list=[]
n=int(input("enter no of element :"))
for i in range (1 , n+1):
    list1=int(input("enter the num :"))
    list.append(list1)
list.sort()
print("largest element :" ,list[-1])

#next method of find the largest value 

list=[]
n=int(input("enter no of element :"))
for i in range (1 , n+1):
    list1=int(input("enter the num :"))
    list.append(list1)
print("largest element :" ,max(list))

# reversed list as input 

list=[]
n=int(input("enter no of element :"))
for i in range (1 , n+1):
    list1=int(input("enter the num :"))
    list.append(list1)
list.sort()
print("largest element :" ,list[:: -1])


# avrege num of list :


n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))


# Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List
n=int(input("enter the value of element ti be in list"))
b=[]
for i in range (0,n):
    a=int(input("enter the value :"))
    b.append(a)
sum1=0
sum2=0
sum3=0
for j in b:
    if (j>0):
       if(j%2==0):
           sum1=sum1+j
           print("sum of all postive even no :", sum1)   
       else:
           sum2=sum2+j
           print("sum of all postive odd :", sum2) 
    else:
        sum3=sum3+j
        print("sum of all postive negtive no :", sum3)  


a=[1,2,3,444,56,78,-88,-12,];i=0
x=[i for i in a if i >0 and i%2==0]
y=[i for i in a if i >0 and i%2!=0]
z=[i for i in a if i<0]
print("even positive number sum :", sum(x))
print("odd positive number sum :" , sum(y))
print("negtive num   sum :" ,sum(z))


# sort num as using 2 list

a=[1,23,445,5678,5,43,22]
b=[23,-12,23,45,67,77,53]
c=a+b
c.sort()
print("sort num is ", c)

a=[]
n=int(input("enter no "))
for x in range (0, n):
     element=int(input("number"))
     a.append(element)
    
    
# Python Program to Swap the First and Last Element in a List
    
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("new list is")
print(a)

a=[1,3,5,6,4]
temp=a[0]
a[0]=a[-1]
a[-1]=temp
print("new list is")
print(a)
      
