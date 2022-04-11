
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
# print(f'test 3 {is_two(3)}')
# test = '2'
# test2 = 'a'
# print(f'test \'2\' {is_two(test)}')
# #print(f'test \'2\' {is_two('2')}') #Figure out why it didn't like that
# #Solution: You can do this, but you need to use single quotes inside double or vice-versa.  See is_vowel
# print(f'test 2 {is_two(2)}')
# print(f'test a {is_two(test2)}')
# print(f'test 2.0 {is_two(2.0)}')

#2)
def is_vowel(char):
    vowels = ['a','e','i','o','u']
    if char.lower() in vowels: return True
    else: return False

test_funct(['a','b','E','G'],is_vowel)

#3) 
def is_consonant(char):
    vowels = ['a','e','i','o','u']
    if char.lower() not in vowels: return True
    else: return False
#or just use our last function
def is_consonant_v2(char):
    return not is_vowel(char)

test_funct(['a','b','E','G'],is_consonant)
test_funct(['a','b','E','G'],is_consonant_v2)

#4) take in word, capitalize first letter if consonant
def cap_cons(word):
    if not is_vowel(word[0].lower()):
        return (word[0].upper() + word[1:])
    else: return word

test_funct(['apple','banana','Custard','straw Berry pie'],cap_cons)