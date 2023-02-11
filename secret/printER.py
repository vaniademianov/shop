# by remoteaccess01
# або я косий або пірамідка без шансів
try:
    px = int(input("Скільки поверхів в пірамідці повинно бути? "))+1
except ValueError:
    raise ValueError("Невірне число!")
a = 1
try:
    symbol = str(input("Введіть символ: "))[0]

except:
    raise ValueError("Невірний символ!")
for i in range(px):
    print(" "*(10 - i), symbol*a)
    a+=2
