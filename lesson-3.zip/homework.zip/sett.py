{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "23df3435",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{32, 34, 'adfs', 5, 'asdf', 'asd', 23}\n"
     ]
    }
   ],
   "source": [
    "abb = { 23,5,32,\"asd\", \"asdf\"}\n",
    "abba = {23,34,32,\"asd\", \"adfs\"}\n",
    "bbaa = abb.union(abba)\n",
    "print(bbaa)\n",
    "# bbaa=abb\n",
    "# print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "21530599",
   "metadata": {},
   "outputs": [],
   "source": [
    "bbab=abb.intersection(abba)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5728c000",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{32, 'asd', 23}\n"
     ]
    }
   ],
   "source": [
    "print(bbab)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cb7fdd8c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{5, 'asdf'}\n",
      "{5, 'asdf'}\n"
     ]
    }
   ],
   "source": [
    "bbaas=abb.difference(abba )  \n",
    "print(bbaas) \n",
    "bbah =  abb - abba\n",
    "print(bbah)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "b1679416",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "cbab ={32,'asd'}\n",
    "print( cbab.issubset(bbab))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "3e27e6fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(\"asd\" in bbab)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ace108c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{23, 32, 'asd', 'dfsa'}"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(len(bbab)) #6\n",
    "bbab.add(\"dfsa\")\n",
    "bbab"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1794ba77",
   "metadata": {},
   "source": [
    "#7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e5aef2e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{34, 45, 56, 'as', 'mad'}"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "llis = [45,56,34,45,'as','as','mad']\n",
    "lliset = set(llis)\n",
    "lliset\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "64272875",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{23, 'dfsa'}"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# bbab.remove(32) #8\n",
    "# print(bbab)\n",
    "# print(bbab)\n",
    "bbab.discard('asd')\n",
    "bbab\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3af38310",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "set()\n"
     ]
    }
   ],
   "source": [
    "bbab.clear()\n",
    "print(bbab)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "1fc7ef7a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "emptyku\n",
      "no\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "if len(bbab)==0:\n",
    "    print(\n",
    "        'emptyku'\n",
    "    )\n",
    "else:\n",
    "    print(\n",
    "        'no'\n",
    "    )\n",
    "if bbab:\n",
    "  print('emt')\n",
    "else:\n",
    "   print('no')\n",
    "   \n",
    "print(bbab==())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "37d82d93",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{2, 23, 5, 'sf'}"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "was = { 'as', 34,34,5}\n",
    "ad = {'as', 'sf',23,34,2}\n",
    "wad = ad.symmetric_difference(was)\n",
    "wad\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "a9c5bea3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{34, 5, 'asfg', 'as', 'qos'}\n"
     ]
    }
   ],
   "source": [
    "if 'asfg' in was:\n",
    "    print('existg/''o')\n",
    "else:\n",
    "    was.add('asfg')\n",
    "    print(was)\n",
    "\n",
    "    \n",
    "\n",
    "was.add('qos')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "1401523d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'as', 'asfg', 'qos'}"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "was.pop()\n",
    "was"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "aa174661",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "23"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num = {23,2,5,23}\n",
    "nums = {12,23,12,6\n",
    "        }\n",
    "max(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "55c3767b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num = {23,2,5,23}\n",
    "nums = {12,23,12,6\n",
    "        }\n",
    "max(num)\n",
    "min(nums)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "f9507ab0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "no\n",
      "no\n"
     ]
    }
   ],
   "source": [
    "for x in num:\n",
    "  if x%2==0:\n",
    "    print(x)\n",
    "  else:\n",
    "    (print('no'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "c49dd928",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "23\n"
     ]
    }
   ],
   "source": [
    "for x in num:\n",
    "  if x%2==1:\n",
    "     print(x)\n",
    "#   else:\n",
    "#     (print('no'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "47f3ad0b",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'set' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[67]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mdel\u001b[39;00m \u001b[38;5;28;43mset\u001b[39;49m\n",
      "\u001b[31mNameError\u001b[39m: name 'set' is not defined"
     ]
    }
   ],
   "source": [
    "del set\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "bf7ed024",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "sret = tuple(range(1,12))\n",
    "sre = set(sret)\n",
    "sre"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "99e52b25",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{6, 8, 9, 45}"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "aas = [1,24,45,6]\n",
    "assd = [ 24,1,9,8]\n",
    "saas = set(aas) \n",
    "sassd= set (assd)\n",
    "sfet = sassd.symmetric_difference(saas)\n",
    "sfet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4539e52d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "print(len(saas.intersection(sassd))==0)\n",
    "print(saas.isdisjoint(sassd))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "9f1f21b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[45, 6]\n",
      "[24, 1, 9, 8]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[24, 1, 9, 8]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(aas)\n",
    "print(assd)\n",
    "assd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "00a18ce4",
   "metadata": {},
   "outputs": [],
   "source": [
    "saas = set(aas) \n",
    "sassd= set (assd)\n",
    "das= saas.intersection(sassd)\n",
    "for x in das:\n",
    "    if x in saas:\n",
    "        saas.remove(x)\n",
    "        aas = list(saas)\n",
    "        print(saas)\n",
    "    else:\n",
    "        print('error')\n",
    "    if x in sassd:\n",
    "        sassd.remove(x)\n",
    "        assd = list(sassd)\n",
    "        print(sassd)\n",
    "    else:\n",
    "        print('error')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "29a2ac08",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[45, 6]\n",
      "[24, 1, 9, 8]\n"
     ]
    }
   ],
   "source": [
    "saas = set(aas) \n",
    "sassd= set (assd)\n",
    "das= saas.intersection(sassd)\n",
    "for x in das:\n",
    "    if x in saas:\n",
    "        saas.remove(x)\n",
    "        aas = list(saas)\n",
    "        print(saas)\n",
    "    else:\n",
    "        print('error')\n",
    "print(aas)\n",
    "print(assd)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "0b20a46a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "gha= [2,2,4,5,3,3]  #21\n",
    "sgha = set(gha)\n",
    "gha = list(sgha)\n",
    "print(gha)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "9326d0a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "print(gha.append(4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "7a50058d",
   "metadata": {},
   "outputs": [],
   "source": [
    "ghas = set(gha)\n",
    "for g in ghas:   #22\n",
    " for y in gha:\n",
    "    if g ==y:\n",
    "        gha.remove(y)\n",
    "        print(len(gha))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "0877bbce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "my_list = [1, 2, 2, 3, 4, 4, 5]\n",
    "#22\n",
    "# Convert to set to remove duplicates\n",
    "unique_elements = set(my_list)\n",
    "\n",
    "# Count unique elements\n",
    "count = len(unique_elements)\n",
    "\n",
    "print(count)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "53dafe2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{7, 8, 9}"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import random\n",
    "det = set(random.sample(range(1,12),3))\n",
    "det"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3bf80ee",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.12.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
