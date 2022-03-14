#Functional Programming

def greetings():
    print("Hello World")

greetings()
#########################################
def perkalian(x):
    return x*x

print(perkalian(6))
#########################################
def formalGreeting():
    print("How are you?")

def casualGreeting():
    print("What's up?")

def greet(type, greetFormal, greetCasual):
    if(type == 'formal'):
        greetFormal()
    elif(type == 'casual'):
        greetCasual()

greet('casual', formalGreeting, casualGreeting)
#########################################
def item(x):
    return x*2

arr1 = 1,2,3
arr2 = map(item, arr1)

print(list(arr2))
#########################################
def umur(tahun):
    return 2022 - tahun

lahir = 2002, 1998, 1995, 2001
hasil = map(umur, lahir)

print(list(hasil))
#########################################
from array import *
data = [
    {
        "Name" : 'Pete', 
        "age" : 16
    }, 
    {
        "Name" : 'Mark', 
        "age" : 18
    }, 
    {
        "Name" : 'John', 
        "age" : 27
    }, 
    {
        "Name" : 'Jane', 
        "age" : 14
    }, 
    {
        "Name" : 'Tony', 
        "age" : 24
    }
]
print("Data Awal:")
print(data)
titip = []
for i in range(len(data)):
    if data[i]["age"] < 18:
        titip.append(i)
for i in range(len(titip)):
    titip[i] -= i
print(titip)

for i in range(len(titip)):
    data.pop(titip[i])
print("Data Akhir:")
print(data)
#########################################
