# age = 25

# if(age<13):
#     print("Child")
# elif(age<20):
#     print("Teen")
# elif(age<60):
#     print('Adult')
# else:
#     print('Senior')


# discount=2
# dayOfWeek='wednesday'
# age=20
# adult_price=12
# children_price=8
# ticket_price=0

# if (age>=18):
    
   
#         ticket_price=adult_price
# else:
   
#             ticket_price=children_price


# if(dayOfWeek=='wednesday'):
#         ticket_price=adult_price-discount

# print(ticket_price)


# student_grade=""
# marks=90

# if(marks<60):
#     student_grade='F'
# elif(marks>=60 and marks<=69):
#     student_grade='D'
# elif(marks>=70 and marks<=79):
#     student_grade='C'
# elif(marks>=80 and marks<=89):
#     student_grade='B'
# elif(marks>=90 and marks<=100):
#     student_grade='A'

# print(student_grade)


# fruit='banana'
# color='brown'
# status=''

# if ( fruit== 'banana' and color=='green' ) :
#     status='unripe'
# elif(fruit== 'banana' and color=='yelow' ):
#     status='ripe'
# else:
#     status='overripe'

# print(status)

# distance=15
# transport=''

# if(distance>15):
#     transport='car'
# elif(distance>3):
#     transport='bike'
# else:
#     transport='walk'

# print(transport)

# password='1234ka'
# strength=''

# if(len(password)>10):
#     strength='Strong'
# elif(len(password)>5):
#     strength='Medium'
# else:
#     strength='Weak'

# print(strength)

# numbers=[1,2,3,-4,6,-5,-7,4,65]
# count=0
# for number in numbers:
#     if(number<0):
#         count+=1
    
# print(count)


# number =20
# sum=0

# for i in range(1,20):
#     if(i%2==0):
#         print(i)
#         sum+=i
# print(sum)


# for i in range (1,10):
#     if(i==5):
#         continue
#     mult=10*i
#     print("10 X",i,'=',mult)

# string='Python'
# output=''

# for i in string:
#     output= i+ output 

# print(output)

# string=']ttateaeorapzxd'
# non_repeated=''


# for char in string:
#     str=char
#     count=0
#     for char_i in string:
#         if(char_i==str):
#             count+=1

#     if(count==1):
#         non_repeated+=char
#         break
# print(non_repeated)

# number=6
# factorial=1

# while number>0 :
#     factorial=factorial*number
#     number-=1
# print(factorial)

# while True:
#     number=int(input('Enter betwn 1 and 10'))
#     print(number)
#     if(number>1 and number<10 ):
#         break



# number=4
# count=0

# for i in range(1,number):
#     if(number%i==0):
#         count+=1
    
# if(count>1):
#     print(number,' is not prime number')
# else:
#     print(number,' is a prime number')


item=['one','two','one','three','four','five','six', 'six']
duplicate=''

for i in item:
    if(item.count(i)>1):
        duplicate+=i
        break