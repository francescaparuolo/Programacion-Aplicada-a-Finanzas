

# FUNCIONES RECURSIVAS 

# ejemplo del PDF que nos dio para leer Gabi

#%% SUMMING INTEGERS

# Compute the sum of the integers from 0 up to and including n using recursion
# @param n the maximum value to include in the sum
# @return the sum of the integers from 0 up to and including n
def sum_to(n):
    if n <= 0:
        return 0                    # Base case
    else:
        return n + sum_to(n - 1)    # Recursive case
    
# Compute the sum of the integers from 0 up to and including a value entered by the user
num = int(input("Enter a non-negative integer: "))
total = sum_to(num)
print("The total of the integers from 0 up to and including", num, "is", total)

#%% FIBONACCI NUMBERS

# Compute the nth Fibonacci number using recursion
# @param n the index of the Fibonacci number to compute
# @return the nth Fibonacci number
def fib(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case
    return fib(n-1) + fib(n-2)

# Compute the Fibonacci number requested by the user
n = int(input("Enter a non-negative integer: "))
print("fib(%d) is %d." % (n, fib(n)))

#%% COUNTING CHARACTERS

# Count the number of times a particular character is present in a string
# @param s the string in which the characters are counted
# @param ch the character to count
# @return the number of occurrences of ch in s
def count(s, ch):
    if s == "":
        return 0 # Base case
    # Compute the tail of s
    tail = s[1 : len(s)]
    # Recursive cases
    if ch == s[0]:
        return 1 + count(tail, ch)
    else:
        return count(tail, ch)

# Count the number of times a character entered by the user occurs in a string entered by the user
s = input("Enter a string: ")
ch = input("Enter the character to count: ")
print("’%s’ occurs %d times in ’%s’" % (ch, count(s, ch), s))

#%% EJERCICIOS DEL PDF 

#%% EJERCICIO 173: Total the Values
# Write a program that reads values from the user until a blank line is entered. Display
# the total of all of the values entered by the user (or 0.0 if the first value entered is
# a blank line). Complete this task using recursion. Your program may not use any
# loops.

def total_of_values ():
    n = input("Enter a numeric value: ")
    if n == "":
        return 0
    else: 
        return int(n) + total_of_values()
    
total =  total_of_values ()
print ("La suma de sus numeros es: ", total)


#%% EJERCICIO 174: Greatest Common Divisor

# Formula de Euclides
def gcd (a, b):
    # if a == 0 and b == 0:
    #     error = print ("ERROR, no se puede dividir cero con cero")
    #     return error
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        num = a%b
        if num == int:
            return num
        if num != int:
            return gcd (b, num)
    if a < b:
        num = b%a
        if num == int:
           return num
        if num != int:
           return gcd (a, num)

a = int(input("Enter a numeric value: "))
b = int(input("Enter another numeric value: "))

divisor = gcd(a, b)
print (f'The greatest common divisor between {a} and {b} is {divisor}')

# Formula de los factores primos 
def descomponer(n):
    primos = []

    for i in range(2, n+1):
        # Lo que hace el while es que el numero se divida la mayor cantidad de veces 
        # posibles por un numero primo, como el 2 por ejemplo. 
        # Cuando el resto de la division por 2 ya no es cero, el loop sigue al siguiente numero primo, 
        # Cual seria el 3. Y asi sucesivamente. 
        while n % i == 0:
            primos.append(i)
            n = n / i
    return primos

def mcd (a, b):
    lista_combinados = []
    lista_a = descomponer(a)
    lista_b = descomponer(b)
    mcd = 1

    for numero in lista_a:
        if numero in lista_b:
            lista_combinados.append(numero)
            lista_b.remove(numero)
        else:
            None
    for num in lista_combinados:
        mcd *= num   
    return mcd 
    
a = int(input('Introduzca un numero: '))
b = int(input('Introduzca otro numero: '))
mcd = mcd(a, b)   
print(f'El mcd es {mcd}.')


#%% EJERCICIO 177
def roman_numbers (r):
    if r == "M":
        return 1000
    if r == "D":
        return 500
    if r == "C":
        return 100
    if r == "L":
        return 50
    if r == "X":
        return 10
    if r == "V":
        return 5
    if r == "I":
        return 1
    
        
def roman_to_integer4 (x):
    first = roman_numbers(x[0])
    tail = x[1 : len(x)]
    
    # BASE CASE
    if len(x) == 1:
        return first
    
    # RECURSIVE CASE
    else:
        if roman_numbers(x[0]) >= roman_numbers(x[1]):
            return roman_to_integer4(tail) + first
        if roman_numbers(x[0]) < roman_numbers(x[1]):
            return roman_to_integer4(tail) - first
    

x = input("Enter a roman number: ")
integer = roman_to_integer4(x)
print (f"El numero romano es {integer}.")

#%% EJERCICIO 177 USANDO UN DICCIONARIO 

dic = {'M':1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        
def roman_to_integer (x):
    first = dic[x[0]]
    tail = x[1 : len(x)]
    
    if len(x) == 1:
        return first
    
    else:
        if dic[x[0]] >= dic[x[1]]:
            return roman_to_integer(tail) + first
        if dic[x[0]] < dic[x[1]]:
            return roman_to_integer(tail) - first
    

x = input("Enter a roman number: ")
numero = roman_to_integer(x)
print (f"El numero romano es {numero}.")


#%% EJERCICIO 178

# The notion of a palindrome was introduced previously in Exercise 75. In this exercise
# you will write a recursive function that determines whether or not a string is a
# palindrome. The empty string is a palindrome, as is any string containing only one
# character. Any longer string is a palindrome if its first and last characters match, and
# if the string formed by removing the first and last characters is also a palindrome.
# Write a main program that reads a string from the user and uses your recursive
# function to determine whether or not it is a palindrome. Then your program should
# display an appropriste message for the user.

def palindrome (word):
    lista = list(word)
    
    if len(lista) == 0 or len(lista) == 1:
        x = print ('Your word is a PALINDROME.')
        return x
    
    primer_letra = lista.pop(0)
    ultima_letra = lista.pop(-1)
    
    if primer_letra == ultima_letra:
        new_word = ''.join(lista)
        return palindrome (new_word)
    else:
        y = print ('Your word is NOT a palindrome.')
        return y

word = input('Introudce a word: ')
palindrome (word)

#%% EJERCICIO 179

# Create a square root function with two parameters. The first parameter, n, will
# be the number for which the square root is being computed. The second parameter,
# guess, will be the current guess for the square root. The guess parameter should have
# a default value of 1.0. Do not provide a default value for the first parameter.
# Your square root function will be recursive. The base case occurs when guess^2 is
# within 10−12 of n. In this case your function should return guess because it is close
# enough to the square root of n. Otherwise your function should return the result of
# calling itself recursively with n as the first parameter and FORMULA as the second parameter. 
# Write a main program that demonstrate your square root function by computing
# the square root of several different values. When you call your square root function
# from the main program you should only pass one parameter to it so that the default
# value is used for guess.

def square_root (n, guess=1.0):
    
    guess2 = guess**2
    num = float(n)
    
    if guess2-(10**(-12)) <= num and num <= guess2+(10**(-12)):
        return guess
    else:
        formula = (guess+num/guess)/2
        return square_root(n, formula)
    
n = input('Introduce a number to find the square root: ')
sr = square_root(n)
print (f'The square root of {n} is {sr}')

#%% EJERCICIO 180

# If the last character in s does not equal the last character in t then
# Set cost to 1
# Set d1 equal to the edit distance between all characters except the last one
# in s, and all characters in t, plus 1
# Set d2 equal to the edit distance between all characters in s, and all
# characters except the last one in t, plus 1
# Set d3 equal to the edit distance between all characters except the last one
# in s, and all characters except the last one in t, plus cost
# Return the minimum of d1, d2 and d3

def edit_distance (s, t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0
        if s[-1] != t[-1]:
            cost += 1
        d1 = edit_distance(s[0:-1], t) + 1
        d2 = edit_distance(s, t[0:-1]) + 1
        d3 = edit_distance(s[0:-1], t[0:-1]) + cost
        return min(d1, d2, d3)
    
s = input('Introduzca una palabra: ')
t = input('Introduzca otra palabra: ')
ed = edit_distance(s, t)
print (f'The edit distance is {ed}.')








    

    
    



































