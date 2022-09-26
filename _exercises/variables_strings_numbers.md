---
layout: page
title: Variables, Strings, and Numbers
description: This notebook has code about variables, strings, and numbers (class demo).
---

# Variables


```python
greeting = "Hello World!"
```


```python
print(greeting)
```

    Hello World!
    


```python
ice_cream = "yummers"
print(ice_cream)
```

    yummers
    


```python
ice_cream = "even more yummers"
print(ice_cream)
```

    even more yummers
    


```python
ex_1 = "this is a string"
print(ex_1)
```

    this is a string
    


```python
ex_2 =  'this is also a string and not a char for some reason'
print(ex_2)
```

    this is also a string and not a char for some reason
    


```python
ex_3 = "here  is a string'
print(ex_3)
```


      Input In [9]
        ex_3 = "here  is a string'
                                  ^
    SyntaxError: EOL while scanning string literal
    



```python
ex_4 = "I asked the question, \"when should I use single quotes?\""
print(ex_4)
```

    I asked the question, "when should I use single quotes?"
    


```python
historian = "edward gibbon"
print(historian)
```

    edward gibbon
    


```python
print(historian.title())
```

    Edward Gibbon
    


```python
novelist = "Becky Chambers"
print(novelist.lower())
```

    becky chambers
    


```python
"becky" == "becky"
```




    True




```python
"becky"  == "Becky"
```




    False




```python
first_name = "ada"
last_name = "lovelace"
```


```python
full_name = first_name + " " + last_name
print(full_name)
```

    ada lovelace
    


```python
greeting = f"Hello {first_name} {last_name}"
print(greeting)
```

    Hello ada lovelace
    

## Whitespace


```python
print("tab")
```

    tab
    


```python
print("\ttab")
```

    	tab
    


```python
print("Languages: \nGreek \nLatin \nEngish")
```

    Languages: 
    Greek 
    Latin 
    Engish
    


```python
str_rspace = "strirng     "
print(str_rspace)
```

    strirng     
    


```python
print(str_rspace.rstrip())
```

    strirng
    


```python
example = str_rspace + "@"
```


```python
print(example)

```

    strirng     @
    


```python
example2 = str_rspace.rstrip() + "@"
print(example2)
```

    strirng@
    

## Numbers


```python
# ints
```


```python
238 + 4000 + 834
```




    5072




```python
19 - 7
```




    12




```python
54  * 123123123

```




    6648648642




```python
type  (example)

```




    str




```python
30 / 10

```




    3.0




```python
f  = 30 / 7
f
```




    4.285714285714286




```python
f
```




    4.285714285714286




```python
tyep (f)

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Input In [17], in <cell line: 1>()
    ----> 1 tyep (f)
    

    NameError: name 'tyep' is not defined



```python
type(f)
```




    float




```python
5 **3

```




    125



# Lists


```python
subjects = ['classics', 'history', 'philosophy']

```


```python
print(subjects)
```

    ['classics', 'history', 'philosophy']
    


```python
print(subjects[0])
```

    classics
    


```python
print(subjects[2])
```

    philosophy
    


```python
print(subjects[-1])
```

    philosophy
    


```python
print(subjects[-3])
```

    classics
    


```python
message = f"My most difficult subject is {subjects[1].title()}."
print(message)
```

    My most difficult subject is History.
    


```python
# how to mod a list
```


```python
print(subjects)
```

    ['classics', 'history', 'philosophy']
    


```python
subjects[1] = "sociology"

```


```python
print(subjects)

```

    ['classics', 'sociology', 'philosophy']
    


```python
# append
```


```python
subjects.append("history")
print(subjects)
subjects.append("linguistics")
```

    ['classics', 'sociology', 'philosophy', 'history']
    


```python
print(subjects)

```

    ['classics', 'sociology', 'philosophy', 'history', 'linguistics']
    


```python
# insert
```


```python
subjects.insert(0, 'religion')
print(subjects)
```

    ['religion', 'classics', 'sociology', 'philosophy', 'history', 'linguistics']
    


```python
subjects.insert(2, "literature")
```


```python
print(subjects)

```

    ['religion', 'classics', 'literature', 'sociology', 'philosophy', 'history', 'linguistics']
    


```python
# delete items
```


```python
del subjects[-1]
print(subjects)

```

    ['religion', 'classics', 'literature', 'sociology', 'philosophy', 'history']
    


```python
# pop method
```


```python
popped_subject = subjects.pop(0)
print(popped_subject)
```

    religion
    


```python
print(subjects)

```

    ['classics', 'literature', 'sociology', 'philosophy', 'history']
    


```python
# remove
subjects.remove("sociology")
print(subjects)
```

    ['classics', 'literature', 'philosophy', 'history']
    


```python

```
