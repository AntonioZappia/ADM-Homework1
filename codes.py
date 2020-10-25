import textwrap
import string
import calendar
import math
import random
import os
import sys
from datetime import datetime
import re
from html.parser import HTMLParser
import xml.etree.ElementTree as etree
import numpy
from collections import OrderedDict
from collections import Counter
from collections import defaultdict
from collections import namedtuple

#### INTRODUCTION #####

## 1. Say "Hello, World!" With Python

print("Hello, World!")

## 2. Python If-Else

n=int(input().strip())

if n%2 != 0:
    print("Weird")
elif n%2 == 0 and 2<=n<= 5:
    print("Not Weird")
elif n%2 == 0 and 6<=n<=20:
    print("Weird")
elif n%2 == 0 and n>=20:
    print("Not Weird")

## 3. Arithmetic Operators


if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a+b)
print(a-b)
print(a*b)


##4. Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a//b)
print(a/b)


##5. Loops

if __name__ == '__main__':
    n = int(input())

for i in range(n):
    print(i**2)


##6. Write a function

def is_leap(year):
    leap = False
    if (year % 4 == 0):
        leap = True
        if (year % 100 == 0):
             leap = False
             if (year % 400 == 0):
                leap = True
    return leap

##7. Print a function

if __name__ == '__main__':
    n = int(input())
for i in range(1,n+1):
    print(i,end="")
    
#### BASIC DATA TYPES #####


##1. List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

lista=[]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if (i+j+k!=n):
                lista.append([i,j,k])

print(lista)

##2. Find the Runner-Up Score!

n = int(input())
arr = map(int, input().split())
listanodop=list(set(arr))
listafinale=sorted(listanodop)
print (listafinale[-2])

##3. Nested Lists

lista=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    lista.append([name,score])
score=list([marks for name, marks in lista])
secondo_valore=sorted(set(score))[1]
for name, score in sorted(lista):
    if score == secondo_valore:
        print(name)

##4. Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_score=student_marks[query_name]
    value=sum(query_score)/len(query_score)
    print("{0:.2f}".format(value))


##5. Lists

N=int(input())
lista=[]
for _ in range(N):
    command = input().split()
    if command[0] == "insert":
        lista.insert(int(command[1]),int(command[2]))
    elif command[0] == "remove":
        lista.remove(int(command[1]))
    elif command[0] == "append":
        lista.append(int(command[1]))
    elif command[0] == "sort":
        lista.sort()
    elif command[0] == "pop":
        lista.pop()
    elif command[0] == "reverse":
        lista.reverse()
    elif command[0] == "print":
        print(lista)


##6. Tuples

n = int(input())
integer_list = map(int, input().split())
t=tuple(integer_list)
print(hash(t))



#### STRING #####


##1. sWAP CASE

def swap_case(s):
    newstring= ""
    for i in s:
        if i.isupper():
            newstring += i.lower()
        elif i.islower():
            newstring += i.upper()
        else:
            newstring += i
    return newstring

##2. String Split and Join

def split_and_join(line):
    lista=line.split()
    result= "-".join(lista)
    return result

##3. What's your name?

