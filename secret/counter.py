sp = [
    "Ананас", 15,
    "Шоколадка", 1000,
    "Цибуля", 1
]
s = 0
for i in range(0, len(sp), 2):
    s+=sp[i+1]
print("Корзині є ", end="")
for i in range(0, len(sp), 2):
    if i != len(sp)-2:
        print((sp[i]+", ").lower(), end="")
    else:   
        print(sp[i].lower())
print("Все це добро коштує ", s, "грн")
