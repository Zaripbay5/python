{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "1f75ebd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('as', 'add', 'af', 45, 23, 6784)\n"
     ]
    }
   ],
   "source": [
    "tup = ('as','add', 'af', 45, 23, 6784)\n",
    "print(tup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "86bc765f",
   "metadata": {},
   "outputs": [],
   "source": [
    "yut = ('tupa',)\n",
    "type(yut)\n",
    "y = ('af','af')\n",
    "tup +=y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d52893a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup.count(\"af\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4c975ffd",
   "metadata": {},
   "source": [
    "2 3  tawispadin'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "87557be0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "67\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "# # max(tup)\n",
    "# # len(tup)\n",
    "# for h in tup:\n",
    "#   if h==int:\n",
    "#     print(max(h))\n",
    "# else:\n",
    "#   print(min(h))\n",
    "num =(4, 34, 2, 67,7)\n",
    "print(max(num))\n",
    "print(min(num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3eacac38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "existt\n"
     ]
    }
   ],
   "source": [
    "if \"af\" in tup:  #4\n",
    "    print(\n",
    "    \"existt\"\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "aa467158",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "as\n"
     ]
    }
   ],
   "source": [
    "if len(tup)==0:\n",
    "    print('emptty')\n",
    "else:\n",
    "    print(tup[0]) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "317252ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6784\n"
     ]
    }
   ],
   "source": [
    "if len(tup)==0:\n",
    "    print('emptty')  #6\n",
    "else:\n",
    "    print(tup[-1]) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d9f475fc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(tup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "213b3f3e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('as', 'add', 'af')"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "yup = tup[0:3]\n",
    "yup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5a31b36f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('as', 'add', 'af')\n"
     ]
    }
   ],
   "source": [
    "\n",
    "s = slice(3) \n",
    "print(tup[s])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08cb3aa8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('as', 'add', 'af', 45, 23, 6784, 'as', 'add', 'af')"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cup = tup + yup #9\n",
    "cup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "25066318",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "noteem\n"
     ]
    }
   ],
   "source": [
    "yup =()\n",
    "if yup: #== ():\n",
    "    print('empty')\n",
    "else :\n",
    "    print('noteem')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "46335281",
   "metadata": {},
   "source": [
    "11  check, this then, below"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e88e9b8",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "f8baaa6c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup.index('af')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a25c339e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "34\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "#12 #13\n",
    "llist = list(num)\n",
    "llist.sort()\n",
    "print(llist[-2])\n",
    "print(llist[1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "a364c90e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 4, 7, 34, 67]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# list = [tup]\n",
    "# list.sort()\n",
    "# for l in list:\n",
    "#     print(max(l))\n",
    "llist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ee53b36b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "tuple"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#14\n",
    "mytup = (y,)\n",
    "type(mytup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3c595fae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[45, 3, 'we']"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lisst = [45,3, \"we\"]\n",
    "tyup = (lisst)  #+ [34]\n",
    "tyup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "97e3bc50",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "idkk\n"
     ]
    }
   ],
   "source": [
    "tupli = list(num)\n",
    "#print( tupli ==sorted(tupli))\n",
    "# tupli\n",
    "if tupli== sorted(tupli):\n",
    "  print('yes')\n",
    "else:\n",
    "   print('idkk')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "397f6e5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "67\n"
     ]
    }
   ],
   "source": [
    "tupli[1:4]\n",
    "print(max(tupli[1:4]))  #17"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "d5cf44e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "tupli[-1:-4]\n",
    "print(min(tupli[-4:-1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "07962816",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 34, 2, 67, 7]\n",
      "(4, 34, 2, 67, 7)\n",
      "('as', 'add', 'af', 45, 23, 6784, 'af', 'af')\n"
     ]
    }
   ],
   "source": [
    "#19\n",
    "print(tupli)\n",
    "print(num)\n",
    "print(tup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "937a337d",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'tupli' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[43]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mdel\u001b[39;00m  \u001b[43mtupli\u001b[49m\n\u001b[32m      2\u001b[39m tupli\n",
      "\u001b[31mNameError\u001b[39m: name 'tupli' is not defined"
     ]
    }
   ],
   "source": [
    "del  tupli\n",
    "tupli"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "af777db1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(45, 23, 6784, 'af', 'af')"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tup\n",
    "u = list(tup)\n",
    "u.pop(0)\n",
    "tup = tuple(u)\n",
    "tup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "e75ade56",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[45, 23, 6784, 'af', 'af', (['af'], [45]), (['af'], [45]), (['af'], [45]), (['af'], [45]), (['af'], [45])]\n"
     ]
    }
   ],
   "source": [
    "#20\n",
    "u.append((['af'],[45]))\n",
    "tup = tuple(u)\n",
    "u.pop(-1)\n",
    "print(u)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ccbcc7b1",
   "metadata": {},
   "source": [
    "#20 islenbedi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "198eb168",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('a', 'p', 'p', 'l', 'e')\n",
      "('b', 'a', 'n', 'a', 'n', 'a')\n",
      "('c', 'h', 'e', 'r', 'r', 'y')\n"
     ]
    }
   ],
   "source": [
    "# thistuple = (\"apple\", \"banana\", \"cherry\")\n",
    "# for i in range(len(thistuple)):\n",
    "#   print(thistuple[i])\n",
    "\n",
    "\n",
    "thistuple = (\"apple\", \"banana\", \"cherry\")\n",
    "for x in thistuple:\n",
    "  x == tuple(x)\n",
    "  print(tuple(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "2c61e1e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "appleappleapple\n",
      "bananabananabanana\n",
      "cherrycherrycherry\n"
     ]
    }
   ],
   "source": [
    "\n",
    "n=3\n",
    "thistuple = (\"apple\", \"banana\", \"cherry\")\n",
    "for x in thistuple:\n",
    "  print(x*n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a5257eb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "fab802ef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#22\n",
    "tu = tuple(range(1,11,1))\n",
    "tu"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "fbd32ef8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)\n"
     ]
    }
   ],
   "source": [
    "#23\n",
    "yu = list(tu)\n",
    "yu.reverse()\n",
    "tu = tuple(yu)\n",
    "print(tu)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "82450327",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "palindrome\n"
     ]
    }
   ],
   "source": [
    "#24\n",
    "su = ('a', 2, 5, 2, 'a')\n",
    "yu = list(su)\n",
    "if yu== yu[::-1]:\n",
    "# if yu== yu.reverse():\n",
    "    print('palindrome')\n",
    "else:\n",
    "    print('noo')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "59e288d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{2, 3, 5, 21}"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nums =[3,2,2,2,21,5]\n",
    "sup = set(nums)\n",
    "sup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "0ffd3730",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4, 34, 2, 67, 7)"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num"
   ]
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
