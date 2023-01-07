# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

listA = []
listB = []

a = int(input())
for i in range(a):
    b = int(input())
    listA.append(b)

if len(listA) % 2 !=0:
    for i in range((len(listA) + 1) // 2):
        listB.append(listA[i] * listA[-i-1])
else:
    for i in range(len(listA)):
        listB.append(listA[i] * listA[-i])

print(f'{listA} => ', end= ' ')
print(listB)
