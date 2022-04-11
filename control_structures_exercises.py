#1)  condition basics
weekend = ['saturday','sunday']
inp = input("Enter a day of the week: ").lower()

if inp == 'monday':
    print(f'\n {inp} is a Monday')
else:
    print(f'\n {inp} is not a Monday')

if inp in weekend:
    print(f'\n WOOHOO! {inp} is on the weekend!')
else:
    print(f'\n {inp} is a weekday :(')

#calculating weekly pay
hrs = int(input('\nHow many hours did you work this week? '))
rate = int(input('\nWhat is your hourly pay? '))

overtime = 0 #assume no overtime/reset variable
if hrs > 40: 
    overtime = (hrs-40)*rate*.5
paycheck = overtime + (hrs*rate)

print(f'\n\nThis week\'s paycheck will be ${paycheck}')


#2) Loop basics
#a) While
i=5
while i <= 15:
    print(i)
    i += 1

i=0
while i<= 100:
    print(i)
    i += 2

i=100
while i > -11:
    print(i)
    i += -5

i = 2
while i < 1000000:
    print(i)
    i = i**2
#alt
# i = 2
# while i < 1000000:
#     print(i)
#     i *= i

i=100
while i > 0:
    print(i)
    i += -5

#b) For loops
val = int(input('Enter a number '))
for i in range(1,11):
    print(f'\n{val} x {i} = {val*i}')

for i in range(1,10):
    line = str(i)
    for x in range(1,i):
        line += str(i)
    print(line)
#The better way:
for i in range(1,10):
    print(f'{i}'*i)

#c) break and continue
while True:
    inp = input('Please enter an odd number between 1 and 50: ')
    if not inp.isdigit():
        print('That\'s not even a number!')
        continue
    inp=int(inp)
    if (inp % 2 != 0) and 1<inp<50 :
        break
    else: print(' Error! Try again') 
print(f'Number to skip is: {inp}\n')
i=1
while i < 50:
    if i != inp: print(f'Here is an odd number: {i}')
    i += 2

#d/e) Count to positive integer
while True:
    inp = input('Please enter a positive number: ')
    if not inp.isdigit() or int(inp)<=0:
        print('Invalid entry.')
        continue
    inp=int(inp)
    break

for i in range (0,inp+1):
    print(i)
for i in reversed(range(1,inp+1)):
    print(i)


#3) FIZZBUZZ
for i in range(1,101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)



#4) Table of Powers
inp = int(input('Enter an integer: '))
print('Here is your Table of POWERS!\n')
print('number | squared | cubed')
print('------ | ------- | -----')
for i in range(1,inp+1):
    print(f'{i}' + (' ' * (7-len(str(i)))) + f'| {i**2}' + (' ' * (8-len(str(i**2)))) + f'| {i**3}' )

#ugh, this is way better:
print('\nHere is your well-coded table!\n')
print('number | squared | cubed')
print('------ | ------- | -----')
for i in range(1,inp+1):
    print(f'{i}'.ljust(7) + f'| {i**2}'.ljust(10) + f'| {i**3}')

#5) Convert give number grades into letter grades
while True:
    inp = int(input('Please enter your numerical grade: '))
    if inp >= 88: 
        grade = 'A'
    elif inp >= 80:
        grade = 'B'
    elif inp >= 67:
        grade = 'C'
    elif inp >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(f'Your grade is {grade}')
    cont = input('\nWould you like to enter another grade? (Yes/No) ')
    if cont.lower() in ('y','yes'):
        continue
    else: break

#6) 
new_fav = { 
    'title':'A Testament of Steel',
    'author':'Davis Ashura',
    'genre':'Epic Fantasy'
    }
old_fav = { 
    'title':'Dragonsdawn',
    'author':'Anne McCaffery',
    'genre':'sci-fi'
    }
epic_fav = { 
    'title':'The Wise Man\'s Fear',
    'author':'Patrick Rothfuss',
    'genre':'Epic Fantasy'
    }
my_books = [new_fav,old_fav,epic_fav]
genre = input('Please enter a genre: ')

for x in my_books:
    if x['genre'] == genre:
        print(x['title'])








