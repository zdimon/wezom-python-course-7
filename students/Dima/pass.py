import random
x=""
password="29121998"
while x!=password:
    x=""
    while len(x)!=len(password):
        y=random.randrange(10)
        x=str(x)+str(y)
    print(x)
print("Password:",x)