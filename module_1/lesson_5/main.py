"""      ALGO_STRING      """
# /// 147
# s = input()
# a_soni = s.upper().count('A')
# y_soni = s.upper().count('Y')
#
# print(f"{a_soni}\n{y_soni}")

# /// 148
# s = input().split()
# for i in s:
#     if i.startswith("A"):
#         print(i)
#     else:
#         pass
# /// 149
# s = input().split()
# c = 0
# find_str = ''
# for i in s:
#     if i.endswith('NA'):
#         c += 1
#         find_str += i + " "
# print(f"{c}\n{find_str}")


# /// 150
# s = input().split()
# for i in s:
#     if 'info' in i.lower():
#         print(i, end=' ')


# /// 151
# s = input()
# x = 0
# for i in s:
#     if i in "AEOUIouiea":
#         x += 1
#
# print(x)

# /// 152
# s = input()
# matn = ''.join(reversed(s))
# print(matn)

# /// 153
# s = input().split()
# for i in s:
#     print(i, len(i))

# /// 154
# num = input()
# s = 0
# for i in num:
#     if i.isdigit():
#         s += int(i)
# print(s)

# /// 155
# s = input().split()
# summ = 0
# for i in s:
#     if i[0].isupper():
#         summ += 1
# print(summ)

# /// 156
# s = input().split()
# i, j = map(int, input().split())
# s[i - 1], s[j - 1] = s[j - 1], s[i - 1]
# print(' '.join(s))


# /// 157
# a = input().split()
# place = int(input())
# a[place - 1] = "TATU"
# print(' '.join(a))

# /// 158
# a = input().split()
# toq, juft = 0, 0
# for i in a:
#     uzunlik = len(i)
#     if uzunlik % 2 == 0:
#         juft += 1
#     else:
#         toq += 1
# print(toq * juft)

# /// 159
# a = input().split()
# summ = 0
# for i in a:
#     if i.startswith('a') and i.endswith('b'):
#         summ += 1
# print(summ)

# /// 160
# s = input()
# matn = s.swapcase()
# print(matn)

# ///161
# max_card = int(input())
# cards = input()
# tmp = "ASSALOM"
# for i in tmp:
#     if tmp.count(i) > cards.count(i):
#         print("NO")
#         break
# else:
#     print("YES")


# /// 162
# s=int(input()), print(input().replace('$',""))

# /// 163
# S = input().split()
# tmp = max(S, key=len)
# print(tmp)

# /// 164
# matn = input()
# L, R = map(int, input().split())
# if R < L:
#     print(matn[R - 1: L][::-1])
# else:
#     print(matn[L - 1: R])


"""   lesson 7-8   """
# /// task_1
# sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# print()

# def is_palindrome(word):
#     return word==word[::-1]
# print(is_palindrome("ikki"))
# print(is_palindrome("bir"))

# i = input(">>>")
# print(i==i[::-1])

# i = " Lor56em Ips2um is simp17ly dummy text of the prin8ting and typesetting industry "
# print(i)
# print(i.isdigit())


# i="Lorem       Ipsum        is       simply "
# print(" ".join(i.split()))
# res=""
# for a in i.split():
#     res+=a[::-1]
# print(res)
# print(*i[::-1].split()[::-1])

# i="Lorem Ipsum is simply "
# print(i.split()
#       [len(i)//2])
#
"""
"hPrBKWDH8y8c6Lt5NQZWQ"  -->  "865"
"ynMAisVpHEqpqHBqTrwH"  -->  "One more run!"
"555"                   -->  "5"
"""

# a="ynMAisVpHEqpqHBqTrwH"
# res=""
# print(a)
# for i in a:
#     if i.isdigit() and i not in res:
#         res+=i
# if res:
#     print(res)
# else:
#     print("One more run!")

# a="aiopz"
# b="abcdefghijklmnopqrstuwxyz"
# for i in a:

# alpha = 'abdegopqDAOPRQ'
# res = 'IMBAWEjlGRTDWetPS'
# for i in res:
#     if i alpha:
#         print(i)

# arr = [110, 111, 112, 113, 114, 115]
# print(f"{chr(arr[1])}{chr(arr[-4])}{chr(arr[-2])}{chr(arr[0])}")
# print(f"{chr(arr[0])}{chr(arr[1])}{chr(arr[-2])}{chr(arr[-1])}")
# print(f"{chr(arr[-1])}{chr(arr[-2])}{chr(arr[1])}{chr(arr[0])}")
# print(f"{chr(arr[0])}{chr(arr[1])}{chr(arr[-2])}{chr(arr[-1])}")


# alpha = "zyxwvutsrqponmlkjihgfedcba!? "
# arr = ['24', '12', '23', '22', '4', '26', '9', '8']
# res = ""
# for i in arr:
#     res+=alpha[int(i) - 1]
# print(res)

# ['24', '12', '23', '22', '4', '26', '9', '8'], 'codewars'

# a = ["John3", "My0", "is2", "name1", ".4"]
# a.sort(reverse=False, key=lambda x: x[-1])
# print(a)
#
# for i in a:
#     print(i[:-1], end=' ')

# a=[21,2,7,8,10,3]
# a.sort(key=lambda x: x if x%2==0 else -x)
# print(a)

