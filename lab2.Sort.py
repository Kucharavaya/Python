import random
import datetime
import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика

def BubbleSort(A):                  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a


def QuickSort(A, fst, lst):         # быстрая сортировка
    if fst >= lst:
        return

    #i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst+1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger+1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger-1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller-1)
    QuickSort(A, first_bigger, lst)

"""
3. Функция шейкерной (коктейльной) сортировки shaker - модификации пузырьковой:
Цикл 1 – по i от 0 до N/2 :				            # i - счетчик пар проходов по списку,
                                                    # которых в 2 раза меньше, чем в пузырьковой
Цикл 2 – по j от i до N-1-i :			            # j - номер позиции при проходе по списку слева направо
    Условие – если A[j]>A[j+1] :	                # сравнение текущего элемента со следующим
        Действие – перестановка местами A[j] и A[j+1]
Цикл 3 – по j от N-2-i до i+1 : 		            # j - номер позиции при проходе по списку справа налево
    Условие если A[j]<A[j-1] :		                # сравнение текущего элемента с предыдущим
        Действие – перестановка местами A[j] и A[j-1]
"""
def ShakerSort(A):
    n = len(A)
    for i in range(n//2):
        # Проход слева направо
        for j in range(i, n-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

        # Проход справа налево
        for j in range(n-2-i, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой", "Время shaker"])
x=[]
y1=[]
y2=[]
y3 =[]



for N in range(1000,5001,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    #print(A)

    B = A.copy()
    C = A.copy()
    # print(B)

    # BubbleSort(A)
    print("---")
    # print(A)


    # QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Пузырьковая сортировка   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B)-1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()
    ShakerSort(C)
    t6 = datetime.datetime.now()
    y3.append((t6-t5).total_seconds())
    print("Shaker   " +str(N)+"   заняла   "+str((t6-t5).total_seconds()) + "c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds()), str((t6-t5).total_seconds())])

print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C5")
plt.show()
