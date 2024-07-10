##name = "sedhuPrakash"
##oc = "cse"
##clg = "smvec"
##m = "advisor"
##s_date = "24-04-2024"
##e_date = "28-04-2024"
##print("from:")
##print()
##print(name,oc,clg, sep="\n")
##print()
##
##print("to:")
##print()
##
##print(m, clg, sep="\n")
##print()
##
##print("Respected",m,",\nI am writing to request a leave of absence from college due to fever./nI would like to take leave from",s_date,"to",e_date,".")
##
##print("\t\t\tthanking you")

##a = int(input("Enter a number:"))
##b = int(input("enter a number"))
##
##print("sum = ",a+b)        
##print("sub =",a-b)
##print("mul =",a*b)
##print("div =",a/b)
##print("mod =",a%b)
##print("flo =",a//b)
##print("pow =",a**b)
    
##a = input("enter a string")
##b = input("enter a string")
##print(a==b)

##a = int(input("enter a number"))
##a += 1
##print("increment",a)
##a -= 1
##print("decrement",a)

##a= int(input("enter a number"))
##b= int(input("enter a number"))
##c= int(input("enter a number"))
##print(a and b or c and a)
##print(b or c and a)
##print(not a)

##age = int(input("enter your age"))
##a = 2024-age
##print(a)

##a = input("enter your name")
##b = float(input("cgpa"))
##c = input("dept")
##print("my name is",a,"\n my cgpa is",b,"\n My dept is",c)

##a= int(input("enter the quantity"))
##bill = int(a* 100)
##print(bill)

##max = 90
##age = int(input("enter your age"))
##remaining_years = max-age
##remaining_months = (max-age)*12
##remaining_weeks = (max-age)*52
##remaining_days = (max-age)*365
##print("You have",remaining_years,"years to live.")
##print("You have",remaining_months,"months to live.")
##print("You have",remaining_weeks,"weeks to live.")
##print("You have",remaining_days,"days to live.")

##weight = int(input("enter your weight: "))
##height = int(input("enter your height: "))
##BMI = weight/(height**2)
##print(BMI)
##--------------------------------------------------------------------------
#1.
##name =(input("Enter your name"))
##print("Hello",name)

#2.
##a = int(input("enter a number"))
##b = int(input("enter a number"))
##if a==b:
##    print("Both numbers are equal")
##elif a>b:
##    print("The first number is greater")
##else:
##    print("The second number is greater")

#3.
##a = int(input("Enter your age"))
##b = a*12
##print(b)

#4.
##l = int(input("Enter the length"))
##b = int(input("Enter the breadth"))
##area = l*b
##print(area)
##        

#5.
##a = int(input("Enter a number"))
##if a%2==0:
##    print("The number is even")
##else:
##    print("The number is odd")

#6.
##age = int(input("Enter your age"))
##if age>=18:
##    print("You are Eligible to vote")
##else:
##    print("You are Not Eligible to vote")

#7.
##a = input("Enter a number")
##b = input("Enter a number")
##a = int(a)
##b = int(b)
##print(a+b)

#8.
##name = input("Enter your Name")
##age = int(input("Enter your age"))
##print("Hello",name,"You are",age,"years old")

#9.
##num = int(input("Enter a  number"))
##if num==0:
##    print("Zero")
##elif num>0:
##    print("positive")
##else:
##    print("negative")

#10.
##num = int(input("Enter a number"))
##if(num%5==0):
##    print("It is divisible by 5")
##else:
##    print("It is not divisible by 5")
    
#11.
##a = int(input("Enter a number"))
##b = int(input("Enter a number"))
##print("sum of two numbers is ",a+b)
##print("product of two numbers is ",a*b)
##print("difference of two numbers is ",a-b)

#12.
##a = int(input("Enter a number"))
##if a%3==0 and a%5==0:
##    print("Multiple of both 5 and 3")
##else:
##    print("Not a multiple of both 5 and 3")

#13.
##r = float(input("Enter the radius"))
##area = float(r**2)
##print(area)

#15.
##age = int(input("Enter your age"))
##if age<=12:
##    print("child")
##elif age>12 and age<=19:
##    print("Teen")
##elif age>13 and age<=59:
##    print("Adult")
##elif age>59:
##    print("Senior")

#16.
##password = "abc123"
##a = input("Enter a password")
##if a==password:
##    print("Access Granted")
##else:
##    print("Access Denied")

