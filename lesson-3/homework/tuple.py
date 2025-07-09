{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
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
   "execution_count": 9,
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
   "execution_count": 65,
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
   "execution_count": 23,
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
   "execution_count": 42,
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
   "execution_count": null,
   "id": "a25c339e",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'>' not supported between instances of 'int' and 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[61]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;66;03m# print(max(tup))\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m larg = \u001b[38;5;28;43mmax\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mtup\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m      3\u001b[39m \u001b[38;5;28mprint\u001b[39m(larg)\n",
      "\u001b[31mTypeError\u001b[39m: '>' not supported between instances of 'int' and 'str'"
     ]
    }
   ],
   "source": [
    "# print(max(tup))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "a364c90e",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'>' not supported between instances of 'int' and 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[56]\u001b[39m\u001b[32m, line 4\u001b[39m\n\u001b[32m      2\u001b[39m \u001b[38;5;28mlist\u001b[39m.sort()\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mfor\u001b[39;00m l \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mlist\u001b[39m:\n\u001b[32m----> \u001b[39m\u001b[32m4\u001b[39m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;28;43mmax\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43ml\u001b[49m\u001b[43m)\u001b[49m)\n",
      "\u001b[31mTypeError\u001b[39m: '>' not supported between instances of 'int' and 'str'"
     ]
    }
   ],
   "source": [
    "list = [tup]\n",
    "list.sort()\n",
    "for l in list:\n",
    "    print(max(l))"
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
