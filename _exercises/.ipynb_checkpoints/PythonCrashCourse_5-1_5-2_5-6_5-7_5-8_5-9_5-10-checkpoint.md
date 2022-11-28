{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0b848d1e",
   "metadata": {},
   "source": [
    "### 5-1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "14f306f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is snack == 'chips'? I predict True.\n",
      "True\n",
      "is snack == 'cookie'? I predict False.\n",
      "False\n",
      "is snack == 'pie'? I predict True.\n",
      "True\n",
      "is snack == 'chips'? I predict False.\n",
      "False\n",
      "is snack == 'apple'? I predict True.\n",
      "True\n",
      "is snack == 'chips'? I predict False.\n",
      "False\n",
      "is snack == 'goldfish'? I predict True.\n",
      "True\n",
      "is snack == 'apple'? I predict False.\n",
      "False\n",
      "is snack == 'cheese'? I predict True.\n",
      "True\n",
      "is snack == 'pie'? I predict False.\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "snack = \"chips\"\n",
    "print(\"is snack == 'chips'? I predict True.\")\n",
    "print (snack == \"chips\")\n",
    "\n",
    "print(\"is snack == 'cookie'? I predict False.\")\n",
    "print (snack == \"cookie\")\n",
    "\n",
    "snack = \"pie\"\n",
    "print(\"is snack == 'pie'? I predict True.\")\n",
    "print (snack == \"pie\")\n",
    "\n",
    "print(\"is snack == 'chips'? I predict False.\")\n",
    "print (snack == \"chips\")\n",
    "\n",
    "snack = \"apple\"\n",
    "print(\"is snack == 'apple'? I predict True.\")\n",
    "print (snack == \"apple\")\n",
    "\n",
    "print(\"is snack == 'chips'? I predict False.\")\n",
    "print (snack == \"chips\")\n",
    "\n",
    "snack = \"goldfish\"\n",
    "print(\"is snack == 'goldfish'? I predict True.\")\n",
    "print (snack == \"goldfish\")\n",
    "\n",
    "print(\"is snack == 'apple'? I predict False.\")\n",
    "print (snack == \"apple\")\n",
    "\n",
    "snack = \"cheese\"\n",
    "print(\"is snack == 'cheese'? I predict True.\")\n",
    "print (snack == \"cheese\")\n",
    "\n",
    "print(\"is snack == 'pie'? I predict False.\")\n",
    "print (snack == \"pie\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5b4f2724",
   "metadata": {},
   "source": [
    "### 5-2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1f72a661",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is str1 == str2? I predit False\n",
      "False\n",
      "is str1 == 'Cat'.lower()? I predict true\n",
      "True\n",
      " is num1 == num2? I predict false\n",
      "False\n",
      " is num1 > num2? I predict false\n",
      "False\n",
      "is num1 < num 2? I predict true\n",
      "True\n",
      "is num1 >= num2?  I predict false\n",
      "False\n",
      "is num1 <= num2? I predict true\n",
      "True\n",
      "is c1 == c1 or c2? I predict true\n",
      "True\n",
      "is c1 == c1 and c2? I predict false\n",
      "False\n",
      "is 0 in the list? I predict true\n",
      "True\n",
      "is 8 in the list? I predict false\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "str1 = \"cat\"\n",
    "str2 = \"dog\"\n",
    "print( \"is str1 == str2? I predit False\")\n",
    "print(str1 == str2)\n",
    "\n",
    "print( \"is str1 == 'Cat'.lower()? I predict true\")\n",
    "print(str1 == 'Cat'.lower())\n",
    "\n",
    "num1 = 1\n",
    "num2 = 2\n",
    "print(\" is num1 == num2? I predict false\")\n",
    "print(num1 == num2)\n",
    "print(\" is num1 > num2? I predict false\") \n",
    "print(num1 > num2)\n",
    "print (\"is num1 < num 2? I predict true\")\n",
    "print(num1 < num2)\n",
    "print( \"is num1 >= num2?  I predict false\")\n",
    "print(num1 >= num2)\n",
    "print(\"is num1 <= num2? I predict true\")\n",
    "print(num1 <= num2)\n",
    "\n",
    "c1 = \"red\"\n",
    "c2 = \"blue\"\n",
    "print(\"is c1 == c1 or c2? I predict true\")\n",
    "print(c1 == c1 or c2)\n",
    "print(\"is c1 == c1 and c2? I predict false\")\n",
    "print(c1 == (c1 and c2))\n",
    "\n",
    "list = [0,1,2,3]\n",
    "print(\"is 0 in the list? I predict true\")\n",
    "print(0 in list)\n",
    "        \n",
    "print(\"is 8 in the list? I predict false\")\n",
    "print(8 in list)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "df2931d3",
   "metadata": {},
   "source": [
    "### 5-6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "997cf038",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you are a \n",
      "adult\n"
     ]
    }
   ],
   "source": [
    "age = 21\n",
    "print(\"you are a \")\n",
    "if age < 2:\n",
    "    print(\"baby!\")\n",
    "elif age >= 2 and age < 4:\n",
    "    print(\"toddler!\")\n",
    "elif age >= 4 and age < 13:\n",
    "    print(\"kid!\")\n",
    "elif age >= 13 and age < 20:\n",
    "    print(\"teen!\")\n",
    "elif age >= 20 and age < 65:\n",
    "    print(\"adult\")\n",
    "elif age >= 65:\n",
    "    print(\"elder!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2c23690a",
   "metadata": {},
   "source": [
    "### 5-7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2e532dd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You really like mango\n",
      "You really like lychee\n"
     ]
    }
   ],
   "source": [
    "favorite_fruits = [\"lychee\", \"mango\", \"watermelon\"]\n",
    "if \"apple\" in favorite_fruits:\n",
    "    print(\"You really like apple\")\n",
    "if \"pear\" in favorite_fruits:\n",
    "    print(\"You really like pear\")\n",
    "if \"mango\" in favorite_fruits:\n",
    "    print(\"You really like mango\")\n",
    "if \"banana\" in favorite_fruits:\n",
    "    print(\"You really like banana\")\n",
    "if \"lychee\" in favorite_fruits:\n",
    "    print(\"You really like lychee\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "02a20827",
   "metadata": {},
   "source": [
    "### 5-8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ccc4c441",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello A\n",
      " thank you for loggin in again.\n",
      "Hello B\n",
      " thank you for loggin in again.\n",
      "Hello C\n",
      " thank you for loggin in again.\n",
      "Hello D\n",
      " thank you for loggin in again.\n",
      "Hello E\n",
      " thank you for loggin in again.\n",
      "Hello Admin\n",
      " would you like to see a status report?\n"
     ]
    }
   ],
   "source": [
    "usernames = [\"a\", \"b\", \"c\", \"d\", \"e\", \"admin\"]\n",
    "for name in usernames:\n",
    "    print(\"Hello \" + name.title())\n",
    "    if name == \"admin\":\n",
    "        print(\" would you like to see a status report?\")\n",
    "    else:\n",
    "        print(\" thank you for loggin in again.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb02df7b",
   "metadata": {},
   "source": [
    "### 5-9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "ef3e7aa4",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (950202153.py, line 5)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [22]\u001b[1;36m\u001b[0m\n\u001b[1;33m    if\u001b[0m\n\u001b[1;37m      ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "usernames = [\"a\", \"b\", \"c\", \"d\", \"e\", \"admin\"]\n",
    "usernames.clear()\n",
    "if usernames:\n",
    "    for name in usernames:\n",
    "        if\n",
    "        print(\"Hello \" + name.title())\n",
    "        if name == \"admin\":\n",
    "            print(\" would you like to see a status report?\")\n",
    "        else:\n",
    "            print(\" thank you for loggin in again.\")\n",
    "    \n",
    "else:\n",
    "    print(\"we need to find some users\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "674187a9",
   "metadata": {},
   "source": [
    "###  5-10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "5de81d1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b, choose new name please\n",
      "a, choose new name please\n"
     ]
    }
   ],
   "source": [
    "current_users = [\"a\", \"b\", \"c\", \"d\", \"e\"]\n",
    "new_users = [\"f\",  \"g\", \"h\", \"b\", \"a\"]\n",
    "\n",
    "for name in new_users:\n",
    "    if name in current_users:\n",
    "        print( name + \", choose new name please\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43ab8d88",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
