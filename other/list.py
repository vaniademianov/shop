students = ["Vania", "Ivan", "Vanushka", "Vanushik", "Vanichka"]
print(students)
print("Students count:", len(students))
index = int(input("Enter number of student: "))-1


print(students[index])
a = 1
while a <= len(students):
    print(str(a)+". "+students[a-1]) 
    a+=1


for i in range(0,10,2):
    print(i)

b = 0
a = 1
while b <= len(students):
    if (b % 2) == 0:
        print(str(a)+". "+students[b]) 
        a+=1
    b+=1