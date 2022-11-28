{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ffaf695f",
   "metadata": {},
   "source": [
    "---\n",
    "layout: page\n",
    "title: PythonCrashCourse_3.1-3.8_4.1-4.3_4.6_4.10_4.11\n",
    "description: Python Basics 2\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f4e68bf0",
   "metadata": {},
   "source": [
    "### 3.1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f10a4daf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "eileen katie\n"
     ]
    }
   ],
   "source": [
    "names = [\"eileen\", \"emma\", \"katelyn\", \"colby\", \"katie\", \"emily\", \"kristin\"]\n",
    "print(names[0], names[4])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5e67849d",
   "metadata": {},
   "source": [
    "### 3.2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d5f75869",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This person's name is eileen\n",
      "This person's name is emma\n",
      "This person's name is katelyn\n",
      "This person's name is colby\n",
      "This person's name is katie\n",
      "This person's name is emily\n",
      "This person's name is kristin\n"
     ]
    }
   ],
   "source": [
    "for name in names:\n",
    "    print(\"This person's name is \" + name)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2ee4a981",
   "metadata": {},
   "source": [
    "### 3.3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b1ae8911",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you can get around using a car\n",
      "you can get around using a electric bike\n",
      "you can get around using a skateboard\n",
      "you can get around using a scooter\n"
     ]
    }
   ],
   "source": [
    "vehicles = [\"car\", 'electric bike', 'skateboard', 'scooter']\n",
    "for vehicle in vehicles:\n",
    "    print(\"you can get around using a \" + vehicle)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "38b76857",
   "metadata": {},
   "source": [
    "### 3.4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "bce8e98c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rosa Parks, please join me for dinner!\n",
      "Neil Shusterman, please join me for dinner!\n",
      "Hayao Miazaki, please join me for dinner!\n"
     ]
    }
   ],
   "source": [
    "guests = [\"rosa parks\", \"neil shusterman\", \"hayao miazaki\"]\n",
    "for guest in guests:\n",
    "    print(guest.title() +  \", please join me for dinner!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e259adb",
   "metadata": {},
   "source": [
    "### 3.5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "58091e8b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Neil Shusterman can't make it\n"
     ]
    }
   ],
   "source": [
    "print(guests[1].title() + \" can't make it\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "1f7b8ed2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rosa Parks, join me for dinner\n",
      "Tara Westover, join me for dinner\n",
      "Hayao Miazaki, join me for dinner\n"
     ]
    }
   ],
   "source": [
    "guests[1] = \"tara westover\"\n",
    "for guest in guests:\n",
    "    print(guest.title()+ \", join me for dinner\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dd72f297",
   "metadata": {},
   "source": [
    "### 3.6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "85598492",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I found a bigger table!\n",
      "Hi Hilma Klint, please join me for dinner!\n",
      "Hi Rosa Parks, please join me for dinner!\n",
      "Hi Rebecca Whiteread, please join me for dinner!\n",
      "Hi Tara Westover, please join me for dinner!\n",
      "Hi Hayao Miazaki, please join me for dinner!\n",
      "Hi Theo Jansen, please join me for dinner!\n"
     ]
    }
   ],
   "source": [
    "print(\"I found a bigger table!\")\n",
    "guests.insert(0, \"hilma klint\")\n",
    "guests.insert(2, \"rebecca whiteread\")\n",
    "guests.append(\"theo jansen\")\n",
    "for guest in guests:\n",
    "    print(\"Hi \" + guest.title() + \", please join me for dinner!\")\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc552d88",
   "metadata": {},
   "source": [
    "### 3.7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "7f0c5491",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sorry, but I can only invite two guests\n"
     ]
    }
   ],
   "source": [
    "print(\"Sorry, but I can only invite two guests\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "46dd53d1",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sorry hilma klint, but you are uninvited\n",
      "Sorry rosa parks, but you are uninvited\n",
      "Sorry rebecca whiteread, but you are uninvited\n",
      "Sorry tara westover, but you are uninvited\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'tara westover'"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(\"Sorry \" + guests[0] + \", but you are uninvited\")\n",
    "guests.pop(0)\n",
    "print(\"Sorry \" + guests[0] + \", but you are uninvited\")\n",
    "guests.pop(0)\n",
    "print(\"Sorry \" + guests[0] + \", but you are uninvited\")\n",
    "guests.pop(0)\n",
    "print(\"Sorry \" + guests[0] + \", but you are uninvited\")\n",
    "guests.pop(0)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "6aee62af",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['hayao miazaki', 'theo jansen']"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "guests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "820babc2",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi Hayao Miazaki, you can still come\n",
      "Hi Theo Jansen, you can still come\n"
     ]
    }
   ],
   "source": [
    "for guest in guests:\n",
    "    print(\"Hi \" + guest.title() + \", you can still come\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "0b8d647e",
   "metadata": {},
   "outputs": [],
   "source": [
    "del guests[0]\n",
    "del guests[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "id": "910208d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 136,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "guests"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f0ea4955",
   "metadata": {},
   "source": [
    "### 3.8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "274b509e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Canada', 'Mexico', 'Honduras', 'Greenland', 'Nicaragua']\n",
      "['Canada', 'Greenland', 'Honduras', 'Mexico', 'Nicaragua']\n",
      "['Canada', 'Mexico', 'Honduras', 'Greenland', 'Nicaragua']\n",
      "['Nicaragua', 'Greenland', 'Honduras', 'Mexico', 'Canada']\n",
      "['Canada', 'Mexico', 'Honduras', 'Greenland', 'Nicaragua']\n",
      "['Canada', 'Greenland', 'Honduras', 'Mexico', 'Nicaragua']\n",
      "['Nicaragua', 'Mexico', 'Honduras', 'Greenland', 'Canada']\n"
     ]
    }
   ],
   "source": [
    "places  = [\"Canada\", \"Mexico\", \"Honduras\", \"Greenland\", \"Nicaragua\"]\n",
    "print(places)\n",
    "print(sorted(places))\n",
    "print(places)\n",
    "places.reverse()\n",
    "print(places)\n",
    "places.reverse()\n",
    "print(places)\n",
    "places.sort()\n",
    "print(places)\n",
    "places.sort()\n",
    "places.reverse()\n",
    "print(places)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6f8855f5",
   "metadata": {},
   "source": [
    "### 4.1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1ae0b95c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "prosciutto\n",
      "pineapple\n",
      "veggie\n",
      "I like prosciutto pizza!\n",
      "I like pineapple pizza!\n",
      "I like veggie pizza!\n",
      "I love all different kinds of pizza.\n",
      "Depending on the type of crust, I like different toppings. Prosciutto is great on thin crust.\n",
      "I could really go for some pizza right now\n"
     ]
    }
   ],
   "source": [
    "pizzas =  [\"prosciutto\", \"pineapple\", \"veggie\"]\n",
    "for pizza in pizzas:\n",
    "    print(pizza)\n",
    "    \n",
    "for pizza in pizzas:\n",
    "    print(\"I like \" + pizza + \" pizza!\")\n",
    "\n",
    "print(\"I love all different kinds of pizza.\")\n",
    "print(\"Depending on the type of crust, I like different toppings. \"+ pizzas[0].title() + \" is great on thin crust.\")\n",
    "print(\"I could really go for some pizza right now\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9d6f0fdc",
   "metadata": {},
   "source": [
    "### 4.2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c7f3f74d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "seal\n",
      "whale\n",
      "dolphin\n",
      "A seal needs to breathe oxygen\n",
      "A whale needs to breathe oxygen\n",
      "A dolphin needs to breathe oxygen\n",
      "All of these animals are mammals!\n"
     ]
    }
   ],
   "source": [
    "animals = [\"seal\", \"whale\", \"dolphin\"]\n",
    "for sea_mammal in animals:\n",
    "    print(sea_mammal)\n",
    "    \n",
    "for sea_mammal in animals:\n",
    "    print(\"A \" + sea_mammal + \" needs to breathe oxygen\")\n",
    "    \n",
    "print(\"All of these animals are mammals!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a2951f7",
   "metadata": {},
   "source": [
    "### 4.3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a0fa7cec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n",
      "16\n",
      "17\n",
      "18\n",
      "19\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "numbers = list(range(1,21))\n",
    "for number in numbers:\n",
    "    print(number)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f12b23be",
   "metadata": {},
   "source": [
    "### 4.6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "3ec0a66a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n",
      "5\n",
      "7\n",
      "9\n",
      "11\n",
      "13\n",
      "15\n",
      "17\n",
      "19\n"
     ]
    }
   ],
   "source": [
    "odd_nums = list(range(1,21,2))\n",
    "for num in odd_nums:\n",
    "    print(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd3305f8",
   "metadata": {},
   "source": [
    "### 4.10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "a264344c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the first three items in the list are: \n",
      "1\n",
      "3\n",
      "5\n",
      "three items from the middle of the list are: \n",
      "5\n",
      "7\n",
      "9\n",
      "the last three items in the list are: \n",
      "15\n",
      "17\n",
      "19\n"
     ]
    }
   ],
   "source": [
    "#str = str(odd_nums[:3])\n",
    "\n",
    "\n",
    "print(\"the first three items in the list are: \")\n",
    "for num in odd_nums[:3]:\n",
    "    print((num))\n",
    "    \n",
    "#str = str(odd_nums[2:5])\n",
    "print(\"three items from the middle of the list are: \")\n",
    "for num in odd_nums[2:5]:\n",
    "    print((num))\n",
    "    \n",
    "#str = str(odd_nums[-3:])\n",
    "print(\"the last three items in the list are: \")\n",
    "for num in odd_nums[-3:]:\n",
    "    print((num))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dfe58b91",
   "metadata": {},
   "source": [
    "### 4.11"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "949c7d6e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my fav pizzas are \n",
      "prosciutto\n",
      "pineapple\n",
      "veggie\n",
      "my friend's fav pizzas are\n",
      "prosciutto\n",
      "pineapple\n",
      "veggie\n",
      "olive\n"
     ]
    }
   ],
   "source": [
    "friend_pizzas = pizzas[:]\n",
    "friend_pizzas.append(\"olive\")\n",
    "print(\"my fav pizzas are \")\n",
    "for za in pizzas:\n",
    "    print(za)\n",
    "print(\"my friend's fav pizzas are\")\n",
    "for za in friend_pizzas:\n",
    "    print(za)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "64535666",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0046f88e",
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
