import random 
import string 

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters 
    digits = string.digits
    special = string.punctuation 

    characters = letters
    if numbers:
        characters += digits 
    if special_characters:
        characters += special

    meets_criteria = False
    has_digits = False
    has_special = False

    password = ''

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char 

        if numbers and new_char in digits:
            has_digits = True

        if special_characters and new_char in special:
            has_special = True

        meets_criteria = True

        if numbers:
            meets_criteria = meets_criteria and has_digits

        if special_characters:
            meets_criteria = meets_criteria and has_special

    return password

if __name__=='__main__':
    min_length = int(input('Enter a Length for your password: '))
    nums = input('Do you want your password to have numbers? (Yes / NO): ')
    specials = input('Do you want your password to have special characters? (Yes / No): ')

    if nums.lower() == 'yes' and specials.lower() == 'yes':
        print('Here is Your Password: ',generate_password(min_length))
    
    elif nums.lower() == 'yes' and specials.lower() == 'no':
        print('Here is Your Password: ',generate_password(min_length, True, False))

    elif nums.lower() == 'no' and specials.lower() == 'yes':
        print('Here is Your Password: ',generate_password(min_length, False, True))

    else:
        print('Here is Your Password: ',generate_password(min_length, False, False))
