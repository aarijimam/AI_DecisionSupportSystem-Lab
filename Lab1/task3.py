import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.punctuation + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == '__main__':
    total_passwords = int(input('Enter number of passwords: '))
    length = int(input('Enter length of passwords: '))
    passwords = []
    for i in range(total_passwords):
        passwords.append(generate_password(length))

    print(f'Your passwords are: ')
    for i, pw in enumerate(passwords):
        print(f'  {i+1}. {pw}')