# a = [1, 2, 3, 4, 5, 6]
# print(id(a),a)
# a.append(a[0])
# a.pop(0)
# print(id(a),a)

# l = int(input())
# a = list(map(int, input().split()))
# summa = sum(a) / l
# tmp = []
# for i in a:
#     if summa > i:
#         tmp.append(i)
# print(f"{sum(tmp) / len(tmp):.2f}")


# ['$56.64', '$33.59', '$29.49', '$94.20', '$44.94']

# a1 = '$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94'.split()
# for i in range(len(a1)):
#     tmp=0
#     for j in a1[i]:
#         if j.isdigit():
#            tmp+=j
#     a1[i]="$"


# /// 101
# n = int(input())
# massiv = list(map(int, input().split()))
# orta = sum(massiv) / n
# tmp = []
# for i in massiv:
#     if i < orta:
#         tmp.append(i)
# print(f"{sum(tmp) / len(tmp):.2f}")


# /// 102
# n = int(input())
# massiv = list(map(int, input().split()))
# a, b = map(int, input().split())
# mini = min(massiv)
#
# for i in range(len(massiv)):
#     if a - 1 <= i <= b - 1:
#         massiv[i] = massiv[i] / mini + 0.000001
#
# for i in massiv:
#     print(f"{i:.1f}", end=" ")

# /// 103
# n = int(input())
# massiv = list(map(int, input().split()))
# k, l = map(int, input().split())
# tmp = []
# for i in range(len(massiv)):
#     if k - 1 <= i <= l - 1:
#         tmp.append(massiv[i])
# print(f"{sum(tmp) / len(tmp):.1f}")

# /// 105
# n = int(input())
# massiv = list(map(int, input().split()))
# k, l = map(int, input().split())
# tmp = []
# for i in range(len(massiv)):
#     if not k - 1 <= i <= l - 1:
#         tmp.append(massiv[i])
# print(f"{sum(tmp) / len(tmp):.2f}")

# /// 106
# n = int(input())
# massiv = list(map(int, input().split()))
# summ = 0
# for i in massiv:
#     summ += i ** 2
# print(summ)


# /// 107
# n = int(input())
# massiv = list(map(int, input().split()))
# maxi=max(massiv)
# for i in range(len(massiv)):
#     massiv[i]=massiv[i]/maxi
# for i in massiv:
#     print(f"{i:.2f}",end=" ")

# /// 108
# n = int(input())
# massiv = list(map(int, input().split()))
# mini=min(massiv)
# for i in range(len(massiv)):
#     massiv[i]=massiv[i]/mini
# for i in massiv:
#     print(f"{i:.2f}",end=" ")

# /// 109
# from math import log
#
# n = int(input())
# massiv = list(map(int, input().split()))
# m = int(input())
# summ = 1
# for i in massiv:
#     if i > m:
#         summ *= i
# print(f"{log(summ):.2f}")

# /// 110
# n = int(input())
# massiv = list(map(int, input().split()))
# k, m = map(int, input().split())
# summ = 1
# for i in massiv:
#     if k == i or m == i:
#         summ *= i
# print(summ)

# /// 111
# N = int(input())
# a = list(map(int, input().split()))
# M = int(input())
# summ = 0
# for i in a:
#         if i > M:
#                 summ += i
# print(summ)

# /// 112
# N = int(input())
# a = list(map(int, input().split()))
# summ,tmp=1,0
# for i in range(N):
#         if (i+1)%2==0:
#                 tmp+=a[i]
#         else:
#             summ *= a[i]
# print(f"{(summ/tmp):.2f}")

# /// 113
# N = int(input())
# a = list(map(int, input().split()))
# print(f"{sum(b := list(filter(lambda x: x < 0, a))) / len(b):.2f}")

# /// 114
# from math import sin
#
# N = int(input())
# a = list(map(int, input().split()))
# summ = 1
# for i in a:
#     if i % 2 == 0 or i % 5 == 0:
#         summ *= i
# print(f"{(sin(summ)):.2f}")

# /// 115
# N = int(input())
# a = list(map(int, input().split()))
# M = int(input())
# summ = 0
# for i in a:
#     if i < M:
#         summ += i ** 2
# print(summ)

# /// 116
# n = int(input())
# massiv = list(map(int, input().split()))
# print(*[f"{i / max(massiv)+.00001:.2f}" for i in massiv])


# /// 117
# n = int(input())
# massiv = list(map(int, input().split()))
# summ = 0
# for i in range(len(massiv)):
#     if (i + 1) % 2 == 1:
#         summ += massiv[i]
# print(summ)

# /// 118
# n = int(input())
# massiv = list(map(int, input().split()))
# print(f"{sum(b := list(filter(lambda x: x % 2 == 1, massiv))) / len(b)+.00001:.2f}")


# /// 120
# n = int(input())
# massiv = list(map(int, input().split()))
# x, y = map(int, input().split())
# summ = 0
# for i in massiv:
#     if not x <= i <= y:
#         summ += 1
# print(summ)

# /// 121
# N = int(input())
# a = list(map(int, input().split()))
# M = int(input())
# print(sum(a[M:]))

# /// 122
# N = int(input())
# a = list(map(int, input().split()))
# summ = 0
# tmp = 0
# for i in a:
#     summ += i ** 2
# for i in a:
#     tmp += i / N
# print(f"{(summ)}\n{(tmp):.2f}")

