import random
import string
def generate_password():
    upper=string.ascii_uppercase
    lower=string.ascii_lowercase
    special=string.punctuation
    digit=string.digits

    password=[]
    password.extend(list(upper))
    password.extend(list(lower))
    password.extend(list(special))
    password.extend(list(digit))

    pass_len = input('Enter password Length : ')

    try:
        pass_len=int(pass_len)
        print('Random Password - 1 :')
        new=random.sample(password,pass_len)
        print('\t',('').join(new))
        print('Random Password - 2 :')
        random.shuffle(password)
        print('\t',('').join(password[:pass_len]))
        print('Random Password - 3 :')
        new=random.sample(password,pass_len)
        print('\t',('').join(new))

    except:
        print('Enter Integer Only')

while True:
    user=input('Press Enter to Excecute and \'q\' to Quit -->')
    if user!='q':
        generate_password()
        print()
    else:
        break
