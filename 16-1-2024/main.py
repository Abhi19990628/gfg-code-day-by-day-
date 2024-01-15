#basic qoution on python day by dya 

 # even odd num  ans a


num=int(input("enter the value "))
if num % 2==0:
     print("{0} is Even".format(num))
else:
     print("{0} is odd".format(num))
    
 # 1 to 10 num print and find odd and even 
 
 
for i in range (1 , 11):
    if i % 2==0:
       print(i ,"even" )
    else:
       print(i , "odd" )


#sum of num  two num 

num1 =int (input("enter first value :"))
num2 =int (input("enter second value :"))

print("sum of num1 and num2 is :", num1+num2)


 #postive num as input ;

num = int(input("enter the num is "))
if num >0 :
    print ("postive num :", num )
elif num == 0 :
    print ("zero num :", num )
else:
    print ("negtive num :", num)
    
    
# # # find the postive and negtive num as list 
    
list =[1,-1,0,2,3]
for i in list:
     if i >0:
         print("postive :", i)
     elif i==0:
        print("zero num :",i)
     else:
         print ("negtive num ",i)
        
        

# # # print the all num is odd 
        
        
lower=int(input("Enter the lower limit for the range:"))
upper=int(input("Enter the upper limit for the range:"))
for i in range(lower,upper+1):
    if(i%2!= 0):
        print(i)
        
# # # print the all num is even 

lower=int(input("enter lower value is :"))
upper=int(input("enter upper value is :"))
for i in range (lower,upper+1):
     if i % 2==0:
         print(i,"is even num ")
        
        
        
# #     # reverse no of list , string 
    
list = [1,3,4,5,6]
list_reversed=list[::-1]
print(list_reversed)


num_string=(input("enter the values of reversed no :"))
num_reversed = num_string[::-1]
print(num_reversed)

print (int(input("enter the value")[::-1]))


# for print 1 to 100 number not divied by 2 and 3

for i in range (1,100):
    if i % 2 !=0 and i % 3!=0:
        print(i)
        
lower=int(input("enter the value :"))
upper=int(input("enter the value :")) 
for i in range (lower , upper + 1):
    if (i % 7==0 and i % 5==0):
        print (i) 
        
        
lower=int(input("enter the value :"))
upper=int(input("enter the value :"))
n=int(input("enter the value of divison"))
for i in range (lower, upper+1):
    if i % n == 0:
        print(i)
        
        
# count the digit 
        
n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)


num = int(input("value of count"))
print(len(str(num)))

# make table for small childer 

n= int(input("enter the number of table which you want :"))
for i in range (1, 11):
    print( n, "x" , i , "=", n*i)
