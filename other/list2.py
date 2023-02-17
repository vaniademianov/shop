products = [
    "Вітчим вітчимів, звичайний", 2000,
    "Кампудахтер Поліни", 4000,
    "Піца з Маркетопту", 300,
    "Манікен путіна", 200,
    "Яйце куряче", 20,
    "Мука 1 класу, 1 кг", 600,
    "Сік Садочок мультифрукт, 1 літр", 300,
    "Іграшка L.O.L.", 260,
    "Цукор, 1 кг",120, 
    "Бойовий комар, одна штука", 20000
]
pc = len(products)
print("Товарів:",int(pc/2))
n = 1
for prod in range(0,len(products),2):
    print(str(n)+". "+ products[prod] +" - " + str(products[prod+1]) + " грн")
    n+=1
#перший варіант
price = 0
for prod in range(1,len(products),2):
    price += products[prod]
print("В звичайному магазині вас обанкротять на " + str(price) + " гривень")

#другий варіант
#другий топ
#там ще сайт є https://vaniademianov.github.io/shop/main
#але АПІшник лагає
import requests
cart = requests.get("https://remoteaccess01.pythonanywhere.com/showall").json()
ts = 0
for tov in cart:
    ts+=requests.get("https://remoteaccess01.pythonanywhere.com/describe_element/"+str(tov)+"/").json()[1]
print("Але в моєму магазинчику (http://bit.ly/3jYNQdE) з вас візьмуть всього навсього " + str(ts) + " гривень!")
