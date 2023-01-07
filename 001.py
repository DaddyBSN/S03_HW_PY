# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

listA = []
listB = []
summ = 0
a = int(input())
for i in range(a):
    b = int(input())
    listA.append(b)

for i in range(len(listA)):
    if i % 2 != 0:
        listB.append(listA[i])

print(f'{listA} -> на нечетных позициях элементы', end= ' ')
for i in range(len(listB) -1):
    print(listB[i], end= ' и ')
print(f'{listB[-1]}, ответ:', end= ' ')

for i in range(len(listB)):
    summ += listB[i]

print(summ)