#17.
##temp = float(input("Enter the temperature(in celsius) :"))
##fahrenheit = float(temp*9/5)+32
##print(fahrenheit,"fahrenheit")

#18.
##l1 = int(input("enter the length"))
##l2 = int(input("enter the length"))
##l3 = int(input("enter the length"))
##if l1==l2 and l2==l3 and l3==l1:
##    print("It's an equilateral")
##elif l1==l2 or l2==l3 or l3==l1:
##    print("It's an isosceles")
##elif l1!=l2 and l2!=l3 and l3!=l1:
##    print("it's an scalene")
    
#19.
##year = int(input("Enter the year"))
##if year%4==0:
##    print("Leap year")
##else:
##    print("Not a Leap year")


#Nested if

##a = int(input("Enter the mark"))
##if a>60:
##    if a>=90:
##        print("Grade A")
##    elif 80<=a<=89:
##        print("Grade B")
##    elif 70<=a<=79:
##        print("Grade C")
##    elif 60<=a<=69:
##        print("Grade D")
##else:
##    print("Fail")
#2.        
##age = int(input("Enter the age"))
##if age<=12:
##    print("The ticket price is $5")
##elif age>12:
##    if 13<=age<=17:
##        print("The ticket price is $8")
##    elif 18<=age<65:
##        print("The ticket price is $10")
##    elif age>=65:
##        print("The ticket price is $6")    


#loop       
##a = int(input("enter a number"))
##b = 0
##for i in range(1,a+1):
##    b+=i
##print(b)


# a = int(input("enter a number"))
# b = 1
# for i in range(1,a+1):
#    b*=i
#    print(b)

##a = int(input("enter a number"))
##for i in range(1,11):
##    print(i,"x",a,"=",i*a)

##a = input("Enter a word")
##b = "aeiouAEIOU"
##count = 0
##for i in (a):
##    if i in b:
##        count+=1
##print(count)

##a = int(input("Enter a number"))
##b = int(input("Enter a number"))
##c = int(input("Enter a number"))
##if a>b and a>c:
##    print("a is greater")
##elif b>a and b>c:
##    print("b is greater")
##elif c>a and c>b:
##    print("c is greater")
    

##a = int(input("Enter a number"))
##Flag =0
##for i in range(2,a):
##    if a%i==0:
##        Flag=1
##if Flag==1:
##    print("Not a prime")
##else:
##    print("Prime")

##a = int(input("Enter a number"))
##b=1
##for i in range(1,a+1):
##     b*=i
##print(b)

##a = int(input("Enter a num"))  ****
##b = input("Enter a symbol")    ****
##for i in range(1,a+1):        ****
##    print(b*a)

#a =int(input("Enter a num"))
#b =input("Enter a str")
#for i in range(1,a+1):
#   print(i*b)

#a = int(input("Enter a number"))
#for i in range(0,a,1):
#    print("*"*i)
#for i in range(a,0,-1):
#    print("*"*i)
     
# a = int(input("a"))
# add = str(input("y or n"))
# bill = 0
# if a>=10:
#     bill+=10
# else:
#     bill+=5
# if add=="y":
#     bill+=3
# else:
#     bill+=8
# print(bill)                

# import random
# b = random.random()
# a = random.randint(100,200)
# print(a)
# print(b*100)

# import random
# a = random.randint(0,1)
# if a==0:
#     print("heads")
# elif a==1:
#     print("tails")    

# import random
# name_string = input("Enter the names separated by comma ")
# names = name_string.split(",")
# print(names)
# a = random.randint(0,len(names)-1)
# print(names[a])

# name = str(input("Enter your name: "))
# clg = str(input("Enter a name of your clg: "))
# print(f"Welcome to {clg}")
# print("hi {} welcome to {}".format(name,clg))
# print("hi %s welcome to %s"%(name,clg))

# student_heights = input("Enter the heights").split()
# for n in range(0,len(student_heights)):
#     student_heights[n]=int(student_heights[n])
# print(student_heights)                                  

# a = input("Enter your input: ")
# b = a[ : :-1]
# if a==b:
#     print("It is a palindrome")
# else:
#     print("it is not a palindrome")    

# a = 26
# b = 30
# c = 1
# for i in range(1,a):
#     if a % i == 0 and b % i == 0:
#         c = i
# print(c)

# a = str(input("Enter your password"))
# b = a.upper()
# if len(a)>=8:
#     print("your password has more than 8 characters")
#     print(b)
# for b in a:
#     if b in a:
#         print("It has atleast one uppercase") 
#     break   
# else:
#     print("Enter the password with required conditions")

