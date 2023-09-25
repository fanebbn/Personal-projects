import sys
import random

def generator():
    ans = input('-- PASSWORD GENERATOR --\nChoose option\n1: generate password\n2: exit the program\nYour choice: ')
    while ans != '1' and ans != '2':
        ans = input('Enter a valid number! ')
    if ans == '1':
        letters = 'abcdefghijklmnopqrstuvwxyz'
        digits = '0123456789'
        special_char = '!@#$%^&*|()_+'
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        password_length = int(input('Password length: '))
        uppercase_ans = input('Use uppercase letters? (y/n): ')
        digits_ans = input('Use digits? (y/n): ')
        special_char_ans = input('Use special char? (y/n): ')
        password = ''
        if uppercase_ans == 'y' and digits_ans == 'y' and special_char_ans == 'y':
            list = [letters, digits, special_char, uppercase]
            for i in range(0,password_length):
                new_var = random.choice(list)
                if new_var == letters:
                    password = password + random.choice(letters)
                if new_var == digits:
                    password = password + random.choice(digits)
                if new_var == special_char:
                    password = password + random.choice(special_char)
                if new_var == uppercase:
                    password = password + random.choice(uppercase)
                    
        if uppercase_ans == 'y' and digits_ans == 'y' and special_char_ans == 'n':
            list = [letters, uppercase, digits]
            for i in range(0,password_length):
                new_var = random.choice(list)
                if new_var == letters:
                    password = password + random.choice(letters)
                if new_var == digits:
                    password = password + random.choice(digits)
                if new_var == uppercase:
                    password = password + random.choice(uppercase)
    
        if uppercase_ans == 'y' and digits_ans == 'n' and special_char_ans == 'n':
            list = [letters, uppercase]
            for i in range(0,password_length):
                new_var = random.choice(list)
                if new_var == letters:
                    password = password + random.choice(letters)
                if new_var == uppercase:
                    password = password + random.choice(uppercase)
                    
        if uppercase_ans == 'n' and digits_ans == 'n' and special_char_ans == 'n':
            list = [letters]
            for i in range(0,password_length):
                new_var = random.choice(list)
                if new_var == letters:
                    password = password + random.choice(letters)
                    
        if uppercase_ans == 'n' and digits_ans == 'y' and special_char_ans == 'n':
            list = [letters, digits]
            for i in range(0,password_length):
                new_var = random.choice(list)
                if new_var == letters:
                    password = password + random.choice(letters)
                if new_var == digits:
                    password = password + random.choice(digits)
                    
        if uppercase_ans == 'n' and digits_ans == 'y' and special_char_ans == 'y':
            list = [letters, digits, special_char]
            for i in range(0,password_length):
                new_var = random.choice(list)
                if new_var == letters:
                    password = password + random.choice(letters)
                if new_var == digits:
                    password = password + random.choice(digits)
                if new_var == special_char:
                    password = password + random.choice(special_char)
                    
        if uppercase_ans == 'n' and digits_ans == 'n' and special_char_ans == 'y':
            list = [letters, special_char]
            for i in range(0,password_length):
                new_var = random.choice(list)
                if new_var == letters:
                    password = password + random.choice(letters)
                if new_var == special_char:
                    password = password + random.choice(special_char)
                    
        if uppercase_ans == 'y' and digits_ans == 'n' and special_char_ans == 'y':
            list = [letters, uppercase, special_char]
            for i in range(0,password_length):
                new_var = random.choice(list)
                if new_var == letters:
                    password = password + random.choice(letters)
                if new_var == special_char:
                    password = password + random.choice(special_char)
                if new_var == uppercase:
                    password = password + random.choice(uppercase)
    
        #if not isinstance(password_length,int):
         #   sys.exit()
            
    if ans == '2':
        print('Bye!')
        sys.exit()
        
    print('Generated password:', password, '\n')
    generator()

#generator()