# /// 123
# n = input()
# l = list(map(int, input().split()))
# summa = sum(l[1::2])
# print(*[f'{i / summa:.2f}' if i % 2 and i > 0 else f'{i:.2f}' for i in l])

# /// 124
# n = int(input())
# a = list(map(int, input().split()))
# k = int(input()) - 1
# k_el=a[k]
# maxi = max(a)
# for i, val in enumerate(a):
#        if val == maxi:
#               a[i] = k_el
# a[k] = maxi
# print(*a)

# /// 125
# N = int(input())
# A = list(map(int, input().split()))
# x , y = map(int, input().split())
# summ = 0
# for i in range(len(A)):
#     if x-1 <= i <= y-1:
#         summ += A[i]**3
# print(summ)

# /// 126
# from math import log
#
# n = int(input())
# massiv = list(map(int, input().split()))
# summ = log(sum(massiv) / n)
# tmp = [f"{summ:.2f}" if i < 0 else f"{i:.2f}" for i in massiv]
# print(*tmp)

# /// 127
# n = int(input())
# massiv = list(map(int, input().split()))
# summ = min(massiv)
# tmp = [summ ** 2 if i < 0 else i for i in massiv]
# print(*tmp)

# /// 128
# N = int(input())
# a = list(map(int, input().split()))
# print(f"{sum(b := list(filter(lambda x: x % 2==0, a))) / len(b):.2f}")


# /// 129
# N = int(input())
# a = list(map(int, input().split()))
# summ = 0
# for i in a:
#     if i % 2 == 0 or i % 5 == 0 or i % 3 == 0:
#         summ += i
# print(summ)

# /// 1920
# nums=input()
# print([nums[i] for i in nums])

# /// 1470
# nums=[2,5,1,3,4,7]
# n=3
# (l:=[]), [l.extend([nums[:n][i],nums[n:][i]])for i in nums] ,print(l)

# Candies=[2,3,5,1,3]
# extraCandies=3
#
# for i in Candies:

# nums=[8,1,2,2,3]
# tmp=[]
# for i in range(len(nums)):
#     summ = 0
#     for j in range(len(nums)):
#         if nums[i]>nums[j]:
#             summ+=1
#     tmp.append(summ)
# print(tmp)

# d = {
#     "12" : [1,2,3],
#     "13" : [6,2,3],
#     "14" : [1,3,3],
#     "15" : [1,2,3 ],
# }
# d["12"].append(sum(d["12"]))
# print(d["12"])

