""""""
"""
Sorting Algoritms:
    1->Selection sort
    2->Insertion sort
    3->Buble sort
"""

find = 20
l = [11, 15, 20, 30, 45, 50, 78]
L = 0
H = len(l) - 1
while L <= H:
    midle = (L + H) // 2
    if l[midle] == find:
        print(midle)
        break
    if l[midle] > find:
        H = midle - 1
    else:
        L = midle + 1
else:
    print("Not found")
