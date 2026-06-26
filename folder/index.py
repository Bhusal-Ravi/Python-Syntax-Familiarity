age = 25

if(age<13):
    print("Child")
elif(age<20):
    print("Teen")
elif(age<60):
    print('Adult')
else:
    print('Senior')


discount=2
dayOfWeek='wednesday'
age=20
adult_price=12
children_price=8
ticket_price=0

if (age>=18):
    
   
        ticket_price=adult_price
else:
   
            ticket_price=children_price


if(dayOfWeek=='wednesday'):
        ticket_price=adult_price-discount

print(ticket_price)


student_grade=""
marks=90

if(marks<60):
    student_grade='F'
elif(marks>=60 and marks<=69):
    student_grade='D'
elif(marks>=70 and marks<=79):
    student_grade='C'
elif(marks>=80 and marks<=89):
    student_grade='B'
elif(marks>=90 and marks<=100):
    student_grade='A'

print(student_grade)


fruit='banana'
color='brown'
status=''

if ( fruit== 'banana' and color=='green' ) :
    status='unripe'
elif(fruit== 'banana' and color=='yelow' ):
    status='ripe'
else:
    status='overripe'

print(status)

distance=15
transport=''

if(distance>15):
    transport='car'
elif(distance>3):
    transport='bike'
else:
    transport='walk'

print(transport)

password='1234ka'
strength=''

if(len(password)>10):
    strength='Strong'
elif(len(password)>5):
    strength='Medium'
else:
    strength='Weak'

print(strength)