#Playing with operators and data types
#1) calculating cost of movies
lm = 3
bb = 5
he = 1
price = 3*(lm + bb + he)
print(f'Your total is ${price}.')

#2) 
r_Google = 400
r_Amazon = 380
r_Facebook = 350
weeks_pay = r_Google* 6 + r_Amazon * 4 + r_Facebook * 10
print(f'Your salary this week is ${weeks_pay}')

#3)
max_seats = 26
enr_students = 24
class_time_code = 15 
# imagining a system where each day/hour during the weeks corresponds to a time slot code
# so let's say ~10 a day, so 15 would correspond to Tuesday around noon
stud_schedule = [2,3, 12, 28, 29,40] #student's hypothetical existing schedule
if enr_students < max_seats:
    if class_time_code in stud_schedule:
        print("This class conflicts with another on your schedule")
    else: 
        stud_schedule.append(class_time_code)
        print("Class added to your schedule")
else: print("This class is full")

#4)
num_items = 5
if num_items > 2:
    discount = .9
    print('You get a discount!')
else: 
    discount = 1
    print('You have not bought enough items to get a discount')
#dictionaries would be a good choice here

#5) password verification
username = 'codeup'
password = 'notastrongpassword'

hasWhiteSpace = ((len(username)>len(username.strip())) or (len(password)>len(password.strip())))
minLen = len(password)>=5
maxLen = len(username) <= 20
notSame = (username != password) 
print(hasWhiteSpace,minLen,maxLen,notSame)



