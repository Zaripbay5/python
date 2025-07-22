{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7cde4ee6",
   "metadata": {},
   "outputs": [],
   "source": [
    "ava = {\n",
    "'k1': \"maxxa\",\n",
    "'kk2': 'arbiter',\n",
    "'k3': '3434a',\n",
    "\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "a301e554",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'k4'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[68]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[32m      1\u001b[39m ava.keys()\n\u001b[32m      2\u001b[39m ava[\u001b[33m'\u001b[39m\u001b[33mk1\u001b[39m\u001b[33m'\u001b[39m]\n\u001b[32m----> \u001b[39m\u001b[32m3\u001b[39m \u001b[43mava\u001b[49m\u001b[43m[\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mk4\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m]\u001b[49m\n",
      "\u001b[31mKeyError\u001b[39m: 'k4'"
     ]
    }
   ],
   "source": [
    "ava.keys()\n",
    "ava['k1']\n",
    "ava['k4']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "75a960ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "maxxa\n"
     ]
    }
   ],
   "source": [
    "print(ava['k1'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "29ecfd30",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    " \n",
    "len(ava.keys())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "15b9f3ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['k1', 'kk2', 'k3'])"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ava.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3c19a308",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values(['maxxa', 'arbiter', '3434a'])"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ava.values()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fe2ed830",
   "metadata": {},
   "source": [
    "6 below"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "82114b8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'a': 23, 'b': 34}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{'da': {'a': 23, 'b': 34}, 'ba': {'b': 12, 'd': 90}}"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "da = { 'a':23, 'b':34}\n",
    "ba = {'b':12, 'd':90}\n",
    "print(da)\n",
    "bad = { \"da\": da,\n",
    "       \"ba\": ba,\n",
    "\n",
    "\n",
    "}\n",
    "bad"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "5ea59496",
   "metadata": {},
   "outputs": [],
   "source": [
    "del dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "3dde0b72",
   "metadata": {},
   "outputs": [],
   "source": [
    "#8\n",
    "dicet= {\"year\":23, \"we\":\"wew\", \"name \":\"asti\"}\n",
    "dicet.clear()\n",
    "dictde= dict()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d4cc8cef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ba.pop(\"b\")   #7\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "c9f65e4d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "#9 \n",
    "print(len(dicet)==0)\n",
    "\n",
    "print(len(ava)==0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca769fe8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_items([('k1', 'maxxa'), ('kk2', 'arbiter'), ('k3', '3434a')])"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ava.items() #10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "e58e1ddd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{}\n"
     ]
    }
   ],
   "source": [
    "ava = {\n",
    "'k1': \"maxxa\",\n",
    "'kk2': 'arbiter',\n",
    "'k3': '3434a',\n",
    "\"k1\": \"ekinshi\",\n",
    "():({}),\n",
    "\n",
    "}\n",
    "print(ava[()])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "d04ce00d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{}\n"
     ]
    }
   ],
   "source": [
    "myy_dict={}\n",
    "print(myy_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "5597b244",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "allright, there is\n"
     ]
    }
   ],
   "source": [
    "ava.get('k1')\n",
    "ava[\"k4\"]=4544\n",
    "if 'k1' in ava:\n",
    "    print('allright, there is')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "9411c867",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "key-value: k1 ekinshi\n"
     ]
    }
   ],
   "source": [
    "if \"k1\" in ava:\n",
    "    print(\"key-value:\", 'k1', ava['k1'])\n",
    "else:\n",
    "    print(\"key not exist\")\n",
    "\n",
    "    #10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c014c9f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'k1': 'maxxa', 'kk2': 'maxc', 'k3': '3434a'}"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ava"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "80df5d94",
   "metadata": {},
   "outputs": [],
   "source": [
    "ava.update({\"k1\":45}) #11"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0b95950e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "k1 45\n"
     ]
    }
   ],
   "source": [
    "print(\"k1\",ava['k1'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "583c8225",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unhashable type: 'list'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[6]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m ava.update({\u001b[33m\"\u001b[39m\u001b[33mk4\u001b[39m\u001b[33m\"\u001b[39m:\u001b[33m'\u001b[39m\u001b[33mekinshi\u001b[39m\u001b[33m'\u001b[39m, \u001b[33m'\u001b[39m\u001b[33mk5\u001b[39m\u001b[33m'\u001b[39m:\u001b[33m\"\u001b[39m\u001b[33mkk5\u001b[39m\u001b[33m\"\u001b[39m})\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;28;43mhash\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43m[\u001b[49m\u001b[32;43m34\u001b[39;49m\u001b[43m,\u001b[49m\u001b[32;43m22\u001b[39;49m\u001b[43m,\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mheh\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m)\u001b[49m)\n",
      "\u001b[31mTypeError\u001b[39m: unhashable type: 'list'"
     ]
    }
   ],
   "source": [
    "ava.update({\"k4\":'ekinshi', 'k5':\"kk5\"})\n",
    "print(hash([34,22,'heh']))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fdbb235c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "ava\n",
    "for x in ava.values():\n",
    " if x=='ekinshi':\n",
    "  llist = list(ava.values())\n",
    "  print(llist.count(x))        #12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c798a102",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(ava.keys())\n",
    "list(ava.values()).count('ekinshi')  #12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "3c477b81",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'k1': 'ekinshi',\n",
       " 'kk2': 'arbiter',\n",
       " 'k3': '3434a',\n",
       " (): (),\n",
       " 'k4': 'ekinshi',\n",
       " 'k5': 'kk5'}"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ava"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "3903ef02",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'k1': 'maxxa', 'kk2': 'maxc', 'k3': '3434a', 'k4': 'maxc'}"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ava.update({'kk2':\"maxc\"})\n",
    "ava.keys()=='a'\n",
    "ava.values()=='b'\n",
    "ava.items()==({'b':'a'})\n",
    "ava\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "adbe1f3c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "d190c05e",
   "metadata": {},
   "source": [
    "13 bolamdi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "75c6c72f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# avas = {ava.values():ava.keys()}\n",
    "# avf={()}\n",
    "# for x in ava.values():\n",
    "#     for y in ava.keys():\n",
    "#          x==avf.keys()\n",
    "#          y==avf.values()\n",
    "#          print(avf)\n",
    "new = {():()}\n",
    "for key, value in ava.items():\n",
    " new[value]=key\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "158a2110",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['kk2']\n",
      "['k4']\n"
     ]
    }
   ],
   "source": [
    "#14\n",
    "ava.update({\"k4\":\"maxc\"})\n",
    "for key, value in ava.items():\n",
    "  if value=='maxc': \n",
    "    type(key)==list\n",
    "    print([key])\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b5798227",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1: 1, 67: 3, 'asa': 'as'}"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l1 = [1,67,'asa',34]\n",
    "l2 = [1,3,'as']    #15\n",
    "tl1= tuple(l1)   \n",
    "tl2 = tuple(l2)\n",
    "dll = {tl1:tl2}\n",
    "dlc = dict(zip(l1,l2))\n",
    "dlc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "aa5703c9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'k1': 'maxxa', 'kk2': 'maxc', 'k3': '3434a', 'k4': 'maxc'}"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ava"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0669ce8a",
   "metadata": {},
   "source": [
    "16 qaldi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "4ff1a053",
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
    "#16\n",
    "print(bool(ava['k1'][2]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8db9dd28",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2024\n"
     ]
    }
   ],
   "source": [
    "nestd = {'ati':{'at':'fam', 'jil':2024},\n",
    "         \"ati2\": {'ast':\"usti\"}}\n",
    "nestd\n",
    "print(nestd['ati']['jil'])   #18"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa37139b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'ati': {'at': 'fam', 'jil': 2024},\n",
       " 'ati2': {'ast': 'usti'},\n",
       " 'ism': 'name',\n",
       " 'woye': None,\n",
       " 'erk': 'er',\n",
       " 'yangi': None}"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nestd.setdefault('yangi')  #19\n",
    "nestd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc8919c6",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'dict_values' object has no attribute 'count'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mAttributeError\u001b[39m                            Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[80]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m a1=\u001b[38;5;28mlen\u001b[39m(\u001b[43m(\u001b[49m\u001b[43mava\u001b[49m\u001b[43m.\u001b[49m\u001b[43mvalues\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\u001b[43m.\u001b[49m\u001b[43mcount\u001b[49m(x \u001b[38;5;28;01mfor\u001b[39;00m x \u001b[38;5;129;01min\u001b[39;00m ava.values()))\n\u001b[32m      2\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m a1<\u001b[32m2\u001b[39m:\n\u001b[32m      3\u001b[39m     \u001b[38;5;28mprint\u001b[39m(a1)\n",
      "\u001b[31mAttributeError\u001b[39m: 'dict_values' object has no attribute 'count'"
     ]
    }
   ],
   "source": [
    "a1=len(list(ava.values()).count(x for x in ava.values()))\n",
    "if a1<2:\n",
    "    print(a1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca26781a",
   "metadata": {},
   "source": [
    "19 shala"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89f8093d",
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
       "3"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# len({for s in ava.values()})  #19\n",
    "print(len(set(ava.values())))\n",
    "\n",
    "len({s for s in ava.values()})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "295995c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "list(ava.values()).sort()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab7dfc5a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('df', 4), ('gh', 34), ('s', 1)]"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ghf ={'s':1, \"gh\":34,\"df\":4}\n",
    "ghj = sorted(ghf.items())\n",
    "ghj    #20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "b12fc199",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['df', 'gh', 's']"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ghf ={'s':1, \"gh\":34,\"df\":4}\n",
    "sorted(ghf.keys())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e16e76ed",
   "metadata": {},
   "source": [
    "22 chatgpt qiyin"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d9197b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'gh': 34, 'df': 4}\n"
     ]
    }
   ],
   "source": [
    "filtr = {}\n",
    "for x in ghf: #22\n",
    "    if ghf[x]>2:\n",
    "      filtr[x] = ghf[x]\n",
    "print(filtr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d9a0fcf",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'builtin_function_or_method' object is not subscriptable",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[170]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mfor\u001b[39;00m key \u001b[38;5;129;01min\u001b[39;00m filtr:\n\u001b[32m      2\u001b[39m   \u001b[38;5;28;01mif\u001b[39;00m key \u001b[38;5;129;01min\u001b[39;00m filtr \u001b[38;5;129;01mand\u001b[39;00m filtr[key]==ghf[key]:\n\u001b[32m----> \u001b[39m\u001b[32m3\u001b[39m         \u001b[38;5;28;43mprint\u001b[39;49m\u001b[43m[\u001b[49m\u001b[43mkey\u001b[49m\u001b[43m]\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: 'builtin_function_or_method' object is not subscriptable"
     ]
    }
   ],
   "source": [
    "23"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01e24207",
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
