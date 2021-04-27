import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-@#$%^"
total = upper + lower + numbers + symbols
length = 10
if length < 10:
    print ("low strength")
elif length == 10:
    print("medium strength")
else:print("high strength")
password = "".join(random.sample(total, length))
print(password)