# a = {"yui","jkf","ghj","sdf"}
# print(a)
# print(a[0])

# a=[1,2,3,4,5]
# b=0
# for i in a:
#     b+=i
#     print(b)

# a = input("Enter a three digit value")
# c=1
# d=1
# e=1
# for i in range(1,int(a[0])+1):
#     c=c*i

# for i in range(1,int(a[1])+1):
#     d=d*i

# for i in range(1,int(a[2])+1):
#     e=e*i

# result = c+d+e
# print(c,"+",d,"+",e,"=",result)
# if result==int(a):
#     print("It's a strong number")
# else:
#     print("It's not a strong number")


# a = int(input("Enter a number"))
# b=0
# for i in range(1,a):
#     if a%i==0:
#         b+=i
#         print(b)
# print(b)       
# if b==a:
#     print("It's a perfect number") 
# else:
#     print("It's not a perfect number")    
 
# for i in range(0,101):
#     if i%3==0 and i%5==0:
#         print("fizzbuzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#         print(i)        


# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# l = int(input("How many letters would you like in your password?\n")) 
# s = int(input(f"How many symbols would you like?\n"))
# n = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = []
# real_password =""
# for i in range(1,l+1):
#     char = random.choice(letters)
#     password += char
# print(password)

# for i in range(1,n+1):
#     num = random.choice(numbers)
#     password += num
# print(password)

# for i in range(1,s+1):
#     sym = random.choice(symbols)
#     password += sym
# print(password)
# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# random.shuffle(password)
# print(password)     
            
# for i in password:
#     real_password+=i
# print(real_password)            



# a=int(input("Enter a number"))
# b=0                                  ****
# for i in range(a,0,-1):              ***
#     i=i*"*"                          **
#     print(i)                         *

# a=int(input("Enter a number"))
# b=1
# for i in range(1,a+1):
#     i=1*str(i)*a
#     print(i)

# a=int(input("Enter a number"))         *
# for i in range(1,a+1):                ***
#     print(" "*(a-i),"*"*(2*i-1))     *****

# a = int(input("Enter a number"))
# b = 0
# for i in range(1,a):           *
#     i=i*"*"                    **
#     print(i)                   ***
# for i in range(a,0,-1):        **
#     i=i*"*"                    *
#     print(i)    


# a=int(input("Enter a number"))  
# for i in range(1,a):                
#     print(" "*(a-i),"*"*(2*i-1))       
# for j in range(a,0,-1):                
#     print(" "*(a-j),"*"*(2*j-1))    

# a = int(input("Enter a number"))
# b=0
# for i in range(1,a):
#     b+=i
#     if a%i==0:
#         print(i)
# if b>a:
#     print("It's an abundant number")
# else:
#     print("It's not an abundant number")      

# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# c=0
# d=0
# for i in range(1,a):
#     if a%i==0:
#         c+=i
#         print(i)
   
# for j in range(1,b):
#     if b%j==0:
#         d+=j
#         print(j)         
# f=c/a
# g=d/b
# if f==1 and g==1:
#     print("It's is a friendly pair")
# else:
#     print("Not a friendly pair")

# a=list(input("Enter a sentence").split(" "))
# b=[]
# for i in a:
#     b+=str(len(i))
# c=max(b)
# e=b.index(c)    
# print(e)
# print(a[e])

# a=input("Enter a sentence")
# b="aeiouAEIOU"
# count=0
# for i in a:
#     if i in b:
#         count+=1
# print(count)        

# a=input("Enter a sentence")
# b=input("Enter a sentence")
# for i in a:
#     print(i)
# for j in b:
#     print(j)     

# #make_tags('cite', 'Yay') → '<cite>Yay</cite>'
# tag = "cite"
# word = "yay"
# print('<'+tag+'>'+ word +'</'+tag+'>')

# # make_out_word('<<>>', 'Yay') → '<<Yay>>'
# out="<<>>"
# word="yay"
# print(out[0:2]+word+out[2:4])

# # extra_end('Hello') → 'lololo'
# word="hello"
# print(word[-1:-3:-1])

# nums=[1,3,2,4,1]
# if len(nums)>0 and nums[0]==nums[-1]:
#     print(True)
# else: 
#     print(False) 

# nums=[1,2,3]
# left, right = 0, len(numbers) - 1
# while left < right:
#     numbers[left], numbers[right] = numbers[right], numbers[left]
#     left += 1
#     right -= 1