def print_full_name(a, b):
    print(f"Hello {first_name} {last_name}! You just delved into python."

##4. Mutations

def mutate_string(string, position, character):
    new_string=s[:position] +character +s[position+1:]
    return new_string

##5. Find a string

def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count = count + 1
    return count

##6. String Validators

s = input()
print(any([char.isalnum() for char in s]))
print(any([char.isalpha() for char in s]))
print(any([char.isdigit() for char in s]))
print(any([char.islower() for char in s]))
print(any([char.isupper() for char in s]))

##7. Text Alignment

thickness = int(input()) 
c = 'H'

#Top Cone

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



##8. Text Wrap

def wrap(string, max_width):
    testodiviso = textwrap.fill(string, width= max_width)
    return testodiviso


##9. Designer Door Mat

n,m=map(int,input().split(" "))
for i in range(n):
    if i < (n-1)/2:
        print((".|."*(2*i+1)).center(m,"-"))
    if i == (n-1)/2:
        print("WELCOME".center(m,"-"))
    if i > (n-1)/2:
        print((".|."*(2*(n-1-i)+1)).center(m,"-"))


##10. String Formatting

def print_formatted(number):
    weidth=len((bin(n)[2:]))
    for i in range(1,n+1):
       decimal = str(i).rjust(weidth," ")
       octal = oct(i).replace("0o","").rjust(weidth," ")
       hexadecimal = hex(i).replace("0x","").rjust(weidth," ").upper()
       binary=bin(i).replace("0b","").rjust(weidth," ")
       print(decimal,octal,hexadecimal,binary)

##11. Alphabet Rangoli

import string
def print_rangoli(size):
    alphabet = string.ascii_lowercase
    for i in range(size-1, -size, -1):
        x = abs(i)
        stringa = alphabet[size-1:x:-1]+alphabet[x:size]
        print ("--"*x+ '-'.join(stringa)+"--"*x)

##12. Capitalize

def solve(s):
    for element in s.split():
        s=s.replace(element,element.capitalize())
    return s

##13. The Minion Game

def minion_game(string):
    vocali="AEIOU"
    KPOINTS=0
    SPOINTS=0
    N=len(s)
    for i in range(N):
        if string[i] in vocali:
            KPOINTS += len(s)-i
        else:
            SPOINTS += len(s)-i
    if KPOINTS > SPOINTS:
        print("Kevin", (KPOINTS))
    elif SPOINTS > KPOINTS:
        print("Stuart", (SPOINTS))
    else:
        print("Draw")

##14. Merge the tools!

def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        newstring=string[i:i+k]
        final=""
        for char in newstring:
            if char not in final:
                final += char
        print(final)


#### SETS #####

##1. Introduction to Sets

def average(array):
    average = sum(set(arr))/len(set(arr))
    return average

##2. No Idea!

n,m = input().split()
integer=input().split()
A=set(input().split())
B=set(input().split())
count=0
for i in integer:
    if i in A:
        count+=1
    if i in B:
        count-= 1
print(count)

##3. Symmetric Difference

M = int(input())
myset1 = set(map(int, input().split()))
N = int(input())
myset2 = set(map(int, input().split()))
res=sorted(list((myset1.symmetric_difference(myset2))))
for element in res:
    print (element)

##4. Set.add()

N=int(input())
city=set()
for i in range(N):
    city.add(input())
print(len(city))

##5. Set.discard().remove() & pop()

n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(N):
    command =input().split()
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))

##6. Set.union()

N=int(input())
set1=set(map(int, input().split()))
M=int(input())
set2=set(map(int, input().split()))
setfinale=set1.union(set2)
print(len(setfinale))

##7. Set.intersection()

N=int(input())
set1=set(map(int, input().split()))
M=int(input())
set2=set(map(int, input().split()))
setfinale=set1.intersection(set2)
print(len(setfinale))

##8. Set.difference()

N=int(input())
set1=set(map(int, input().split()))
M=int(input())
set2=set(map(int, input().split()))
setfinale=set1.difference(set2)
print(len(setfinale))

##9. Set.symmetric_difference()

N=int(input())
set1=set(map(int, input().split()))
M=int(input())
set2=set(map(int, input().split()))
setfinale=set1.symmetric_difference(set2)
print(len(setfinale))


##10. Set Mutations

N=int(input())
A=set(map(int, input().split()))
M=int(input())
for i in range(M):
    command= input().split()
    B=set(map(int, input().split()))
    if command[0] == "intersection_update":
        A.intersection_update(B)
    elif command[0] == "update":
        A.update(B)
    elif command[0] == "symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif command[0] == "difference_update":
        A.difference_update(B)

print(sum(A))

##11. The Captain's Room

n=int(input())
array=list(map(int,input().split()))
single=set()
multiple=set()
for element in array:
    if element in single:
        multiple.add(element)
    else:
        single.add(element)

diff=list(single.difference(multiple))
print (diff[0])

##12. Check Subset

T=int(input())
for i in range(T):
    N=int(input())
    setA=set(map(int, input().split()))
    M=int(input())
    setB=set(map(int, input().split()))
    if setA.issubset(setB):
        print(True)
    else:
        print(False)

##13. Check strict superset

A=set(map(int,input().split()))
n=int(input())
lista=[]
for _ in range(n):
    B=set(map(int, input().split()))
    lista.append(B)
result = True
for i in lista:
    if not A.issuperset(i):
        result = False

print(result)


#### COLLECTIONS ####

##1. Collections.Counter()

N=int(input())
shoes = Counter(map(int,input().split()))
money = 0
M = int(input())
for i in range(M):
    size, price=map(int,input().split())
    if shoes[size]:
        money += price
        shoes[size] = shoes[size] - 1

