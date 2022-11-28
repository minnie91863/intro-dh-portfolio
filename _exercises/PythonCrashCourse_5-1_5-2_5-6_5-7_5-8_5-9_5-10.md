---
layout: page
title: PythonCrashCourse_5-1_5-2_5-6_5-7_5-8_5-9_5-10
description: Python Basics 3
---

### 5-1


```python
snack = "chips"
print("is snack == 'chips'? I predict True.")
print (snack == "chips")

print("is snack == 'cookie'? I predict False.")
print (snack == "cookie")

snack = "pie"
print("is snack == 'pie'? I predict True.")
print (snack == "pie")

print("is snack == 'chips'? I predict False.")
print (snack == "chips")

snack = "apple"
print("is snack == 'apple'? I predict True.")
print (snack == "apple")

print("is snack == 'chips'? I predict False.")
print (snack == "chips")

snack = "goldfish"
print("is snack == 'goldfish'? I predict True.")
print (snack == "goldfish")

print("is snack == 'apple'? I predict False.")
print (snack == "apple")

snack = "cheese"
print("is snack == 'cheese'? I predict True.")
print (snack == "cheese")

print("is snack == 'pie'? I predict False.")
print (snack == "pie")
```

    is snack == 'chips'? I predict True.
    True
    is snack == 'cookie'? I predict False.
    False
    is snack == 'pie'? I predict True.
    True
    is snack == 'chips'? I predict False.
    False
    is snack == 'apple'? I predict True.
    True
    is snack == 'chips'? I predict False.
    False
    is snack == 'goldfish'? I predict True.
    True
    is snack == 'apple'? I predict False.
    False
    is snack == 'cheese'? I predict True.
    True
    is snack == 'pie'? I predict False.
    False
    

### 5-2


```python
str1 = "cat"
str2 = "dog"
print( "is str1 == str2? I predit False")
print(str1 == str2)

print( "is str1 == 'Cat'.lower()? I predict true")
print(str1 == 'Cat'.lower())

num1 = 1
num2 = 2
print(" is num1 == num2? I predict false")
print(num1 == num2)
print(" is num1 > num2? I predict false") 
print(num1 > num2)
print ("is num1 < num 2? I predict true")
print(num1 < num2)
print( "is num1 >= num2?  I predict false")
print(num1 >= num2)
print("is num1 <= num2? I predict true")
print(num1 <= num2)

c1 = "red"
c2 = "blue"
print("is c1 == c1 or c2? I predict true")
print(c1 == c1 or c2)
print("is c1 == c1 and c2? I predict false")
print(c1 == (c1 and c2))

list = [0,1,2,3]
print("is 0 in the list? I predict true")
print(0 in list)
        
print("is 8 in the list? I predict false")
print(8 in list)
```

    is str1 == str2? I predit False
    False
    is str1 == 'Cat'.lower()? I predict true
    True
     is num1 == num2? I predict false
    False
     is num1 > num2? I predict false
    False
    is num1 < num 2? I predict true
    True
    is num1 >= num2?  I predict false
    False
    is num1 <= num2? I predict true
    True
    is c1 == c1 or c2? I predict true
    True
    is c1 == c1 and c2? I predict false
    False
    is 0 in the list? I predict true
    True
    is 8 in the list? I predict false
    False
    

### 5-6


```python
age = 21
print("you are a ")
if age < 2:
    print("baby!")
elif age >= 2 and age < 4:
    print("toddler!")
elif age >= 4 and age < 13:
    print("kid!")
elif age >= 13 and age < 20:
    print("teen!")
elif age >= 20 and age < 65:
    print("adult")
elif age >= 65:
    print("elder!")
```

    you are a 
    adult
    

### 5-7


```python
favorite_fruits = ["lychee", "mango", "watermelon"]
if "apple" in favorite_fruits:
    print("You really like apple")
if "pear" in favorite_fruits:
    print("You really like pear")
if "mango" in favorite_fruits:
    print("You really like mango")
if "banana" in favorite_fruits:
    print("You really like banana")
if "lychee" in favorite_fruits:
    print("You really like lychee")
```

    You really like mango
    You really like lychee
    

### 5-8


```python
usernames = ["a", "b", "c", "d", "e", "admin"]
for name in usernames:
    print("Hello " + name.title())
    if name == "admin":
        print(" would you like to see a status report?")
    else:
        print(" thank you for loggin in again.")

```

    Hello A
     thank you for loggin in again.
    Hello B
     thank you for loggin in again.
    Hello C
     thank you for loggin in again.
    Hello D
     thank you for loggin in again.
    Hello E
     thank you for loggin in again.
    Hello Admin
     would you like to see a status report?
    

### 5-9


```python
usernames = ["a", "b", "c", "d", "e", "admin"]
usernames.clear()
if usernames:
    for name in usernames:
        print("Hello " + name.title())
        if name == "admin":
            print(" would you like to see a status report?")
        else:
            print(" thank you for loggin in again.")
    
else:
    print("we need to find some users")
```

    we need to find some users
    

###  5-10


```python
current_users = ["a", "b", "c", "d", "e"]
new_users = ["f",  "g", "h", "b", "a"]

for name in new_users:
    if name.lower() in current_users:
        print( name + ", choose a new name please")
    else:
        print("the username " + name + " is available")
```

    the username f is available
    the username g is available
    the username h is available
    b, choose a new name please
    a, choose a new name please
    


```python

```
