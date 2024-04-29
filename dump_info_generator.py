import random

from random import randrange
from datetime import timedelta, datetime

boys_names = []
girls_names = []

with open('names_boys.txt', encoding='utf-8') as f_b:
    for n in f_b:
        boys_names.append(n.strip())

with open('names_girl.txt', encoding='utf-8') as f_b:
    for n in f_b:
        girls_names.append(n.strip())

def get_surname(r_surname):
    if r_surname[-1] in ['a','y','i','e','o']:
        r_surname+='ýew'
    elif r_surname[-1] in ['ç']:
        r_surname=r_surname[:-1]+'jow'
    elif r_surname[-1] in ['p']:
        r_surname=r_surname[:-1]+'bow'
    else:
        r_surname += 'ow'
    
    return r_surname

def get_middle_name(r_middle):
    return get_surname(r_middle)+'iç'

def random_name_surname_boy():
    r_name = random.choice(boys_names).title()
    r_surname = get_surname (random.choice(boys_names).title())
    r_middle = get_middle_name(random.choice(boys_names).title())
          
    return f'{r_surname} {r_name} {r_middle}'

def random_name_surname_girl():
    r_name = random.choice(girls_names).title()
    r_surname = get_surname(random.choice(boys_names).title())+'a'
    r_middle = get_surname(random.choice(boys_names).title())+'na'
          
    return f'{r_surname} {r_name} {r_middle}'


def random_date(start, end):
    d1 = datetime.strptime(start, '%d.%m.%Y')
    d2 = datetime.strptime(end, '%d.%m.%Y')
    delta = d2 - d1
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return  (d1 + timedelta(seconds=random_second)).strftime('%d.%m.%Y')




for i in range(20):
    print(random_name_surname_girl())
    print(random_name_surname_boy())
    print(random_date('01.01.1990','31.12.2002'))
    print(random_date('01.01.2022','31.12.2023'))
