---
layout: page
title: PythonCrashCourse_3.1-3.8_4.1-4.3_4.6_4.10_4.11
description: Python Basics 2
---

### 3.1


```python
names = ["eileen", "emma", "katelyn", "colby", "katie", "emily", "kristin"]
print(names[0], names[4])
```

    eileen katie
    

### 3.2


```python
for name in names:
    print("This person's name is " + name)
```

    This person's name is eileen
    This person's name is emma
    This person's name is katelyn
    This person's name is colby
    This person's name is katie
    This person's name is emily
    This person's name is kristin
    

### 3.3


```python
vehicles = ["car", 'electric bike', 'skateboard', 'scooter']
for vehicle in vehicles:
    print("you can get around using a " + vehicle)
```

    you can get around using a car
    you can get around using a electric bike
    you can get around using a skateboard
    you can get around using a scooter
    

### 3.4


```python
guests = ["rosa parks", "neil shusterman", "hayao miazaki"]
for guest in guests:
    print(guest.title() +  ", please join me for dinner!")
```

    Rosa Parks, please join me for dinner!
    Neil Shusterman, please join me for dinner!
    Hayao Miazaki, please join me for dinner!
    

### 3.5


```python
print(guests[1].title() + " can't make it")
```

    Neil Shusterman can't make it
    


```python
guests[1] = "tara westover"
for guest in guests:
    print(guest.title()+ ", join me for dinner")
```

    Rosa Parks, join me for dinner
    Tara Westover, join me for dinner
    Hayao Miazaki, join me for dinner
    

### 3.6


```python
print("I found a bigger table!")
guests.insert(0, "hilma klint")
guests.insert(2, "rebecca whiteread")
guests.append("theo jansen")
for guest in guests:
    print("Hi " + guest.title() + ", please join me for dinner!")
    
```

    I found a bigger table!
    Hi Hilma Klint, please join me for dinner!
    Hi Rosa Parks, please join me for dinner!
    Hi Rebecca Whiteread, please join me for dinner!
    Hi Tara Westover, please join me for dinner!
    Hi Hayao Miazaki, please join me for dinner!
    Hi Theo Jansen, please join me for dinner!
    

### 3.7


```python
print("Sorry, but I can only invite two guests")
```

    Sorry, but I can only invite two guests
    


```python
print("Sorry " + guests[0] + ", but you are uninvited")
guests.pop(0)
print("Sorry " + guests[0] + ", but you are uninvited")
guests.pop(0)
print("Sorry " + guests[0] + ", but you are uninvited")
guests.pop(0)
print("Sorry " + guests[0] + ", but you are uninvited")
guests.pop(0)

```

    Sorry hilma klint, but you are uninvited
    Sorry rosa parks, but you are uninvited
    Sorry rebecca whiteread, but you are uninvited
    Sorry tara westover, but you are uninvited
    




    'tara westover'




```python
guests
```




    ['hayao miazaki', 'theo jansen']




```python
for guest in guests:
    print("Hi " + guest.title() + ", you can still come")
```

    Hi Hayao Miazaki, you can still come
    Hi Theo Jansen, you can still come
    


```python
del guests[0]
del guests[0]
```


```python
guests
```




    []



### 3.8


```python
places  = ["Canada", "Mexico", "Honduras", "Greenland", "Nicaragua"]
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort()
places.reverse()
print(places)

```

    ['Canada', 'Mexico', 'Honduras', 'Greenland', 'Nicaragua']
    ['Canada', 'Greenland', 'Honduras', 'Mexico', 'Nicaragua']
    ['Canada', 'Mexico', 'Honduras', 'Greenland', 'Nicaragua']
    ['Nicaragua', 'Greenland', 'Honduras', 'Mexico', 'Canada']
    ['Canada', 'Mexico', 'Honduras', 'Greenland', 'Nicaragua']
    ['Canada', 'Greenland', 'Honduras', 'Mexico', 'Nicaragua']
    ['Nicaragua', 'Mexico', 'Honduras', 'Greenland', 'Canada']
    

### 4.1


```python
pizzas =  ["prosciutto", "pineapple", "veggie"]
for pizza in pizzas:
    print(pizza)
    
for pizza in pizzas:
    print("I like " + pizza + " pizza!")

print("I love all different kinds of pizza.")
print("Depending on the type of crust, I like different toppings. "+ pizzas[0].title() + " is great on thin crust.")
print("I could really go for some pizza right now")
```

    prosciutto
    pineapple
    veggie
    I like prosciutto pizza!
    I like pineapple pizza!
    I like veggie pizza!
    I love all different kinds of pizza.
    Depending on the type of crust, I like different toppings. Prosciutto is great on thin crust.
    I could really go for some pizza right now
    

### 4.2


```python
animals = ["seal", "whale", "dolphin"]
for sea_mammal in animals:
    print(sea_mammal)
    
for sea_mammal in animals:
    print("A " + sea_mammal + " needs to breathe oxygen")
    
print("All of these animals are mammals!")
```

    seal
    whale
    dolphin
    A seal needs to breathe oxygen
    A whale needs to breathe oxygen
    A dolphin needs to breathe oxygen
    All of these animals are mammals!
    

### 4.3


```python
numbers = list(range(1,21))
for number in numbers:
    print(number)
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    

### 4.6


```python
odd_nums = list(range(1,21,2))
for num in odd_nums:
    print(num)
```

    1
    3
    5
    7
    9
    11
    13
    15
    17
    19
    

### 4.10


```python
#str = str(odd_nums[:3])


print("the first three items in the list are: ")
for num in odd_nums[:3]:
    print((num))
    
#str = str(odd_nums[2:5])
print("three items from the middle of the list are: ")
for num in odd_nums[2:5]:
    print((num))
    
#str = str(odd_nums[-3:])
print("the last three items in the list are: ")
for num in odd_nums[-3:]:
    print((num))
```

    the first three items in the list are: 
    1
    3
    5
    three items from the middle of the list are: 
    5
    7
    9
    the last three items in the list are: 
    15
    17
    19
    

### 4.11


```python
friend_pizzas = pizzas[:]
friend_pizzas.append("olive")
print("my fav pizzas are ")
for za in pizzas:
    print(za)
print("my friend's fav pizzas are")
for za in friend_pizzas:
    print(za)
```

    my fav pizzas are 
    prosciutto
    pineapple
    veggie
    my friend's fav pizzas are
    prosciutto
    pineapple
    veggie
    olive
    


```python

```


```python

```
