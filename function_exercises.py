#Create test function. Only handles one argument functions for now
def test_funct(test_vals,funct):
    print(f'\nTesting function: {funct.__name__}')
    tick = '\''
    
    for i in test_vals:
        #lots of weird formatting just to get simple data type
        # else print(type(x)) returns a format of " <class 'data_type'> ""
        dtype = str(type(i)).split(tick)[1] 
        
        print(f'Test {i}, {dtype}, {funct(i)}')

#1) 
def is_two(val):
    val=str(val)
    if val == '2' or val == '2.0': return True
    else: return False

test_funct([2,'a','2',2.0],is_two)
# #number can be converted to string w/o error (but not the other way around)
# # also included '2.0' as that is what a converted float to string would look like


#2)
def is_vowel(char):
    vowels = ['a','e','i','o','u']
    if type(char) == str and char.lower() in vowels: return True
    else: return False

test_funct(['a','b','E','G',2,'aa'],is_vowel)

#3) 
def is_consonant(char):
    vowels = ['a','e','i','o','u']
    if type(char) == str and len(char) == 1 and char.isalpha() and char.lower() not in vowels: return True
    else: return False
#or just use our last function
def is_consonant_v2(char):
    return (type(char) == str and len(char) == 1 and char.isalpha() and not is_vowel(char))

test_funct(['a','b','E','G',2,'CC','$'],is_consonant)
test_funct(['a','b','E','G',2,'CC','$'],is_consonant_v2)

#4) take in word, capitalize first letter if consonant
def cap_cons(word):
    if not is_vowel(word[0].lower()):
        return (word[0].upper() + word[1:]) #if special character, upper does nothing
    else: return word

test_funct(['apple','banana','Custard','straw Berry pie','$$bills'],cap_cons)

#5) 
def calculate_tip(perc,bill):
    return bill*perc
print(calculate_tip(.2,80))
print(calculate_tip(.3,20))

#6) 
def apply_discount(price,disc):
    return (price*(1-disc))
print(apply_discount(100,.2))
print(apply_discount(50,.1))

#7)
#only handles US style
def handle_commas(words):
    num = float(words.replace(',',''))
    return num

test_funct(['2,000','15,000.05','5358.25'],handle_commas)
#things to try next:
#  check first character, if not digit then strip () 
#       - granted, there are plenty of multi-character currency symbols
# handle european style numbers (. then ,) - would need optional parameter

#8)
def get_letter_grade(val):
    if val >= 90: 
        grade = 'A'
    elif val >= 80:
        grade = 'B'
    elif val >= 70:
        grade = 'C'
    elif val >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

test_funct([85,101,20,73],get_letter_grade)

#9)
def remove_vowels(words):
    new_word = ''
    for x in words:
        if not is_vowel(x): new_word += x
    return new_word

test_funct(['apple','banana','kiwi','stone fruit'], remove_vowels)

#10)  
def normalize_name(words):
    words = words.strip().lower() #strip spaces first and lowercase
    new_word = ''
    #First remove all unwanted characters (ie special characters, but not spaces)
    for x in words:
        if x.isalnum() or x == ' ' or x =='_':
            new_word += x
    #Now, remove strip numbers from beginning until they are a valid character
    while True:
        if new_word[0].isdigit() or new_word[0] == ' ':
            new_word = new_word[1:]
        else: 
            break
    #Now, replaces any remaining spaces in the middle with underscores
    new_word = new_word.replace(' ','_')
    return new_word

test_funct(['7 dogs','und_score','7 dogs 7 dogs','First Name','% Completed','   spaces spaces spaces  '],normalize_name)

#11)
def cumulative_sum(lst):
    cumul_sum = []  #my array to hold the cumulative sums
    cumul = 0       #
    for i in lst:
        cumul += i  #the new cumulative value for this iteration 
        cumul_sum += [cumul]
    return cumul_sum

test_funct([[1,1,1],[1,2,3,4]],cumulative_sum)

# BONUS
#1)
import re

def twelveto24(time):
    #validate input - NEED TO FIX THIS
    # # first 1-1 characters must be between 1 and 12, then colon, then 2 characters between 0 & 59, then am or pm
    # if not re.match('[0-12]{1,2}:[0-59]{2,2}(am|pm)',time): print('invalid input1')
    # if not re.match('[0-9]{1,2}:[0-5][0-9](am|pm)',time): print('invalid input2') #doesn't account for 00, or ex: 80
    # if not re.match('[0-1]?[0-9]:[0-59]{2,2}(am|pm)',time): print('invalid input3') #doesn't account for 00
    # return 'return'
    #store if pm as T/F
    is_pm = time[-2:].lower() == 'pm' 
    #Drop off last 2 char, then split into hrs and min using ':' and make int
    hr, mn = list(map(int,(time[:-2].split(':')))) 
    if hr == 12 and not is_pm: hr = 0 #if 12am, make zero
    elif hr < 12 and is_pm: hr += 12 #if pm (and not noon-ish) then add 12 hours
    return f'{hr:02}:{mn:02}' #if integers aren't two digits, pad with zero at front

test_funct(['11:52am','1:02pm','01:02pm','12:38am','12:59pm','12:02a','81:12pm','00:43am','0b:33pm','18:15pm'],twelveto24)



#2) 