print(money)
    
##2. DefaultDict Tutorial

groupA = defaultdict(list)
n,m = map(int, input().split())
for i in range(1,n+1):
    groupA[input()].append(str(i))

for element in range(m):
    print(' '.join((groupA[input()])) or -1)

##3. Collections.namedtuple()

N=int(input())
columns=input().split()
Student=namedtuple("student", columns)
somma=0
for _ in range(N):
    column1,column2,column3,column4 = input().split()
    student=Student( column1,column2,column3,column4)
    somma += int(student.MARKS)

media = (somma/N)
print(media)

##4. Collections.OrderedDict()
          
n=int(input())
d=OrderedDict()
for _ in range(n):
    item1,item2,price = input().rpartition(" ")
    if item1 in d.keys():
        d[item1] += int(price)
    else:
        d[item1] = int(price)

for item1,price in d.items():
    print(item1,price)


##5. Word Order

N=int(input())
d= OrderedDict()
for _ in range(N):
    line = input()
    d[line] = d.get(line,0) + 1

print(len(d))
print(*d.values())

##6. Collections.deque()

N=int(input())
d=deque()
for _ in range(N):
    command, *number= input().split()
    getattr(d, command)(*number)

for element in d:
    print(element, end=" ")

##7. Company Logo

s = input()
from collections import Counter
d=Counter(sorted(s))
new_d=d.most_common(3)
for char,number in new_d:
    print(char,number)

##8. Piling Up!

t=int(input())
for i in range(t):
    cubes=int(input())
    lista = list(map(int, input().split()))
    l = len(lista)
    k = 0
    while k < l - 1 and lista[k] >= lista[k+1]:
        k += 1
    while k < l - 1 and lista[k] <= lista[k+1]:
        k += 1
    if k == l-1:
        print("Yes")
    else:
        print("No")


#### DATE AND TIME ####

##1. Calendar Module

mese,giorno,anno = map(int,input().split())
giorno = calendar.day_name[calendar.weekday(anno,mese,giorno)] #con calendar weekday trovo un numero dove 0 è lunedi 1 martedi ecc.. con calendar.day_name associo il numero al giorno
print(giorno.upper())


##2. Time Delta

def time_delta(t1, t2):
    first_time=datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    second_time=datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    return str(int(abs(first_time-second_time).total_seconds()))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()



#### ERRORS AND EXCEPTIONS ####

##1. Exceptions

n=int(input())
for _ in range(n):
    try:
        a,b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except  ValueError as e:
        print("Error Code:", e)


#### BUILT-INS ####

##1. Zipped!

N,X =map(int, input().split())
lista=[]
match=[]
for _ in range(X):
    lista.append(map(float, input().split()))

for i in zip(*(lista)):
    average = sum(i)/len(i)
    print(average)

##2. Athlete Sort

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr=[]

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
arr_ordinata= sorted(arr, key=lambda x:x[k])
for element in arr_ordinata:
    print(*element)

##3. ginortS

string=input()
minuscole=[]
maiuscole=[]
pari=[]
dispari=[]
for i in (string):
    if i.isalpha():
        if i.isupper():
            maiuscole.append(i)
        else:
            minuscole.append(i)
    if i.isdigit():
        if(int(i)%2)==0:
            pari.append(i)
        else:
            dispari.append(i)
minuscole1=sorted(minuscole)
maiuscole1=sorted(maiuscole)
dispari1=sorted(dispari)
pari1=sorted(pari)
newlist = minuscole1+maiuscole1+dispari1+pari1

print("".join(newlist))


#### PYTHON FUNCTIONALS ####

##1. Map and Lambda Function

cube = lambda x: x**3
def fibonacci(n):
    lista=[0,1]
    for i in range(2,n):
        lista.append(lista[i-1] + lista[i-2])
    return (lista[:n])


#### REGEX AND PARSING


##1. Detect Floating Point Number

N=int(input())
for _ in range(N):
    
    m = re.match(r"^[\.+-]?[0-9]*\.[0-9]{1,}$", input())
    if m:
        print(True)
    else:
        print(False)

##2. Re.split()

regex_pattern = r"[,.]"

##3. Group(), groups(), groupdict()

m=re.search(r"([a-zA-Z0-9])\1+", input().strip())
if m:
    print(m.group(1))
