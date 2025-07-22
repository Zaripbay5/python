"""print('hello')
#comments
 comment also
name = input(" What's your name?").strip().title()
)
print('hello, ', name)  
print('hello,'    , end="")
print(name+name)
print("helo", name, sep="##@")
print("helo", name, end="???")
print("hello, \"name\"" + name)
print(f"halo, {name}")
name =name.strip().title()
name = name.title()
name=name.capitalize()
print("hello,"  +name)  

name = input("What's ur name?").strip().title()
fi, se = name.split()
print(f"Hello, {fi}")
x=1
x= float(input("write x? "))
y =float(input("then y,bro? "))
z=x+y #round by next 2nd digits      
#round(nubmer[,ndigits])
print(f"{z:,}") #put dot every 3 digits(decimal .)
c=x/y
print(f"{c:.2f}")   
print(round(x/y,2))"""
# def hello(to):
# ....print('hello,')

# # hello()
# # name=input("Waht's your name? ")
# # hello(name)
# # # import def
"""def hello(kim="World"):
    print("hello, " , kim)

name = input("names bro?").strip().title()
hello(name)
hello()"""
def main():
    x =int(input("What's x? "))
    print("x square is ", square(x))


def square(n):
    return pow(n,3)
main()