todos= [
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False

  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": False

  },
  {
    "userId": 1,
    "id": 3,
    "title": "fugiat veniam minus",
    "completed": False

  },
  {
    "userId": 1,
    "id": 4,
    "title": "et porro tempora",
    "completed": True

  },
  {
    "userId": 1,
    "id": 5,
    "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
    "completed": False

  },
  {
    "userId": 1,
    "id": 6,
    "title": "qui ullam ratione quibusdam voluptatem quia omnis",
    "completed": False

  },
  {
    "userId": 1,
    "id": 7,
    "title": "illo expedita consequatur quia in",
    "completed": False

  },
  {
    "userId": 1,
    "id": 8,
    "title": "quo adipisci enim quam ut ab",
    "completed": True

  },
  {
    "userId": 1,
    "id": 9,
    "title": "molestiae perspiciatis ipsa",
    "completed": False

  },
  {
    "userId": 1,
    "id": 10,
    "title": "illo est ratione doloremque quia maiores aut",
    "completed": True

  },
  {
    "userId": 1,
    "id": 11,
    "title": "vero rerum temporibus dolor",
    "completed": True

  },
  {
    "userId": 1,
    "id": 12,
    "title": "ipsa repellendus fugit nisi",
    "completed": True

  },
  {
    "userId": 1,
    "id": 13,
    "title": "et doloremque nulla",
    "completed": False

  },
  {
    "userId": 1,
    "id": 14,
    "title": "repellendus sunt dolores architecto voluptatum",
    "completed": True

  },
  {
    "userId": 1,
    "id": 15,
    "title": "ab voluptatum amet voluptas",
    "completed": True

  },
  {
    "userId": 1,
    "id": 16,
    "title": "accusamus eos facilis sint et aut voluptatem",
    "completed": True

  },
  {
    "userId": 1,
    "id": 17,
    "title": "quo laboriosam deleniti aut qui",
    "completed": True

  },
  {
    "userId": 1,
    "id": 18,
    "title": "dolorum est consequatur ea mollitia in culpa",
    "completed": False

  },
  {
    "userId": 1,
    "id": 19,
    "title": "molestiae ipsa aut voluptatibus pariatur dolor nihil",
    "completed": True

  },
  {
    "userId": 1,
    "id": 20,
    "title": "ullam nobis libero sapiente ad optio sint",
    "completed": True

  },
  {
    "userId": 2,
    "id": 21,
    "title": "suscipit repellat esse quibusdam voluptatem incidunt",
    "completed": False

  },
  {
    "userId": 2,
    "id": 22,
    "title": "distinctio vitae autem nihil ut molestias quo",
    "completed": True

  },
  {
    "userId": 2,
    "id": 23,
    "title": "et itaque necessitatibus maxime molestiae qui quas velit",
    "completed": False

  },
  {
    "userId": 2,
    "id": 24,
    "title": "adipisci non ad dicta qui amet quaerat doloribus ea",
    "completed": False

  },
  {
    "userId": 2,
    "id": 25,
    "title": "voluptas quo tenetur perspiciatis explicabo natus",
    "completed": True

  },
  {
    "userId": 2,
    "id": 26,
    "title": "aliquam aut quasi",
    "completed": True

  },
  {
    "userId": 2,
    "id": 27,
    "title": "veritatis pariatur delectus",
    "completed": True

  },
  {
    "userId": 2,
    "id": 28,
    "title": "nesciunt totam sit blanditiis sit",
    "completed": False

  },
  {
    "userId": 2,
    "id": 29,
    "title": "laborum aut in quam",
    "completed": False

  },
  {
    "userId": 2,
    "id": 30,
    "title": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis",
    "completed": True

  },
  {
    "userId": 2,
    "id": 31,
    "title": "repudiandae totam in est sint facere fuga",
    "completed": False

  },
  {
    "userId": 2,
    "id": 32,
    "title": "earum doloribus ea doloremque quis",
    "completed": False

  },
  {
    "userId": 2,
    "id": 33,
    "title": "sint sit aut vero",
    "completed": False

  },
  {
    "userId": 2,
    "id": 34,
    "title": "porro aut necessitatibus eaque distinctio",
    "completed": False

  },
  {
    "userId": 2,
    "id": 35,
    "title": "repellendus veritatis molestias dicta incidunt",
    "completed": True

  },
  {
    "userId": 2,
    "id": 36,
    "title": "excepturi deleniti adipisci voluptatem et neque optio illum ad",
    "completed": True

  },
  {
    "userId": 2,
    "id": 37,
    "title": "sunt cum tempora",
    "completed": False

  },
  {
    "userId": 2,
    "id": 38,
    "title": "totam quia non",
    "completed": False

  },
  {
    "userId": 2,
    "id": 39,
    "title": "doloremque quibusdam asperiores libero corrupti illum qui omnis",
    "completed": False

  },
  {
    "userId": 2,
    "id": 40,
    "title": "totam atque quo nesciunt",
    "completed": True

  },
  {
    "userId": 3,
    "id": 41,
    "title": "aliquid amet impedit consequatur aspernatur placeat eaque fugiat suscipit",
    "completed": False

  },
  {
    "userId": 3,
    "id": 42,
    "title": "rerum perferendis error quia ut eveniet",
    "completed": False

  },
  {
    "userId": 3,
    "id": 43,
    "title": "tempore ut sint quis recusandae",
    "completed": True

  },
  {
    "userId": 3,
    "id": 44,
    "title": "cum debitis quis accusamus doloremque ipsa natus sapiente omnis",
    "completed": True

  },
  {
    "userId": 3,
    "id": 45,
    "title": "velit soluta adipisci molestias reiciendis harum",
    "completed": False

  },
  {
    "userId": 3,
    "id": 46,
    "title": "vel voluptatem repellat nihil placeat corporis",
    "completed": False

  },
  {
    "userId": 3,
    "id": 47,
    "title": "nam qui rerum fugiat accusamus",
    "completed": False

  },
  {
    "userId": 3,
    "id": 48,
    "title": "sit reprehenderit omnis quia",
    "completed": False

  },
  {
    "userId": 3,
    "id": 49,
    "title": "ut necessitatibus aut maiores debitis officia blanditiis velit et",
    "completed": False

  },
  {
    "userId": 3,
    "id": 50,
    "title": "cupiditate necessitatibus ullam aut quis dolor voluptate",
    "completed": True

  },
  {
    "userId": 3,
    "id": 51,
    "title": "distinctio exercitationem ab doloribus",
    "completed": False

  },
  {
    "userId": 3,
    "id": 52,
    "title": "nesciunt dolorum quis recusandae ad pariatur ratione",
    "completed": False

  },
  {
    "userId": 3,
    "id": 53,
    "title": "qui labore est occaecati recusandae aliquid quam",
    "completed": False

  },
  {
    "userId": 3,
    "id": 54,
    "title": "quis et est ut voluptate quam dolor",
    "completed": True

  },
  {
    "userId": 3,
    "id": 55,
    "title": "voluptatum omnis minima qui occaecati provident nulla voluptatem ratione",
    "completed": True

  },
  {
    "userId": 3,
    "id": 56,
    "title": "deleniti ea temporibus enim",
    "completed": True

  },
  {
    "userId": 3,
    "id": 57,
    "title": "pariatur et magnam ea doloribus similique voluptatem rerum quia",
    "completed": False

  },
  {
    "userId": 3,
    "id": 58,
    "title": "est dicta totam qui explicabo doloribus qui dignissimos",
    "completed": False

  },
  {
    "userId": 3,
    "id": 59,
    "title": "perspiciatis velit id laborum placeat iusto et aliquam odio",
    "completed": False

  },
  {
    "userId": 3,
    "id": 60,
    "title": "et sequi qui architecto ut adipisci",
    "completed": True

  },
  {
    "userId": 4,
    "id": 61,
    "title": "odit optio omnis qui sunt",
    "completed": True

  },
  {
    "userId": 4,
    "id": 62,
    "title": "et placeat et tempore aspernatur sint numquam",
    "completed": False

  },
  {
    "userId": 4,
    "id": 63,
    "title": "doloremque aut dolores quidem fuga qui nulla",
    "completed": True

  },
  {
    "userId": 4,
    "id": 64,
    "title": "voluptas consequatur qui ut quia magnam nemo esse",
    "completed": False

  },
  {
    "userId": 4,
    "id": 65,
    "title": "fugiat pariatur ratione ut asperiores necessitatibus magni",
    "completed": False

  },
  {
    "userId": 4,
    "id": 66,
    "title": "rerum eum molestias autem voluptatum sit optio",
    "completed": False

  },
  {
    "userId": 4,
    "id": 67,
    "title": "quia voluptatibus voluptatem quos similique maiores repellat",
    "completed": False

  },
  {
    "userId": 4,
    "id": 68,
    "title": "aut id perspiciatis voluptatem iusto",
    "completed": False

  },
  {
    "userId": 4,
    "id": 69,
    "title": "doloribus sint dolorum ab adipisci itaque dignissimos aliquam suscipit",
    "completed": False

  },
  {
    "userId": 4,
    "id": 70,
    "title": "ut sequi accusantium et mollitia delectus sunt",
    "completed": False

  },
  {
    "userId": 4,
    "id": 71,
    "title": "aut velit saepe ullam",
    "completed": False

  },
  {
    "userId": 4,
    "id": 72,
    "title": "praesentium facilis facere quis harum voluptatibus voluptatem eum",
    "completed": False

  },
  {
    "userId": 4,
    "id": 73,
    "title": "sint amet quia totam corporis qui exercitationem commodi",
    "completed": True

  },
  {
    "userId": 4,
    "id": 74,
    "title": "expedita tempore nobis eveniet laborum maiores",
    "completed": False

  },
  {
    "userId": 4,
    "id": 75,
    "title": "occaecati adipisci est possimus totam",
    "completed": False

  },
  {
    "userId": 4,
    "id": 76,
    "title": "sequi dolorem sed",
    "completed": True

  },
  {
    "userId": 4,
    "id": 77,
    "title": "maiores aut nesciunt delectus exercitationem vel assumenda eligendi at",
    "completed": False

  },
  {
    "userId": 4,
    "id": 78,
    "title": "reiciendis est magnam amet nemo iste recusandae impedit quaerat",
    "completed": False

  },
  {
    "userId": 4,
    "id": 79,
    "title": "eum ipsa maxime ut",
    "completed": True

  },
  {
    "userId": 4,
    "id": 80,
    "title": "tempore molestias dolores rerum sequi voluptates ipsum consequatur",
    "completed": True

  },
  {
    "userId": 5,
    "id": 81,
    "title": "suscipit qui totam",
    "completed": True

  },
  {
    "userId": 5,
    "id": 82,
    "title": "voluptates eum voluptas et dicta",
    "completed": False

  },
  {
    "userId": 5,
    "id": 83,
    "title": "quidem at rerum quis ex aut sit quam",
    "completed": True

  },
  {
    "userId": 5,
    "id": 84,
    "title": "sunt veritatis ut voluptate",
    "completed": False

  },
  {
    "userId": 5,
    "id": 85,
    "title": "et quia ad iste a",
    "completed": True

  },
  {
    "userId": 5,
    "id": 86,
    "title": "incidunt ut saepe autem",
    "completed": True

  },
  {
    "userId": 5,
    "id": 87,
    "title": "laudantium quae eligendi consequatur quia et vero autem",
    "completed": True

  },
  {
    "userId": 5,
    "id": 88,
    "title": "vitae aut excepturi laboriosam sint aliquam et et accusantium",
    "completed": False

  },
  {
    "userId": 5,
    "id": 89,
    "title": "sequi ut omnis et",
    "completed": True

  },
  {
    "userId": 5,
    "id": 90,
    "title": "molestiae nisi accusantium tenetur dolorem et",
    "completed": True

  },
  {
    "userId": 5,
    "id": 91,
    "title": "nulla quis consequatur saepe qui id expedita",
    "completed": True

  },
  {
    "userId": 5,
    "id": 92,
    "title": "in omnis laboriosam",
    "completed": True

  },
  {
    "userId": 5,
    "id": 93,
    "title": "odio iure consequatur molestiae quibusdam necessitatibus quia sint",
    "completed": True

  },
  {
    "userId": 5,
    "id": 94,
    "title": "facilis modi saepe mollitia",
    "completed": False

  },
  {
    "userId": 5,
    "id": 95,
    "title": "vel nihil et molestiae iusto assumenda nemo quo ut",
    "completed": True

  },
  {
    "userId": 5,
    "id": 96,
    "title": "nobis suscipit ducimus enim asperiores voluptas",
    "completed": False

  },
  {
    "userId": 5,
    "id": 97,
    "title": "dolorum laboriosam eos qui iure aliquam",
    "completed": False

  },
  {
    "userId": 5,
    "id": 98,
    "title": "debitis accusantium ut quo facilis nihil quis sapiente necessitatibus",
    "completed": True

  },
  {
    "userId": 5,
    "id": 99,
    "title": "neque voluptates ratione",
    "completed": False

  },
  {
    "userId": 5,
    "id": 100,
    "title": "excepturi a et neque qui expedita vel voluptate",
    "completed": False

  },
  {
    "userId": 6,
    "id": 101,
    "title": "explicabo enim cumque porro aperiam occaecati minima",
    "completed": False

  },
  {
    "userId": 6,
    "id": 102,
    "title": "sed ab consequatur",
    "completed": False

  },
  {
    "userId": 6,
    "id": 103,
    "title": "non sunt delectus illo nulla tenetur enim omnis",
    "completed": False

  },
  {
    "userId": 6,
    "id": 104,
    "title": "excepturi non laudantium quo",
    "completed": False

  },
  {
    "userId": 6,
    "id": 105,
    "title": "totam quia dolorem et illum repellat voluptas optio",
    "completed": True

  },
  {
    "userId": 6,
    "id": 106,
    "title": "ad illo quis voluptatem temporibus",
    "completed": True

  },
  {
    "userId": 6,
    "id": 107,
    "title": "praesentium facilis omnis laudantium fugit ad iusto nihil nesciunt",
    "completed": False

  },
  {
    "userId": 6,
    "id": 108,
    "title": "a eos eaque nihil et exercitationem incidunt delectus",
    "completed": True

  },
  {
    "userId": 6,
    "id": 109,
    "title": "autem temporibus harum quisquam in culpa",
    "completed": True

  },
  {
    "userId": 6,
    "id": 110,
    "title": "aut aut ea corporis",
    "completed": True

  },
  {
    "userId": 6,
    "id": 111,
    "title": "magni accusantium labore et id quis provident",
    "completed": False

  },
  {
    "userId": 6,
    "id": 112,
    "title": "consectetur impedit quisquam qui deserunt non rerum consequuntur eius",
    "completed": False

  },
  {
    "userId": 6,
    "id": 113,
    "title": "quia atque aliquam sunt impedit voluptatum rerum assumenda nisi",
    "completed": False

  },
  {
    "userId": 6,
    "id": 114,
    "title": "cupiditate quos possimus corporis quisquam exercitationem beatae",
    "completed": False

  },
  {
    "userId": 6,
    "id": 115,
    "title": "sed et ea eum",
    "completed": False

  },
  {
    "userId": 6,
    "id": 116,
    "title": "ipsa dolores vel facilis ut",
    "completed": True

  },
  {
    "userId": 6,
    "id": 117,
    "title": "sequi quae est et qui qui eveniet asperiores",
    "completed": False

  },
  {
    "userId": 6,
    "id": 118,
    "title": "quia modi consequatur vero fugiat",
    "completed": False

  },
  {
    "userId": 6,
    "id": 119,
    "title": "corporis ducimus ea perspiciatis iste",
    "completed": False

  },
  {
    "userId": 6,
    "id": 120,
    "title": "dolorem laboriosam vel voluptas et aliquam quasi",
    "completed": False

  },
  {
    "userId": 7,
    "id": 121,
    "title": "inventore aut nihil minima laudantium hic qui omnis",
    "completed": True

  },
  {
    "userId": 7,
    "id": 122,
    "title": "provident aut nobis culpa",
    "completed": True

  },
  {
    "userId": 7,
    "id": 123,
    "title": "esse et quis iste est earum aut impedit",
    "completed": False

  },
  {
    "userId": 7,
    "id": 124,
    "title": "qui consectetur id",
    "completed": False

  },
  {
    "userId": 7,
    "id": 125,
    "title": "aut quasi autem iste tempore illum possimus",
    "completed": False

  },
  {
    "userId": 7,
    "id": 126,
    "title": "ut asperiores perspiciatis veniam ipsum rerum saepe",
    "completed": True

  },
  {
    "userId": 7,
    "id": 127,
    "title": "voluptatem libero consectetur rerum ut",
    "completed": True

  },
  {
    "userId": 7,
    "id": 128,
    "title": "eius omnis est qui voluptatem autem",
    "completed": False

  },
  {
    "userId": 7,
    "id": 129,
    "title": "rerum culpa quis harum",
    "completed": False

  },
  {
    "userId": 7,
    "id": 130,
    "title": "nulla aliquid eveniet harum laborum libero alias ut unde",
    "completed": True

  },
  {
    "userId": 7,
    "id": 131,
    "title": "qui ea incidunt quis",
    "completed": False

  },
  {
    "userId": 7,
    "id": 132,
    "title": "qui molestiae voluptatibus velit iure harum quisquam",
    "completed": True

  },
  {
    "userId": 7,
    "id": 133,
    "title": "et labore eos enim rerum consequatur sunt",
    "completed": True

  },
  {
    "userId": 7,
    "id": 134,
    "title": "molestiae doloribus et laborum quod ea",
    "completed": False

  },
  {
    "userId": 7,
    "id": 135,
    "title": "facere ipsa nam eum voluptates reiciendis vero qui",
    "completed": False

  },
  {
    "userId": 7,
    "id": 136,
    "title": "asperiores illo tempora fuga sed ut quasi adipisci",
    "completed": False

  },
  {
    "userId": 7,
    "id": 137,
    "title": "qui sit non",
    "completed": False

  },
  {
    "userId": 7,
    "id": 138,
    "title": "placeat minima consequatur rem qui ut",
    "completed": True

  },
  {
    "userId": 7,
    "id": 139,
    "title": "consequatur doloribus id possimus voluptas a voluptatem",
    "completed": False

  },
  {
    "userId": 7,
    "id": 140,
    "title": "aut consectetur in blanditiis deserunt quia sed laboriosam",
    "completed": True

  },
  {
    "userId": 8,
    "id": 141,
    "title": "explicabo consectetur debitis voluptates quas quae culpa rerum non",
    "completed": True

  },
  {
    "userId": 8,
    "id": 142,
    "title": "maiores accusantium architecto necessitatibus reiciendis ea aut",
    "completed": True

  },
  {
    "userId": 8,
    "id": 143,
    "title": "eum non recusandae cupiditate animi",
    "completed": False

  },
  {
    "userId": 8,
    "id": 144,
    "title": "ut eum exercitationem sint",
    "completed": False

  },
  {
    "userId": 8,
    "id": 145,
    "title": "beatae qui ullam incidunt voluptatem non nisi aliquam",
    "completed": False

  },
  {
    "userId": 8,
    "id": 146,
    "title": "molestiae suscipit ratione nihil odio libero impedit vero totam",
    "completed": True

  },
  {
    "userId": 8,
    "id": 147,
    "title": "eum itaque quod reprehenderit et facilis dolor autem ut",
    "completed": True

  },
  {
    "userId": 8,
    "id": 148,
    "title": "esse quas et quo quasi exercitationem",
    "completed": False

  },
  {
    "userId": 8,
    "id": 149,
    "title": "animi voluptas quod perferendis est",
    "completed": False

  },
  {
    "userId": 8,
    "id": 150,
    "title": "eos amet tempore laudantium fugit a",
    "completed": False

  },
  {
    "userId": 8,
    "id": 151,
    "title": "accusamus adipisci dicta qui quo ea explicabo sed vero",
    "completed": True

  },
  {
    "userId": 8,
    "id": 152,
    "title": "odit eligendi recusandae doloremque cumque non",
    "completed": False

  },
  {
    "userId": 8,
    "id": 153,
    "title": "ea aperiam consequatur qui repellat eos",
    "completed": False

  },
  {
    "userId": 8,
    "id": 154,
    "title": "rerum non ex sapiente",
    "completed": True

  },
  {
    "userId": 8,
    "id": 155,
    "title": "voluptatem nobis consequatur et assumenda magnam",
    "completed": True

  },
  {
    "userId": 8,
    "id": 156,
    "title": "nam quia quia nulla repellat assumenda quibusdam sit nobis",
    "completed": True

  },
  {
    "userId": 8,
    "id": 157,
    "title": "dolorem veniam quisquam deserunt repellendus",
    "completed": True

  },
  {
    "userId": 8,
    "id": 158,
    "title": "debitis vitae delectus et harum accusamus aut deleniti a",
    "completed": True

  },
  {
    "userId": 8,
    "id": 159,
    "title": "debitis adipisci quibusdam aliquam sed dolore ea praesentium nobis",
    "completed": True

  },
  {
    "userId": 8,
    "id": 160,
    "title": "et praesentium aliquam est",
    "completed": False

  },
  {
    "userId": 9,
    "id": 161,
    "title": "ex hic consequuntur earum omnis alias ut occaecati culpa",
    "completed": True

  },
  {
    "userId": 9,
    "id": 162,
    "title": "omnis laboriosam molestias animi sunt dolore",
    "completed": True

  },
  {
    "userId": 9,
    "id": 163,
    "title": "natus corrupti maxime laudantium et voluptatem laboriosam odit",
    "completed": False

  },
  {
    "userId": 9,
    "id": 164,
    "title": "reprehenderit quos aut aut consequatur est sed",
    "completed": False

  },
  {
    "userId": 9,
    "id": 165,
    "title": "fugiat perferendis sed aut quidem",
    "completed": False

  },
  {
    "userId": 9,
    "id": 166,
    "title": "quos quo possimus suscipit minima ut",
    "completed": False

  },
  {
    "userId": 9,
    "id": 167,
    "title": "et quis minus quo a asperiores molestiae",
    "completed": False

  },
  {
    "userId": 9,
    "id": 168,
    "title": "recusandae quia qui sunt libero",
    "completed": False

  },
  {
    "userId": 9,
    "id": 169,
    "title": "ea odio perferendis officiis",
    "completed": True

  },
  {
    "userId": 9,
    "id": 170,
    "title": "quisquam aliquam quia doloribus aut",
    "completed": False

  },
  {
    "userId": 9,
    "id": 171,
    "title": "fugiat aut voluptatibus corrupti deleniti velit iste odio",
    "completed": True

  },
  {
    "userId": 9,
    "id": 172,
    "title": "et provident amet rerum consectetur et voluptatum",
    "completed": False

  },
  {
    "userId": 9,
    "id": 173,
    "title": "harum ad aperiam quis",
    "completed": False

  },
  {
    "userId": 9,
    "id": 174,
    "title": "similique aut quo",
    "completed": False

  },
  {
    "userId": 9,
    "id": 175,
    "title": "laudantium eius officia perferendis provident perspiciatis asperiores",
    "completed": True

  },
  {
    "userId": 9,
    "id": 176,
    "title": "magni soluta corrupti ut maiores rem quidem",
    "completed": False

  },
  {
    "userId": 9,
    "id": 177,
    "title": "et placeat temporibus voluptas est tempora quos quibusdam",
    "completed": False

  },
  {
    "userId": 9,
    "id": 178,
    "title": "nesciunt itaque commodi tempore",
    "completed": True

  },
  {
    "userId": 9,
    "id": 179,
    "title": "omnis consequuntur cupiditate impedit itaque ipsam quo",
    "completed": True

  },
  {
    "userId": 9,
    "id": 180,
    "title": "debitis nisi et dolorem repellat et",
    "completed": True

  },
  {
    "userId": 10,
    "id": 181,
    "title": "ut cupiditate sequi aliquam fuga maiores",
    "completed": False

  },
  {
    "userId": 10,
    "id": 182,
    "title": "inventore saepe cumque et aut illum enim",
    "completed": True

  },
  {
    "userId": 10,
    "id": 183,
    "title": "omnis nulla eum aliquam distinctio",
    "completed": True

  },
  {
    "userId": 10,
    "id": 184,
    "title": "molestias modi perferendis perspiciatis",
    "completed": False

  },
  {
    "userId": 10,
    "id": 185,
    "title": "voluptates dignissimos sed doloribus animi quaerat aut",
    "completed": False

  },
  {
    "userId": 10,
    "id": 186,
    "title": "explicabo odio est et",
    "completed": False

  },
  {
    "userId": 10,
    "id": 187,
    "title": "consequuntur animi possimus",
    "completed": False

  },
  {
    "userId": 10,
    "id": 188,
    "title": "vel non beatae est",
    "completed": True

  },
  {
    "userId": 10,
    "id": 189,
    "title": "culpa eius et voluptatem et",
    "completed": True

  },
  {
    "userId": 10,
    "id": 190,
    "title": "accusamus sint iusto et voluptatem exercitationem",
    "completed": True

  },
  {
    "userId": 10,
    "id": 191,
    "title": "temporibus atque distinctio omnis eius impedit tempore molestias pariatur",
    "completed": True

  },
  {
    "userId": 10,
    "id": 192,
    "title": "ut quas possimus exercitationem sint voluptates",
    "completed": False

  },
  {
    "userId": 10,
    "id": 193,
    "title": "rerum debitis voluptatem qui eveniet tempora distinctio a",
    "completed": True

  },
  {
    "userId": 10,
    "id": 194,
    "title": "sed ut vero sit molestiae",
    "completed": False

  },
  {
    "userId": 10,
    "id": 195,
    "title": "rerum ex veniam mollitia voluptatibus pariatur",
    "completed": True

  },
  {
    "userId": 10,
    "id": 196,
    "title": "consequuntur aut ut fugit similique",
    "completed": True

  },
  {
    "userId": 10,
    "id": 197,
    "title": "dignissimos quo nobis earum saepe",
    "completed": True

  },
  {
    "userId": 10,
    "id": 198,
    "title": "quis eius est sint explicabo",
    "completed": True

  },
  {
    "userId": 10,
    "id": 199,
    "title": "numquam repellendus a magnam",
    "completed": True

  },
  {
    "userId": 10,
    "id": 200,
    "title": "ipsam aperiam voluptates qui",
    "completed": False

  }
]
# def filter(**kwargs):
#   result = []
#   for todo in todos:
#     if todo.get(list(kwargs.keys())[0]) == list(kwargs.values())[0]:
#       result.append(todo)
#
#   return result