else:
    print(-1)

##4. Re.findall(), Re.finditer()

consonanti = "[bcdfghlmnpqrstvzkjyw]"

m= re.findall(r"(?<=" + consonanti + ")([aeiou]{2,})" + consonanti, input(), re.I)
if m:
    print("\n".join(m))
else:
    print(-1)

##5. Re.start(), Re.end()

stringa=input() 
stringa2=input()
pattern=re.compile(stringa2)
m= pattern.search(stringa) 
if not m: print("(-1, -1)") 
while m:  
    print ("({0}, {1})".format(m.start(),m.end()-1))
    m=pattern.search(stringa, m.start() +1) 

##6. Regex Substitution

N=int(input())
for _ in range(N):
    m=re.sub(r"(?<=\s)\&\&\s", "and ", re.sub("\s\|\|\s", " or ", input()))
    print(m)

##7. Validating Roman Numerals

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

##8. Validating Phone Numbers

N=int(input())
for _ in range(N):
    m=re.search(r"^[7,8,9]" + "[0-9]{9}$", input().strip())
    if m:
        print("YES")
    else:
        print("NO")

##9. Validating and Parsing Email Addresses

N=int(input())
for _ in range(N):
    name, email = input().split()
    m=re.match(r"<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>", email)
    if m:
        print( name, email)

##10. Hex Colore Code

N=int(input())
for _ in range(N):
    m=re.findall(r"[:\s](#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3})", input())
    if m:
        print (*m, sep="\n")

##11. HTML Parser 1

N=int(input())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for element in attrs:
            print( "->",element[0],">",element[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag,attrs):
        print("Empty :", tag)
        for element in attrs:
            print( "->",element[0],">",element[1])

parser= MyHTMLParser()
parser.feed("".join([input().strip() for _ in range(N)]))

##12. HTML Parser 2

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)
    def handle_comment(self,data):
        lunghezza=len(data.split("\n"))
        if lunghezza == 1:
            print( ">>> Single-line Comment")
            print(data)
        elif lunghezza > 1:
            print(">>> Multi-line Comment")
            print(data)
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

##13. Detect HTML Tags, Attributes and Attribute Values

N=int(input())
class MYHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(tag)
        for element in attrs:
            print("->", element[0],">", element[1])
        
parser=MYHTMLParser()
parser.feed("".join([input() for _ in range(N)]))


##14. Validating UID

N=int(input())
for _ in range(N):
    line="".join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', line)
        assert re.search(r'[0-9]{3}', line)
        assert not re.search(r'[^a-zA-Z0-9]', line)
        assert not re.search(r'(.)\1', line)
        assert len(line) == 10
    except:
        print('Invalid')
    else:
        print('Valid')


##15. Validating Credit Card

N=int(input())
for _ in range(N):
    number=input()
    try:
        assert re.match(r"(\d{4}-){3}(\d{4})$", number) or re.match(r"[\d]{16}", number)
        assert not re.search(r"([\d])\1\1\1", number.replace("-",""))
        assert re.match(r"[456]", number)
    except:
        print("Invalid")
    else:
        print("Valid")

##16. Validating Postal Codes

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"


#### XML ####

##1. XML 1 Find The Score

def get_attr_number(node):
    count = 0 
    for i in node.iter():
        count += len(i.attrib)
    return countdef get_attr_number(node):
    count = 0 
    for i in node.iter():
        count += len(i.attrib)
    return count

##2. XML 2 Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if level >= maxdepth :
        maxdepth += 1 
    for i in elem:
        depth(i,level+1)
    maxdepth = 0
def depth(elem, level):
    global maxdepth
    if level >= maxdepth :
        maxdepth += 1 
    for i in elem:
        depth(i,level+1)

#### CLOSURES AND DECORATORS

##1. Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        f("+91 " + number[-10: -5]+" "+number[-5:] for number in l)
    return fun

##2. Decoretors 2 Name Directory

def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key= lambda person: int(person[2])))
    return inner

#### NUMPY ####

##1. Arrays

def arrays(arr):
    a=numpy.array(arr,float)
    return a[::-1]

##2. Shape and Reshape

array=list(map(int, input().split()))
new=numpy.reshape(array,(3,3))
print(new)

##3. Transpose and Flatten

n,m = map(int, input().split())
array=numpy.array([input().split() for _ in range(n)], int)

