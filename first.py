from decimal import Decimal, getcontext
import math
from unicodedata import decimal
# Comments

'''
Multi line comments
'''

print('Hello world')
print(1+3)


# Variables
vardas='Jonas'
amzius = 20

#Method 1
print ('Mano vardas' + vardas)
print('Man yra ' + str(amzius))

#Method 2
print(f'Mano vardas {vardas}')
print(f'Man yra {amzius}')


#Method 3
print('Mano vardas {}'.format(vardas))
print('Man  yra {}'.format(amzius))

# str() | int--> str
# int() | str--> int

print(int(amzius)+2)

print('-'*20)

print('Hello world', end='')
print('It prints on the same line')

#Method 4

print('Mano vardas', vardas)
print('Man yra', amzius)

#def echo(word):
#   print(word)

# Mixing ' and "
#print(f'Mano vardas yra {vardas} ir as noriu pasakyti {echo("")}')

#Math
print('2+2 = ', 2+2)

print('2^2= ' , math.pow(2,2))


def hello_world():
    print("Hello world from func")

hello_world()

def hello(name):
    print(f"Hello, {name}")

hello("Robertas")

def sum(a, b):
    print(f"{a} + {b} = {a+b}")

sum(2, 3)

print("-" * 20)

a= input("Pasirink pirma skaiciu: ")
b= input("Pasirink antra skaiciu")


def parse(input_string):
    return int(input_string)
print (f"{a} | {b}")

sum(parse(a), parse(b))

#New code
#New code
#New code
#New code