import math

#comments




print('Hello world')

print(1+3)

vardas = 'Titas'
amzius = '20'

#str() | int = str
#int() | str = int 


print(int(amzius) + 2)

print(f'Mano vardas {vardas}')
print(f'Man yra {amzius}')

print('Mano vardas {}' .format(vardas))
print('Man yra {}' .format(amzius))

print('-'*20)


print('Hello worldd ', end='')
print('Goodbye')


def hello_world():
    print('Hello world for func')
print('print putside the function')

hello_world()

def hello(name):
    print(f'Hello, {name}')
hello('Robertas')

def sum(a,b):
    print(f'{a} + {b} = {a+b}')
sum(2, 3)


a = input('Pasirink pirma skaisiciu: ')
b = input('Pasirink antra skaisiciu: ')

def parse(input_string):
    return int(input_string)

sum(parse(a), parse(b))

#more shit
#more shit 