# 1720
# encoded=[1,2,3]
# first=1
# tmp = [first]
# for i in encoded:
#   tmp.append(tmp[-1] ^ i)
# print(tmp)

# 2859
# nums = [5,10,1,5,2]
# k = 1
# summ=0
# for i, val in enumerate(nums) :
#   if str(bin(i))[2:].count('1')==k:
#       summ += val
# print(summ)

# 1750
# s = "ca"
# while len(s)>=2 and s[0]==s[-1]:
#   s=s.strip(s[0])
# print(len(s))

# 1732
# gain = [-5,1,5,0,-7]
# summ=0
# tmp=0
# for i in gain:
#   summ+=i
#   tmp = max(summ, tmp)
# print(tmp)

# 1827
# nums = [1,1,1]
# tmp=nums[0]
# summ=0
# for i in nums[1:]:
#   if tmp>=i:
#     summ+=tmp+1-i
#     tmp=tmp+1
#   else:
#     tmp=i
# print(tmp)

# n = "8638"
# summ = 0
# for i in n:

d = [
    {
        "id": 1,
        "product_name": "Iphone 15 pro MAX",
        "price": "1800$",
        "count": 10,
        "color": ["RED", "BLACK", "GRAY", "GOLD", "WHITE"]
    },
    {
        "id": 2,
        "product_name": "Iphone 14 pro MAX",
        "price": "1000$",
        "count": 20,
        "color": ["RED", "BLACK", "GRAY", "GOLD", "WHITE"]
    }
]
# tmp=[]
# for i in d:
#
#    tmp += .append("GREEN")
# print(d)

# c = {}
# input = "asdfghytresda"
# for i in input:
#   c[i] = c.get(i, 0) + 1
# print(*c.items(), sep="\n")
