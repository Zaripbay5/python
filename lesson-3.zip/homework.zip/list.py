{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "6ed97292",
   "metadata": {},
   "outputs": [],
   "source": [
    "ab=['abbas']\n",
    "type(ab)\n",
    "ba = ['as','34','false']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "39a02d4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "print(len(ab))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "7f082669",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['as', '34', 'false', 'massa']"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ba.append('massa')\n",
    "ba"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "9f3ee85b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ba.count('massa')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1479663f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[23, 23, 12, 7]\n",
      "65\n"
     ]
    }
   ],
   "source": [
    "num = [23, 23, 12,7]\n",
    "print(num)\n",
    "print(sum(num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "7d5e27d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    }
   ],
   "source": [
    "print(max(num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "305c2e0a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "min(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "592016a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[7, 23]\n"
     ]
    }
   ],
   "source": [
    "print(num[-1::-3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "bfd39e66",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "yes sir\n"
     ]
    }
   ],
   "source": [
    "if 23 in num :\n",
    "    print(\"yes sir\")\n",
    "else:\n",
    "    print(\"no\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3359ded4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "45"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num2 = [45,65,32,2 ]\n",
    "num2[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "24c078fb",
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
    "print(num2[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "f7c6c8d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "num.extend(num2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "bbdee7f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[23, 23, 12]\n"
     ]
    }
   ],
   "source": [
    "print(num[0:3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "ede5364e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 32, 65, 45, 7, 12, 23, 23]"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num.reverse() \n",
    "num\n",
    "#print(num.reverse())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "a76c2591",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 7, 12, 23, 23, 32, 45, 65]"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num.sort()\n",
    "num"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "44842938",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 7, 12, 45, 65, 7]"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num.pop(3)\n",
    "num\n",
    "num.append(7)\n",
    "num\n",
    "del num[3:5]\n",
    "num #11"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "678bf78c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 7, 12, 'maccf', 45, 65, 7]"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num.insert(3,\"maccf\")\n",
    "num"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "91a928b5",
   "metadata": {},
   "source": [
    "#13 task\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "156b65ba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "maccf\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[2, 7, 12, 'maccf', 45, 65, 7]"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(num[3])\n",
    "num"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "e4ddfe55",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "23 is not in list",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mValueError\u001b[39m                                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[62]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m num.index(\u001b[32m7\u001b[39m)\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m \u001b[43mnum\u001b[49m\u001b[43m.\u001b[49m\u001b[43mindex\u001b[49m\u001b[43m(\u001b[49m\u001b[32;43m23\u001b[39;49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mValueError\u001b[39m: 23 is not in list"
     ]
    }
   ],
   "source": [
    "num.index(7)\n",
    "num.index(23)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "99dfe272",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "no\n"
     ]
    }
   ],
   "source": [
    "if num is bool:\n",
    "    print(\" yes\"),\n",
    "else :\n",
    "     print(\"no\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f3f3183",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(len(num)==0)\n",
    "bool(len(num)==0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "edb65bcc",
   "metadata": {},
   "outputs": [],
   "source": [
    "#15\n",
    "num.append(11)\n",
    "\n",
    "num.append(18)\n",
    "num.pop(-1)\n",
    "del num[-5:-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4627da3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "num.append(14)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3fc0c2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "even: 12\n",
      "even: 14\n"
     ]
    }
   ],
   "source": [
    "\n",
    "for nums in num:\n",
    "    if nums%2==0:\n",
    "        print(\"even:\", nums)\n",
    "        # count +=1\n",
    "#         # print(len(if nums%2==0))\n",
    "# print(\"total:\",count)\n",
    "# countev = len([])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3662d038",
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
    "count = len([n \n",
    "             for n in num \n",
    "             if n%2==0])\n",
    "print(count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ec35fe5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "sana = len ([n \n",
    "             for n in num \n",
    "             if n%2==1])\n",
    "print(sana)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d8f6022d",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'num' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[3]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m num3 = [ \u001b[32m4\u001b[39m, \u001b[32m56\u001b[39m,\u001b[32m4\u001b[39m, \u001b[32m23\u001b[39m, \u001b[32m7\u001b[39m,\u001b[32m9\u001b[39m]\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m \u001b[43mnum\u001b[49m\n\u001b[32m      3\u001b[39m num.extend(num3)\n\u001b[32m      4\u001b[39m \u001b[38;5;28mprint\u001b[39m(num)\n",
      "\u001b[31mNameError\u001b[39m: name 'num' is not defined"
     ]
    }
   ],
   "source": [
    "num3 = [ 4, 56,4, 23, 7,9]\n",
    "num\n",
    "num.extend(num3)\n",
    "print(num)\n",
    "\n",
    "for h in num3 :\n",
    "    num.append(h)\n",
    "print(num)\n",
    "\n",
    "nnum = num + num3\n",
    "print(nnum)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "13e3af88",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[23, 23, 12, 7, 4, 56, 4]"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "del  nnum[7:]\n",
    "# nnum\n",
    "num\n",
    "# num3\n",
    "del num[7:]\n",
    "num"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1901602",
   "metadata": {},
   "source": [
    "#18 we wil make better"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "a4588c43",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "not in list\n",
      "not in list\n",
      "not in list\n",
      "not in list\n",
      "yes\n",
      "not in list\n"
     ]
    }
   ],
   "source": [
    "# num.extend(num3)\n",
    "# num 18\n",
    "for g in num3:\n",
    "  if g in num:\n",
    "    print(\"yes\")\n",
    "  else:\n",
    "    print(\"not in list\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "36a82529",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[23, 23, 12, 7, 4, 56, 4, 4, 56, 4, 23, 7, 9, 4, 56, 4, 23, 7, 9, 4, 56, 4, 23, 7, 9]\n",
      "[4, 56, 4, 23, 7, 9]\n"
     ]
    }
   ],
   "source": [
    "print(num)\n",
    "print(num3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "646eb868",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1276821002.py, line 1)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[78]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mnum.insert(0:inchi)\u001b[39m\n                ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "num.insert(0:inchi)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b8513f2d",
   "metadata": {},
   "source": [
    "19 make better"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d14ae2e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['replaceenew', 'soz', 'lar', 'kabii']"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "yangi = numbers=34\n",
    "num[0] = yangi\n",
    "num\n",
    "soz = [ \"soz\", 'lar', 'kabii']\n",
    "type(soz)\n",
    "soz.insert(0,\" replacee\")\n",
    "soz[0] = \"replaceenew\"\n",
    "soz"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03e4469e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[56, 23, 9, 7, 4, 4]\n",
      "23\n"
     ]
    }
   ],
   "source": [
    "num3.sort(reverse= True)  #20task\n",
    "print( num3)\n",
    "print(num3[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "a59bf9ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "print(num3[-2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "bea5c886",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[12]\n",
      "[14]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "for e in num:\n",
    "    if e%2==0 :\n",
    "         list = [e] \n",
    "         print(list)\n",
    "        \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "e4568e12",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[23, 23, 7]\n",
      "[12, 14]\n"
     ]
    }
   ],
   "source": [
    "count = [t for t in num if t%2==1  ]\n",
    "print( count  )\n",
    "\n",
    "count = [t for t in num if t%2==0  ]\n",
    "print( count  )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "58434471",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[23, 23, 12, 7, 14]"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(num)\n",
    "num"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "14b4476e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[23, 23, 12, 7]\n"
     ]
    }
   ],
   "source": [
    "#25\n",
    "co = num.copy()\n",
    "print(co)\n",
    "vo = list(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6c10663",
   "metadata": {},
   "source": [
    "26"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "6cf99c5a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[23, 12]\n"
     ]
    }
   ],
   "source": [
    "d= len(num)//2\n",
    "if len(num)%2==0:\n",
    "    mid = num[d-1:d+1]\n",
    "else :\n",
    "    mid =num[d]\n",
    "\n",
    "print(mid)\n",
    "\n",
    " \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "d7fc0f2c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "34"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nu = num[2:5]\n",
    "asg = max(nu)\n",
    "asg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "79cf7b22",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nu = num[1:5]\n",
    "asg = min(nu)\n",
    "asg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "b0639d79",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[12, 156, 156]"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "del num[-2]\n",
    "num.append(156)\n",
    "\n",
    "\n",
    "num.sort()\n",
    "num"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "9f76f9a7",
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
    "# num.sort()\n",
    "# print(bool(num.sort()))\n",
    "# print(num)\n",
    "\n",
    "print(num == sorted(num))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8ccb1a1b",
   "metadata": {},
   "source": [
    "31\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "60704d11",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[12, 156, 156, 12, 156, 156, 12, 156, 156]\n"
     ]
    }
   ],
   "source": [
    "num9= num*3\n",
    "\n",
    "print(num9)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "9bc85ed1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[12, 12, 12, 12, 12, 156, 156, 156, 156, 156, 156, 156, 156, 156, 156]\n"
     ]
    }
   ],
   "source": [
    "num5 = num9 +num\n",
    "num5.sort(\n",
    ")\n",
    "print(num5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "525b7595",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[156, 156, 12, 9, 90, 90, 90]"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num.append(90)\n",
    "num"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "38df974e",
   "metadata": {},
   "source": [
    "##33 make better"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "7887d8d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "1\n",
      "0\n",
      "1\n",
      "1\n",
      "0\n",
      "1\n",
      "1\n",
      "0\n",
      "1\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "for x in num9:\n",
    "    \n",
    "    a = num9.index(x)\n",
    "    print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ec063b75",
   "metadata": {},
   "source": [
    "34"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "83fae77c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[156, 156, 12, 9, 90, 90, 90]\n"
     ]
    }
   ],
   "source": [
    "for h in num:\n",
    "   h=num[-1]==num[0]\n",
    "print(num) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "0e324b4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n"
     ]
    }
   ],
   "source": [
    "numbers = list(range(1, 11))\n",
    "print(numbers)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "6dae33bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "nu33 = list(range(-2,4))\n",
    "add=0\n",
    "for t in nu33:\n",
    "    if t>0:\n",
    "      add +=t\n",
    "\n",
    "print(add)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e7404ea0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-3\n"
     ]
    }
   ],
   "source": [
    "nu33 = list(range(-2,4))\n",
    "add=0\n",
    "for t in nu33:\n",
    "    if t<0:\n",
    "      add +=t\n",
    "\n",
    "print(add)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "9e80cd4d",
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
    "nu34=[4,3,2,1,1,2,3,4]\n",
    "# print(nu34==nu34.reverse()) \n",
    "temp =nu34.copy()\n",
    "temp.reverse()\n",
    "print( temp==nu34)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0de21fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "no\n",
      "no\n",
      "no\n",
      "no\n",
      "no\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# for f in nu34:\n",
    "#     if f==nu34[0]==nu34[-1]:\n",
    "#         print(bool(f))\n",
    "#     else:\n",
    "#         print(\"no\")\n",
    "# nu34."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dc5b112f",
   "metadata": {},
   "source": [
    "39 better "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "55878217",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4, 5, [3, 2], 3, 8, 9, 5]"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ase =[4 ,5,[3,2]] #39\n",
    "bas = ase + [3,8,9]\n",
    "bas.append(5)\n",
    "bas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b137cb53",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax. Maybe you meant '==' or ':=' instead of '='? (996701294.py, line 2)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[52]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mif h=bas[0:6]==bas[0:7] bas.remove(h):\u001b[39m\n       ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid syntax. Maybe you meant '==' or ':=' instead of '='?\n"
     ]
    }
   ],
   "source": [
    "# for h in bas:\n",
    "#     if h=bas[0:7]==bas[0:7] bas.remove(h):\n",
    "# else:\n",
    "#      print(h)\n",
    "     "
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



#tupple #TUPPLE
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