# a = [83,69,68,72,85]
# b = list(map(lambda x:chr(x),a))
# c = ""
# for i in b:
#     c+=i
# print(c)

#NESTED-FOR
# list1 = list(input("Enter a list"))
# k = int(input("Enter a number"))
# list2=[]
# for i in list1:
#     list2=i-4
# print(list2)
# for i in list1:
#     for j in list2:
#         print(i, j)


# n=int(input("Enter a number"))
# a=0
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         a+=i*j
# print(a)


# n=int(input("Enter a number"))
# a=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")   /////////////////////////////////

# list1=[1,2,3,4,5,6]
# s=7
# for i in list1:
#     for j in list1:
#         if i+j==s:
#             a=(i,j)
#             print(a,end=" ")


##counting numbers in the list.
# def count_element(input_list):
#     element_count={}

#     for item in input_list:
#         if item in element_count:
#             element_count[item]+=1
#         else:
#             element_count[item]=1
#     return element_count

# sample_list=[1,2,2,3,3,3,4,5,5,6,6,7]

# element_count=count_element(sample_list)
# list1 = element_count.items()
# for a,b in list1:
#     print(a,":",b)



# def calculator(num1,num2):
#     num1=float(input("Enter a number"))
#     while True:
#         num2=float(input("Enter a number"))       
#         c=input(f"Your Options are: \n1. +\n2. -\n3. *\n4. /\n5. %\n6. **\n  ")
#         if c=="quit":
#             break
#         elif c=="1":
#             num1=num1+num2
#             print(num1)
#         elif c=="2":
#             num1=num1-num2
#             print(num1)    
#         elif c=="3":
#             num1=num1*num2
#             print(num1) 
#         elif c=="4":
#             num1=num1/num2
#             print(num1)
#         elif c=="5":
#             num1=num1%num2
#             print(num1)
#         elif c=="6":
#             num1=num1**num2
#             print(num1)
#         else:
#             print("Invalid input")
# calculator(2,2)

#--------------------FILE HANDLING------------------------------------

# with open("sample.txt","r") as file:
#     print(file.read())
# with open("sample.txt","w") as file:
#     file.write("Welcome Luci\n")
# with open("sample.txt","a") as file:
#     file.writelines("Welcome vasanth\n Welcome monish\n")  
# import os    
# os.remove(file)       
#------------------Exception Handling--------------------------------------
# try:
#     def division(a,b):
#       c=a/b
#       print(c)
# except ZeroDivisionError:
#    print("Division by 0 is not allowed")
# else:
#    print("Something wrong ")
# division(2,2)

# my_list = [1,2,3,4,5,6,7]
# try:
#     index = int(input("Enter a number"))
# except IndexError:
#     print("Index number does not exist")   
# def get_element(my_list, index):
#     try:
#        if index<=len(my_list):
#           print(my_list[index])  
#     except:
#         print("Index number does not exist")
# get_element(my_list,index)
#-----------1----------------------  
# def get_element(my_list, index):
    # try:
    #    print(my_list[index])  
    # except IndexError:
    #     print("Index number does not exist")
#     except TypeError:
#         print("Check the type of the input")
# get_element([1,2,3,4,5,6],"k")             
# ----------------2--------------------
# def open_file(filename):
#     try:
#        with open("sample.txt","r") as file:
#           file.read()
#           print("File opened Successfully")
#     except FileNotFoundError:
#        print("File not found")   
# open_file("sample.txt")
#----------------3-------------------------
# def safe_divide(a,b):
#      try:
#          print(a/b)
#      except ZeroDivisionError:
#          print("Zero division error occurs")
#      finally:
#          print("Operation Completed")    
# safe_divide(4,0)  
#---------------4------------------------------
# try:
#     def check_positive(number):
#         if number>=0:
#             print("It is a Positive number")
# except ValueError:
#     print("appropriate error occured")
# check_positive(-7)
#---------------------5-----------------
# def safe_divide(a,b):
#      try:
#          c=a/b
#          print(c)
#          try:
#              list1=[1,2,3,4,5,6]
#              print(list1[int(c)])
#          except IndexError:
#              print("Index number out of range")    
#      except ZeroDivisionError:
#          print("Zero division error occurs")    
# safe_divide(24,2) 
#-----------------6-----------------------
def positive_divide(a,b):
     try:
         if a>=0 and b>=0:
             print(a/b)
     except ZeroDivisionError:
         print("Zero division error occurs")
     else:
         print("Only positive numbers are allowed")     
positive_divide(4,-2)
        