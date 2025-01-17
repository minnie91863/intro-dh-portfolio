{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "cb79514c",
   "metadata": {},
   "source": [
    "### 6.1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2ad6576e",
   "metadata": {},
   "outputs": [],
   "source": [
    "person = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fcb73df5",
   "metadata": {},
   "outputs": [],
   "source": [
    "person['first_name'] = 'Minnie'\n",
    "person['last_name'] = 'Xie'\n",
    "person['age'] = '21'\n",
    "person['city'] = 'Medford'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "e649497a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'first_name': 'Minnie', 'last_name': 'Xie', 'age': '21', 'city': 'Medford'}\n"
     ]
    }
   ],
   "source": [
    "print(person)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ed5a4a42",
   "metadata": {},
   "source": [
    "### 6.2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "13fff5c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'minnie': 1, 'emma': 2, 'casey': 3, 'julien': 4, 'colby': 5}\n"
     ]
    }
   ],
   "source": [
    "fav_nums = {}\n",
    "fav_nums['minnie'] = 1\n",
    "fav_nums['emma'] = 2\n",
    "fav_nums['casey'] = 3\n",
    "fav_nums['julien'] = 4\n",
    "fav_nums['colby'] = 5\n",
    "print(fav_nums)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3e04d5a1",
   "metadata": {},
   "source": [
    "### 6.3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "3427efc3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "int: integer value\n",
      "string: list of chars\n",
      "elif: else if\n",
      "python: coding language\n",
      "dictionary: like a list with keys\n"
     ]
    }
   ],
   "source": [
    "vocab = {\n",
    "    'int': 'integer value',\n",
    "    'string': 'list of chars',\n",
    "    'elif': 'else if',\n",
    "    'python': 'coding language',\n",
    "    'dictionary': 'like a list with keys'\n",
    "}\n",
    "print(\"int: \" + vocab['int'])\n",
    "print(\"string: \" + vocab['string'])\n",
    "print(\"elif: \" + vocab['elif'])\n",
    "print(\"python: \" + vocab['python'])\n",
    "print(\"dictionary: \" + vocab['dictionary'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "726946e2",
   "metadata": {},
   "source": [
    "### 6.4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "63ba0be8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "int: integer value\n",
      "string: list of chars\n",
      "elif: else if\n",
      "python: coding language\n",
      "dictionary: like a list with keys\n",
      "loop: helps with iterating\n",
      "variable: stores information\n",
      "list: stores a group of variables\n",
      "boolean: true or false type\n",
      "print: show output\n"
     ]
    }
   ],
   "source": [
    "for key,value in vocab.items():\n",
    "    print(key + \": \" + value)\n",
    "vocab['loop'] = 'helps with iterating'\n",
    "vocab['variable'] = 'stores information'\n",
    "vocab['list'] = 'stores a group of variables'\n",
    "vocab['boolean'] = 'true or false type'\n",
    "vocab['print'] = 'show output'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ba45a1e",
   "metadata": {},
   "source": [
    "### 6.5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "d79e7e8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Nile runs through Egypt\n",
      "The Mississippi runs through United States\n",
      "The Thames runs through England\n",
      "nile\n",
      "mississippi\n",
      "thames\n",
      "egypt\n",
      "united states\n",
      "england\n"
     ]
    }
   ],
   "source": [
    "rivers = {\n",
    "    'nile': 'egypt',\n",
    "    'mississippi': 'united states',\n",
    "    'thames': 'england'\n",
    "}\n",
    "for name,country in rivers.items():\n",
    "    print(\"The \" + name.title() + \" runs through \" + country.title())\n",
    "    \n",
    "for name in rivers.keys():\n",
    "    print(name)\n",
    "    \n",
    "for name in rivers.keys():\n",
    "    print(rivers[name])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f32601cc",
   "metadata": {},
   "source": [
    "### 6.7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "91f53707",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{}\n",
      "{}\n",
      "{'first_name': 'Minnie', 'last_name': 'Xie', 'age': '21', 'city': 'Medford'}\n"
     ]
    }
   ],
   "source": [
    "me = {}\n",
    "you = {}\n",
    "people = [me, you, person]\n",
    "for curr_person in people:\n",
    "    print(curr_person)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8169c1f1",
   "metadata": {},
   "source": [
    "### 6.8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "028b9a8a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'type': 'dog', 'owner': 'sam'}\n",
      "{'type': 'cat', 'owner': 'sam'}\n"
     ]
    }
   ],
   "source": [
    "lucky = {\n",
    "    'type': 'dog',\n",
    "    'owner': 'sam'\n",
    "}\n",
    "\n",
    "mittens = {\n",
    "    'type': 'cat',\n",
    "    'owner': 'sam'\n",
    "}\n",
    "\n",
    "pets = [lucky, mittens]\n",
    "\n",
    "for pet in pets:\n",
    "    print(pet)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4340559a",
   "metadata": {},
   "source": [
    "### 6.9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "8561e73d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('minnie', ['here', 'there'])\n",
      "('julien', ['over here', 'over there'])\n",
      "('emma', ['over the hill', 'across the river', 'through the woods'])\n"
     ]
    }
   ],
   "source": [
    "favorite_places = {}\n",
    "\n",
    "minnie_places = ['here', 'there']\n",
    "julien_places = ['over here', 'over there']\n",
    "emma_places = ['over the hill', 'across the river', 'through the woods']\n",
    "\n",
    "favorite_places = {\n",
    "    'minnie': minnie_places,\n",
    "    'julien': julien_places,\n",
    "    'emma': emma_places,\n",
    "}\n",
    "\n",
    "for person in favorite_places.items():\n",
    "    print(person)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "573aa7f6",
   "metadata": {},
   "source": [
    "### 6.11"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "739b197b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('Medford', {'country': 'united states', 'population': 'over 100', 'fact': 'where Tufts is located'})\n",
      "('Phoenix', {'country': 'united states', 'population': 'over 100', 'fact': 'where my hometown is located'})\n",
      "('Madrid', {'country': 'spain', 'population': 'over 100', 'fact': 'the capital of Spain'})\n"
     ]
    }
   ],
   "source": [
    "medford = {\n",
    "    'country': 'united states',\n",
    "    'population': 'over 100',\n",
    "    'fact': 'where Tufts is located'\n",
    "}\n",
    "phoenix = {\n",
    "    'country': 'united states',\n",
    "    'population': 'over 100',\n",
    "    'fact': 'where my hometown is located'\n",
    "}\n",
    "madrid = {\n",
    "    'country': 'spain',\n",
    "    'population': 'over 100',\n",
    "    'fact': 'the capital of Spain'\n",
    "}\n",
    "cities = {\n",
    "    'Medford': medford,\n",
    "    'Phoenix': phoenix,\n",
    "    'Madrid': madrid\n",
    "}\n",
    "\n",
    "for city in cities.items():\n",
    "    print(city)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3952dcf1",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
