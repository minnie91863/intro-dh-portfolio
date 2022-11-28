{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ea9d98ac",
   "metadata": {},
   "source": [
    "### 8-1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5b330979",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi everyone! I'm currently learning about functions in Python :)\n"
     ]
    }
   ],
   "source": [
    "def display_message():\n",
    "    print(\"Hi everyone! I'm currently learning about functions in Python :)\")\n",
    "    \n",
    "display_message();"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a6dc0cea",
   "metadata": {},
   "source": [
    "### 8-2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "381cd641",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A book I enjoyed in middle school was The Hunger Games\n"
     ]
    }
   ],
   "source": [
    "title = \"The Hunger Games\"\n",
    "def favorite_book(title):\n",
    "    print(\"A book I enjoyed in middle school was \" + title)\n",
    "\n",
    "favorite_book(title);"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "08fdd145",
   "metadata": {},
   "source": [
    "### 8-3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ca365344",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The shirt will be in size medium and the message will be Hello World!\n",
      "The shirt will be in size medium and the message will be Hello World!\n"
     ]
    }
   ],
   "source": [
    "def make_shirt(size, message):\n",
    "    print(\"The shirt will be in size \" + size + \" and the message will be \" + message)\n",
    "\n",
    "make_shirt(\"medium\", 'Hello World!')\n",
    "make_shirt(message = 'Hello World!', size = 'medium')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "40d23697",
   "metadata": {},
   "source": [
    "### 8-5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "8eca67c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The city of Toronto is in Canada\n",
      "The city of Calgary is in Canada\n",
      "The city of Medford is in United States\n"
     ]
    }
   ],
   "source": [
    "country = 'Canada'\n",
    "def describe_city(city, country):\n",
    "    print( \"The city of \" + city.title() + \" is in \" + country.title())\n",
    "\n",
    "describe_city('toronto', country)\n",
    "describe_city('calgary', country)\n",
    "describe_city('medford', 'united states')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "60dc3c82",
   "metadata": {},
   "source": [
    "### 8-6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0fda5f89",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Santiago, Chile\n",
      "Havana, Cuba\n",
      "Sao Paulo, Brazil\n"
     ]
    }
   ],
   "source": [
    "def city_country(city, country):\n",
    "    return (str(city.title() + ', ' + country.title()))\n",
    "\n",
    "print(city_country('santiago', 'chile'))\n",
    "print(city_country('havana', 'cuba'))\n",
    "print(city_country('sao paulo', 'brazil'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8528be2a",
   "metadata": {},
   "source": [
    "### 8-7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e8017288",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'The 1975', 'album': 'Being Funny In A Foriegn Language'}\n",
      "{'name': 'Taylor Swift', 'album': 'Red'}\n",
      "{'name': 'Beabadoobee', 'album': 'Beatopia', 'num_tracks': '14'}\n"
     ]
    }
   ],
   "source": [
    "def make_album(artist, album, num_tracks=''):\n",
    "    artist_album = {'name': artist.title(), 'album': album.title()}\n",
    "    if num_tracks:\n",
    "               artist_album['num_tracks'] = num_tracks\n",
    "    return artist_album\n",
    "\n",
    "print(make_album('the 1975', 'being funny in a foriegn language'))\n",
    "print(make_album('taylor swift', 'red'))\n",
    "print(make_album('beabadoobee', 'beatopia', '14'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "75c30b1d",
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