print(numpy.transpose(array))
print(array.flatten())

##4. Concatenate

n,m,p = map(int, input().split())
array1= numpy.array([input().split() for _ in range (n)], int)
array2= numpy.array([input().split() for _ in range (m)], int)
print(numpy.concatenate((array1,array2), axis = 0))

##5. Zeros and Ones

number = tuple(map(int,input().split()))
array1 = numpy.zeros((number), dtype=int)
array2 = numpy.ones((number), dtype=int)

print(array1)
print(array2)


##6. Eye and Identtity

numpy.set_printoptions(legacy='1.13')
rows, columns = map(int, input().split())
print(numpy.eye(rows,columns))


##7. Array Mathematics

n,m=map(int,input().split())
array1=numpy.array([input().split() for _ in range(n)],int)
array2=numpy.array([input().split() for _ in range(n)],int)
print(numpy.add(array1,array2))
print(numpy.subtract(array1,array2))
print(numpy.multiply(array1,array2))
print(array1//array2)
print(numpy.mod(array1,array2))
print(numpy.power(array1,array2))

##8. Floor, Ceil and Rint

numpy.set_printoptions(legacy='1.13')
array=numpy.array(input().split(),float)
print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))

##9. Sum and Prod

n,m=map(int,input().split())
array= numpy.array([input().split() for _ in range(n)],int)
somma = numpy.sum(array, axis=0)
print(numpy.prod(somma,axis=0))

##10. Min and Max

n,m=map(int,input().split())
array=numpy.array([input().split() for _ in range(n)],int)
minimo=numpy.min(array,axis=1)
print(numpy.max(minimo))

##11. Mean, Var and Std

numpy.set_printoptions(legacy="1.13")
n,m=map(int, input().split())
array=numpy.array([input().split() for _ in range(n)],int)
print(numpy.mean(array, axis=1))
print(numpy.var(array, axis=0))
print(numpy.std(array, axis=None))

##12. Dot and Cross

n=int(input())
arrayA=numpy.array([input().split() for _ in range(n)],int)
arrayB=numpy.array([input().split() for _ in range(n)],int)
D=numpy.dot(arrayA,arrayB)
print(D)

##13. Inner and Outer

arrayA=numpy.array([input().split()],int)
arrayB=numpy.array([input().split()],int)
INN=numpy.inner(arrayA,arrayB)
OUT=numpy.outer(arrayA,arrayB)
print(int(INN))
print(OUT)

##14. Polynomials

coefficent = list(map(float, input().split()))
x= int(input())

desirevalue=numpy.polyval(coefficent, x)
print(desirevalue)

##15. Linear Algebra

n=int(input())
array=numpy.array([input().split() for _ in range(n)], float)
determinante =numpy.linalg.det(array)
print (round(determinante, 2))

### OTHER EXERCISE ####

##1. Number Line Jumps

def kangaroo(x1, v1, x2, v2):
    if (x1 != x2) and (v1 == v2):
        return "NO"
    if (x1 == x2) and (v1 != v2):
        return "NO"
    if (x1 < x2) and (v1 < v2):
        return "NO"
    if (x1 > x2) and (v1 < v2):
        return "NO"
    if (x2-x1)%(v2-v1) != 0 :
        return "NO"
    else:
        return "YES"

##2. Viral Advertising

def viralAdvertising(n):
    shared=[5]
    liked =[]
    for i in range(n-1):
        shared.append(int(shared[i]/2)*3)
    for element in shared:
        liked.append(int(element/2))
    return(sum(liked))

##3. Birthday Cake Candles

def birthdayCakeCandles(candles):
    maximum= max(candles)
    return candles.count(maximum)


##4. Insertion Sort Part 1

def insertionSort1(n, arr):
    element = arr[-1]
    index = n-2
    while (arr[index] > element) and (index >= 0):
        arr[index+1] = arr[index]
        print(' '.join(map(str, arr)))
        index = index - 1  
    arr[index+1] = element
    print(' '.join(map(str, arr)))

##5. Insertion Sort Part 2

def insertionSort2(n, arr):
    for i in range(1,n):
        for j in range(i):
            if j >= 0 and arr[i] < arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
        print(*arr)

##6. Recursive Digit Sum

def superDigit(n, k):
    if len(n) ==1:
        return n
    somma=0
    for element in n:
        somma += int(element)
    return superDigit(str(somma*k), 1)





    
