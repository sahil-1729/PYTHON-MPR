import random
import string

def gen_pass(min_length, number=True, special=True):
    l = string.ascii_letters
    n = string.digits
    s = string.punctuation
    character = l
    if number:
        character += n
    if special:
        character += s
    password = ""
    has_number = False
    has_special = False
    
    while len(password) < min_length:
        new_char = random.choice(character)
        password += new_char
        if new_char in n:
            has_number = True
        if new_char in s:
            has_special = True
            
    while (number and not has_number) or (special and not has_special):
        new_char = random.choice(character)
        password += new_char
        if new_char in n:
            has_number = True
        if new_char in s:
            has_special = True
    
    return password

TheLength = int(input("Enter the length of your password: "))
print(TheLength)
wantN = input("Do you want any numbers? y/n ").lower()=='y'
wantS = input("Do you want any special character? y/n ").lower()=='y'

mpass = gen_pass(TheLength, wantN, wantS)
print(mpass)
