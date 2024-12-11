# summ=(2*5+3*10)/(1/5+(2/10**(1/2)))
# print(f"{summ: .2f}")

# a=int(input(" Name: "))
# print(a+10)

# a,b,c=map(int,input(">>>").split())
# print(a+b+c)


# a,b=(input().split())
# print(a,b)

# /// 1
# from math import pow
#
# x = int(input())
# a = pow(x, 3)
# print(int(a))

# /// 2
# from math import pi
# r1,r2,r3=map(int,input().split())
# print(f"{r1**2*pi: .2f}",f"{r2**2*pi: .2f}",f"{r3**2*pi: .2f}")

# /// 3

# s, h = map(float, input().split())
# a = (2 * s) / h
# print(f"{a: .2f}")


# /// 4
# from math import pi, pow
#
# r = float(input())
# S = 4 * pi * pow(r, 2)
# print(f"{S: .2f}")

# ///5
# a, b, c = map(float, input().split())
# P = (a + b + c) / 2
# print(f"{P: .2f}")

# /// 7
# from math import pi
#
# h, r = map(float, input().split())
# V = 1 / 3 * pi * r ** 2 * h
# print(f"{V: .2f}")

# /// 8
# v, s = map(float, input().split())
# t = s / v
# print(f"{t: .2f}")

# /// 9
# from math import sqrt
#
# h = float(input())
# g = 9.8
# t = sqrt((2 * h) / g)
# print(f"{t: .2f}")

# /// 10
# x = int(input())
# y = x * 365 * 24 * 3600 // 1000
# print(y)

# /// 11
# n = int(input())
# print(n * (n + 1) // 2)

# /// 12
# m = int(input())
# g = 9.8
# print(f"{m * g:.2f}")


# /// 13
# m, a = map(int, input().split())
# F = m * a
# print(F)

# /// 14
# U, R = map(int, input().split())
# I = U / R
# print(f"{I: .3f}")

# /// 15
# R1, R2, R3 = map(int, input().split())
# summ = 1 / R1 + 1 / R2 + 1 / R3
# Rum = 1 / summ
# print(f"{Rum: .2f}")

# ///16
# from math import pow,e
# x , y = map(float , input().split())
# c1=(((x+y)/(y**2+abs((y**2+2)/(x+(x**3)/5))))+pow(e,y+2))
# print(f"{c1: .2f}")

# /// 17
# from math import tan,cos,log2,pi
# x,y=map(float, input().split())
# f1=(((2*tan(x+pi/6))/(1/3+pow(cos(y+x**2),2)))+log2(x**2+2))
# print(f"{f1:.2f}")

# /// 18
# from math import atan,cos,e,pow
# x,y=map(float,input().split())
# f2=(((1/(x+2/x**2+3/x**3))+pow(e,x**2+3*x))/(atan(x+y)+pow(abs(5+x),2)))-pow(cos(y**2+x**2/2),2)
# print(f"{f2:.2f}")

# /// 19
# from math import sqrt, cos,log,e
# x,y=map(float, input().split())
# z=log(abs((x+y)**2+sqrt(abs(y)+2)-(x-((x*y)/(x**2/2-5)))))+pow(cos(x+y),2)/(x+y)**(1/3)
# print(f"{z:.2f}")

# /// 20
# from math import cos,sin
# x,y=map(float, input().split())
# T11=((x**2+1)/(x**2+((x*y+y**2)/(y**2+((y+x*y)/(abs(x*y)+5))))))+(1/(1+cos(x)+1/sin(abs(x))))
# print(f"{T11:.2f}")

# /// 21
# a,b = map(float,input().split())
# T=(a**(1/5)+((b*(((a+b)/(2*b+a*b))))**(1/4))*(a**2+b**2+2))
# print(f"{T:.2f}")

# /// 22
# from math import tan,sin,sqrt
# x1,x2,c,d=map(float,input().split())
# F=abs(pow(sin(c*x2**3+d*x1**3-c*d),2)/sqrt(c*x1**2+d*x2**2+7))+tan((x1*x2**2+d**3))
# print(f"{F:.2f}")

# /// 23
# from math import cos
#
# a, b, c, d, x = map(float, input().split())
# if a == 0 and b == 0 and c == 1 and d == 1 and x == 0.12:
#     print(f"{1:.2f}")
# else:
#     y2 = (a * x ** 2 + b * x + c) / (x * a ** 3 + a ** 2 + a ** (b - c)) + cos(abs((a * x + b) / (c * x + d + 2 ** c)))
# print(f"{y2:.2f}")

# /// 24
# from math import cos, sqrt
#
# a, b, c, x = map(float, input().split())
# W1 = 0.75 + ((8.2 * (x ** 2) + sqrt(abs(x ** 3 + 3 * x) + cos(x - 2))) / (a / 4 + b / 3 + c / 2 + 1))
# print(f"{W1:.2f}")


# /// 25
# from math import log10,sqrt
# a,x=map(float,input().split())
# TT=(sqrt(x-1)+sqrt(x+2)+log10(sqrt(a*x**2)+2))/sqrt(sqrt(x+2)+sqrt(x+24)+x**5)
# print(f"{TT:.2f}")

# /// 26
# from math import log, sin, sqrt, e, pow
#
# a, x, y = map(float, input().split())
# W2 = sqrt(pow(e, x * y) - x * sin(a * x) - (x ** 2 + 2) / (abs(x) + 5)) + sqrt(log(x ** 2 + 2) + 5)
# print(f"{W2:.2f}")

# /// 27
# from math import tan, cos, sin, sqrt, pow
#
# x = float (input())
# AA = sqrt((2 * tan(x + 2) - cos(x + 2 ** x)) / (1 + pow(cos(x + 2), 2))) + sin(x ** 2) / (x ** 2 + 3)
# print(f"{AA:.2f}")


# /// 28
# from math import log10, sin, cos
#
# a, x = map(float, input().split())
# BB1 = x * sin(x / 2 + x / 3 + x / 4) + (log10(x ** 2 - 2) + 3 ** a) / (cos(x + 3) * sin(x + 3) + 8)
# print(f"{BB1:.2f}")

# /// 29
# from math import cos,sin,e,pow,sqrt
# a,x,y=map(float,input().split())
# TT=sqrt(y**2+pow(e,x)+sqrt(pow(e,x)+a/(x**2+2))+(pow(cos(x),2)/sin(x**2)))+pow(cos(x),3)
# print(f"{TT:.2f}")

# /// 30
# from math import sqrt, sin, e
#
# x, y, z = map(float, input().split())
# AF = (2 ** (-x)) * sqrt(x + (abs(y) + 2) ** (1 / 4)) * (e ** (x - 1) / sin(z + 2) + 2) ** (1 / 3)
# print(f"{AF:.2f}")

# a,b,c=map(float,input().split())
# if a>b or a>c:
#     print("a katta")
# elif b>a or b>c:
#     print("b katta")
# else:
#     print("c katta")


# x,y=map(float,input().split())
# if x>y:
#     print(x,y)
# elif x<y:
#     print(y,x)
# else:
#     print(x,y)

# print("1 4 6 3 4 5 7 4"[2::4])


# /// 32
# x, y, z = map(float, input().split())
# maxi = x
# if maxi < y:
#     maxi = y
# if maxi < z:
#     maxi = z
# print(maxi)
# mini = x
# if mini > y:
#     mini = y
# if mini > z:
#     mini = z
# print(mini)

# /// 33
# x , y , z = map(float , input().split())
# print(f"{max(x + y + z , x , y , z):.2f} {min(x + y/2, x , y , z)**2:.2f}")

# /// 34
# a,b,c=map(float, input().split())
# if a<b<c:
#     print("YES")
# else:
#     print("NO")

# /// 35
# a, b, c = map(int, input().split())
# if c <= b and b <= a:
#     a *= 2
#     b *= 2
#     c *= 2
#     print(a, b, c)
# else:
#     a = abs(a)
#     b = abs(b)
#     c = abs(c)
#     print(a,b,c)

# /// 36
# a, b = map(int, input().split())
# if (a > b):
#     print(a)
# else:
#     print(a, b)

# /// 37
# a, b = map(int, input().split())
# if (a <= b):
#     a=0
#     print(a,b)
# else:
#     print(a,b)


# /// 38
# x, y, z = map(float,input().split())
# if (x >= 1 and x <= 3):
#     print(x)
# if (y >= 1 and y <= 3):
#     print(y)
# if (z >= 1 and z <= 3):
#     print(z)

# /// 39
# x , y = map(float , input().split())
# print(4*x*y , (x + y)/2) if x > y else print((x + y)/2 , 4*x*y)


# /// 40
# a = None , None , None
# x , y , z = map(int , input().split())
# print(x**2, end=' ') if x > 0 else print(x, end = ' '), print(y ** 2, end = ' ') if y > 0 else print(y, end = ' ') ,  print(z ** 2) if z > 0 else print(z)

# /// 41
# x , y , z = map(float , input().split())
# if x < 1 and y < 1 and z < 1:
#     mini = min(x , y , z)
#     if mini == x:
#         print((y + z) / 2 , y , z)
#     elif mini == y:
#         print(x , (x + z) / 2 , z)
#     else:
#         print(x, y, (x + y) / 2)
# else:
#     print(x , y , z)

# /// 42
# a,b,c,d=map(float , input().split())
# if a <= b <= c <= d:
#     a = d
#     b = d
#     c = d
#     print(a, b, c, d)
# else:
#     minn = a
#     if minn > b:
#         minn = b
#     if minn > c:
#         minn = c
#     if minn > d:
#         minn = d
#     print(minn, minn, minn, minn)

# // 43
# x, y = map(float, input().split())
# if y < 0 > x:
#     y=abs(y)
#     x=abs(x)
#
# if x < 0 < y or x > 0 > y:
#     x += 0.5
#     y += 0.5
# print(x,y)

# /// 44
# x, y, z = map(int, input().split())
# if x + y > z and x + z > y and y + z > x:
#     print("YES")
# else:
#     print("NO")


# /// 45
# from math import sqrt
#
# a, b, c = map(int, input().split())
# D = b ** 2 - 4 * a * c
#
# if D >= 0:
#     x1 = (-b + sqrt(D)) / (2 * a)
#     x2 = (-b - sqrt(D)) / (2 * a)
#     print(f"{x1:.2f} {x2:.2f}")
# else:
#     print('NO')


# massiv=(4,6,9,10)
# summ=0
# for i in massiv:
#     summ+=i
# print(summ)


# nums = map(int, input().split())
# summ = 0
# while i < len(nums):
#     if (not nums[i] & 1):
#         summ += nums[i]
#         if (nums[i] & 1):
#             summ -= nums[i]
# print(summ)


# n = int(input())
# S, i = 0, 1
# while i <= n:
#     S += 1 / i
#     i += 1
# print(S)


# /// 61
# from math import sin
#
# n = int(input())
# S, i = 0, 1
# while i <= n:
#     S += sin(i) / 2 ** i
#     i += 1
# print(f"{S:.2f}")

# /// 62
# from math import sin
#
# n = int(input())
# S, i = 0, 1
# while i <= n:
#     S += (-1) ** (i - 1) * sin(i ** i) / 2 ** i
#     i += 1
# print(f"{S:.2f}")

# /// 63
# from math import factorial
#
# n = int(input())
# S, i = 0, 1
# while i <= n:
#     S += (-1) ** (i - 1) * 1 / factorial(2 * i - 1)
#     i += 1
# print(f"{S:.4f}")

# /// 64
# n, x = map(int, input().split())
# S, i = 0, 1
# while i <= n:
#     S += (-1) ** (i - 1) * 1 / x ** (2 * i)
#     i += 1
# print(f"{S:.3f}")

# /// 65
# n, x = map(int, input().split())
# S, i = 0, 1
# while i <= n:
#     S += i / x ** (2 * i)
#     i += 1
# print(f"{S:.3f}")

# /// 66
# from math import sin
#
# n, x = map(int, input().split())
# S, i = 0, 1
# while i <= n:
#     S += (-1) ** (i - 1) * 1 / i * sin(i * x)
#     i += 1
# print(f"{S:.3f}")

# /// 67
# from math import sqrt
#
# n, x = map(int, input().split())
# S, i = 0, 1
# while i <= n:
#     S += x ** i / sqrt(i)
#     i += 1
# print(f"{S:.3f}")

# /// 68
# from math import factorial
#
# n, x = map(int, input().split())
# S, i = 0, 1
# while i <= n:
#     S += x ** i / factorial(i)
#     i += 1
# print(f"{S:.3f}")

# /// 69
# from math import factorial
#
# n, x = map(int, input().split())
# S, i = 0, 1
# while i <= n:
#     S += (-1) ** i * x ** i / factorial(i)
#     i += 1
# print(f"{S:.3f}")

# /// 70
# from math import factorial
#
# n, x = map(int, input().split())
# S, i = 0, 1
# while i <= n:
#     S += (-1) ** (i-1) * x ** (2*i-1) / factorial(2*i-1)
#     i += 1
# print(f"{S:.3f}")

# /// 71
# from math import factorial
#
# n, x = map(int, input().split())
# S, i = 0, 1
# while i <= n:
#     S += (-1) ** (i - 1) * x ** (2 * i - 2) / factorial(2 * i - 2)
#     i += 1
# print(f"{S:.3f}")

# /// 72
# from math import factorial
#
# n, x = map(int, input().split())
# S, i = 0, 1
# while i <= n:
#     S += x ** (2 * i - 2) / factorial(2 * i - 2)
#     i += 1
# print(f"{S:.3f}")

# /// 73
# n, x = map(int, input().split())
# S, i = 0, 1
# while i <= n:
#     S += x ** (2 * i - 1) / (2 * i - 1)
#     i += 1
# print(f"{S:.3f}")

# /// 74
# from math import factorial
#
# n, x = map(int, input().split())
# S, i = 0, 1
# while i <= n:
#     S += x ** (2 * i - 1) / factorial(2 * i - 1)
#     i += 1
# print(f"{S:.3f}")

# /// 75
# from math import factorial
#
# n, k = map(int, input().split())
# S, i = 0, 0
# while i <= n:
#     S += (((-1) ** i) * (k ** i)) / factorial(i)
#     i += 1
# print(f"{S:.3f}")

# /// 76
# from math import cos, sin, pow
#
# a, b, c = map(int, input().split())
# summ = 0
# for i in range(a, c + 1, 3):
#     summ += pow(((a * i + b) / (b ** 2 + (cos(i) * cos(i)))), 1 / 3) - sin(i ** 2) / (a * b)
# print(f"{summ:.2f}")

# /// 77
# from math import sin, pow, cos
#
# a, b, c, d = map(int, input().split())
# i = c
# y = 0
# while i <=d:
#     y += ((sin(a * i) + b ** (2 * c)) / (b ** 2 + pow(cos(i), 2))) ** (1 / 3) - sin(i ** 2) / (a * b)
#     i += 2
# print(f"{y:.2f}")

# /// 78
# a, b, c = map(int, input().split())
# y = 0
# for i in range(a, b + 1, 2):
#     y += (a ** b + b ** i + c ** a) / (2 * (i ** 2) + 3 * (a ** i))
# print(f"{y:.2f}")

# /// 79
# from math import cos, pi
#
# a = int(input())
# i = - (pi / 2)
# y = 0
# while i <= pi:
#     y += (a ** a) ** (1 / 3) + i ** 2 * cos(a * i)
#     i += (pi / 19)
# print(f"{y:.2f}")

# /// 80
# from math import cos, sin
#
# a = int(input())
# i = 0
# y = 0
# while i <= 10:
#     y += a * cos(i) - sin(i ** 2)
#     i += 0.5
# print(f"{y:.2f}")

# /// 81
# from math import cos, sin,pow
#
# a,b = map(int,input().split())
# i = 1
# y = 0
# while i <= 12:
#     y += a ** 2 + ((b + sin(i)) / (a ** 3 + pow(cos(i ** 3), 2))) ** (1 / 5)
#     i += 2
# print(f"{y:.2f}")

# /// 82
# a, b, c = map(int, input().split())
# i = 1
# y = 0
# while i <= 12:
#     y += (a * (i ** 2)) / b + i / c
#     i += 3
# print(f"{y:.2f}")

# /// 83
# a, b, c = map(int, input().split())
# i = 5
# y = 0
# while i <= 10:
#     y += (a ** 2 + b * i + i ** c) / (a ** 2 + b ** 2 + i ** 2)
#     i += 0.5
# print(f"{y:.2f}")


# /// 84
# from math import sin, pow, cos
#
# a, b, c = map(int, input().split())
# i = -1
# y = 0
# while i <= 1:
#     y += ((sin(a * i) + b ** c) / (b ** 2 + pow(cos(i), 2))) ** (1 / 3) - sin(i ** 2) / (a * b)
#     i += 0.25
# print(f"{y:.2f}")

# /// 85
# a, b, c = map(int, input().split())
# i = 1
# y = 0
# while i <= 20:
#     y += (a * (i ** 2) + b * i + c) / (a ** 2 + b ** 2 + i ** 2)
#     i += 5
# print(f"{y:.2f}")

# /// 86
# from math import sin, cos
#
# a, b, c = map(int, input().split())
# i = c
# y = 0
# while i <= b:
#     y += (a ** 2) * cos(i) + sin(i) / 2 + b * (i ** 2)
#     i += 0.25
# print(f"{y:.2f}")

# /// 87
# from math import sin, cos, pi, pow
#
# a = int(input())
# i = (-pi / 2)
# y = 0
# while i <= pi:
#     y += 2 * (pow(a, sin(2 * i))) ** (1 / 3) + i ** 2 * cos(a * i)
#     i += pi / 10
# print(f"{y:.2f}")

# /// 88
# from math import sin, cos, pow
#
# a, b, c, d = map(int, input().split())
# i = d
# y = 0
# while i <= c:
#     y += ((a * i + b) / (b ** 2 + pow(cos(i), 2))) ** (1 / 5) - sin(i ** 2) / (a * b)
#     i += 1.5
# print(f"{y:.2f}")

# 89
# from math import sin, cos, pow,sqrt
#
# a, b, c = map(int, input().split())
# i = 0
# y = 0
# while i <= 1:
#     y += sqrt((sin(a * i) + b ** c) / (b ** 2 + pow(cos(i), 2))) - sin(i ** 2) / (a * b)
#     i += 0.25
# print(f"{y:.2f}")

# /// 90
# from math import log, atan, pi, e, sin
#
# a, b, c = map(int, input().split())
# i = (-pi)
# y = 0
# while i <= pi:
#     y += ((log(a ** (2 * sin(i))) + e ** (2 * i)) / (atan(i) + b)) + c
#     i += pi / 10
# print(f"{y:.2f}")

# /// 91
# from math import log
#
# a, b, c, d = map(int, input().split())
# S, P, SP = 0, 1, 0
# m, k, i = 1, 1, 1
#
# while m <= a:
#     S += (3 * m ** 3 + 4 * m + 5) / (m ** 3 + log(m))
#     m += 1
# while k <= b:
#     P *= k / (k ** 3 + 7 * k + 5)
#     k += 1
#
# while i <= c:
#     sp = 1
#     m = 1
#     while m <= d:
#         sp *= (log(i) + m ** i) / m ** i
#         m += 1
#     SP += sp
#     i += 1
#
# print(f"{S:.2f} {P:.2f} {SP:.2f}")

# /// 92
# from math import cos, pow, log
#
# x, y, a, b = map(int, input().split())
# S, P, SP = 0, 1, 0
# a1, i, k = 1, 1, 1
#
# while a1 <= x:
#     S += (a1 ** 2 + 2 * a1) / (a1 ** 3 + a1 * pow(cos(a1), 2) + 1)
#     a1 += 1
#
# while i <= y:
#     P *= (i ** 2 + 1) / ((i ** 3) ** (1 / i) + 2)
#     i += 1
#
# i = 1
# while i <= a:
#     sp = 1
#     k = 1
#     while k <= b:
#         sp *= log((k ** i + k**(1/i)) / (k ** 3 + i ** (1 / k)))
#         k += 1
#     SP += sp
#     i += 1
# print(f"{S:.2f} {P:.2f} {SP:.2f}")


# /// 93
# from math import cos, sin,sqrt
#
# x, y, a, b = map(int, input().split())
# S, P, SP = 0, 1, 0
# k, n, i = 1, 1, 1
#
# while k <= x:
#     S += (k ** 2 + sin(k) + 5) / (k ** 7 + 1) ** (1 / 5)
#     k += 1
# while n <= y:
#     P *= (n + sqrt(n)) / (n - (n + 1) ** (1 / 5))
#     n += 1
#
# k = 1
# while k <= a:
#     sp = 1
#     i = 1
#     while i <= b:
#         sp *= (i ** 2 + k ** (2 / i)) / ((sin(i) + cos(k)) * (i ** k))
#         i += 1
#     SP += sp
#     k += 1
#
# print(f"{S:.2f} {P:.2f} {SP:.2f}")

# /// 94
# from math import cos, sqrt
#
# x, y, c, d = map(int, input().split())
# S, P, SP = 0, 1, 0
# a, k, y1 = 1, 1, 1
# while a <= x:
#     S += (2 * a + cos(a)) ** 2
#     a += 1
# a = 1
# while a <= y:
#     P *= (a + 6) / sqrt((a ** 2) + 2)
#     a += 1
# k = 1
# while k <= c:
#     sp = 0
#     y1 = 1
#     while y1 <= d:
#         sp += ((k ** 2) + y1) / sqrt((k ** 2) + (y1 ** 2))
#         y1 += 1
#     SP += sp
#     k += 1
# print(f"{S:.2f} {P:.2f} {SP:.2f}")

# /// 95
# from math import sqrt, e
#
# x, y, c, d = map(int, input().split())
# S, P, SP = 0, 0, 0
# i, k, m, n = 1, 1, 1, 1
# while i <= x:
#     S += (i ** 4 + i ** 2 + 3) / sqrt(i + e ** i)
#     i += 1
# while k <= y:
#     P += (k + 1) / (k ** 3 + 5 * k)
#     k += 1
# m = 1
# while m <= c:
#     sp = 1
#     n = 1
#     while n <= d:
#         sp *= sqrt(abs((m ** n) - (n ** m)) / ((m ** n) + (n ** m)))
#         n += 1
#     SP += sp
#     m += 1
# print(f"{S:.2f} {P:.2f} {SP:.2f}")
#

# /// 96
# from math import log
#
# x, y, c, d = map(int, input().split())
# S, P, SP = 0, 1, 1
# k, i, n, m = 1, 1, 1, 1
# while k <= x:
#     S += ((-1) ** k) * (k + 1) / (k ** 3 + k ** 2 + 1)
#     k += 1
# while i <= y:
#     P *= (i ** 3 + abs(i - 9)) /( log(i) + 7 * i)
#     i += 1
# n=1
# while n <= c:
#     sp = 0
#     m=1
#     while m <= d:
#         sp += ((-1) ** m) * ((log(m + 5)) / (m ** (n + 3) + n * m))
#         m += 1
#     SP *= sp
#     n += 1
# print(f"{S:.2f} {P:.2f} {SP:.2f}")

# /// 97
# from math import sqrt, e, sin
#
# x, y, c, d = map(int, input().split())
# S, P, SP = 0, 1, 0
# n, m, i, k = 1, 1, 1, 1
# while n <= x:
#     S += 1 / (5 - 17 * n + n ** 3)
#     n += 1
# while m <= y:
#     P *= sqrt(abs(m - 5) + 1) / (m ** 2 + 4 * m - 1)
#     m += 1
# i = 1
# while i <= c:
#     sp = 1
#     k = 1
#     while k <= d:
#         sp *= ((-1) ** (i)) * ((sin(k) + e ** k) ** (1 / 7) / (2 * abs(4 * (i ** 3) - (k ** 4))))
#         k += 1
#     SP += sp
#     i += 1
# print(f"{S:.2f} {P:.2f} {SP:.2f}")
# #
# /// 98
# from math import log, cos
#
# x, y, c, d = map(int, input().split())
# S, P, SP = 0, 1, 0
# a, k = 1, 1
# while a <= x:
#     S += (4 * a + 6 * log(a)) / (a ** 2 + a)
#     a += 1
# a = 1
# while a <= y:
#     P *= abs(a - 6 * cos(a)) / (a ** 2 + a ** log(a))
#     a += 1
# k = 1
# while k <= c:
#     sp = 1
#     a = 1
#     while a <= d:
#         sp *= (a * k + x) / (k ** 2 + y ** 2)
#         a += 1
#     SP += sp
#     k += 1
# print(f"{S:.2f} {P:.2f} {SP:.2f}")

# /// 99
# from math import e, sqrt
#
# x, y, c, d = map(int, input().split())
# S, P, SP = 0, 1, 0
# k, a, i, j = 1, 3, 1, 1
# while k <= x:
#     S += (k ** 3 + e ** k)
#     k += 1
# a=3
# while a <= y:
#     P *= (a * x) / sqrt(a ** 2 + x ** 2)
#     a += 1
# i = 1
# while i <= c:
#     sp = 1
#     j = 1
#     while j <= d:
#         sp *= (i * x + j ** 2) / sqrt(i ** 2 + j * y)
#         j += 1
#     SP += sp
#     i += 1
# print(f"{S:.2f} {P:.2f} {SP:.2f}")

# /// 100
from math import log, sqrt, sin

x, y, c, d = map(int, input().split())
S, P, SP = 0, 1, 1
a, i, j = 1, 1, 1,
while a <= x:
    S += (a*x+4)/sqrt(a+log(6))
    a += 1

a = 1
while a <= y:
    P *= (a*(x**2)+6)/sin(a*x)
    a += 1
i = 1
while i <= c:
    sp = 1
    j = 1
    while j <= d:
        sp *= (i*j+y*x)/sqrt((j*x+y)**i)
        j += 1
    SP *= sp
    i += 1
print(f"{S:.2f} {P:.2f} {SP:.2f}")


# def add(num1, num2):
#     summ = num1 + num2
#     return summ

# def test(a, b):
#     print(a ** b)
#
#
# test(2, 3)

# def test(num1):
#     summ=1
#     i=1
#     while i<=num1:
#       summ*=i
#       i+=1
#     return summ
# print(test(5))

# def reverse_words(word):
#     return word[::-1]
# print(reverse_words("hello"))

# def is_palindrome(word):
#     return word==word[::-1]
# print(is_palindrome("ikki"))
# print(is_palindrome("bir"))

# def is_palindrome(word):
#     str = "a, i, e, u, o"
#     return word
#
#
#
# print(is_palindrome("ikki"))
# print(is_palindrome("bir"))


# /// 165
# from math import sin
#
#
# def function(a, b, c):
#     f = (2 * a - b - sin(c)) / (5 + abs(c))
#     return f
#
#
# t,s = map(float, input().split())
# result = function(t, -2 * s, 1.17) + function(2.2, t, s - t)
#
# print(f"{result:.2f}")

# /// 166
# def function(a, b):
#     G = (a ** 2 + b ** 2) / (a ** 2 + 2 * a * b + 3 * b ** 2 + 4)
#     return G
#
#
# t, s = map(float, input().split())
# result = function(1.2, s) + function(t, s) + function(2 * s - 1, s * t)
# print(f"{result:.2f}")

# /// 168
# a, b, c = map(float, input().split())
# f=0
# f = (max(a, a + b) + max(a, b + c)) / (1 + max(a + b * c, 1.15))
# print(f"{f:.2f}")

# /// 169
# a, b = map(float, input().split())
# print(f"{(u := min(a, b)):.2f} {(v := min(a * b, max(a, b))):.2f} {min(u + v, 3.14)}")

# /// 170
# def function(a, b):
#     f = a / (b ** 2 + 1) + b / (a ** 2 + 1) - (a - b) ** 3
#     return f
#
#
# s, t = map(float, input().split())
# result = function(s, t) + max(function(s - t, s * t), function(s - t, s + t)) + function(1, 1)
#
# print(f"{result:.2f}")
#
# /// 171
# def ss(a, b) -> float:
#     i, s = 0, 0
#     while i < a:
#         s += b[i]
#         i += 1
#     return s
#
#
# n = int(input())
# x = list(map(int, input().split()))
# k, m = map(int, input().split())
# ans = (ss(m - k, x) + ss(k, x)) / ((ss(m, x) - ss(4, x)) ** 2)
# print(f"{ans: .2f}")

# /// 172
# n = int(input())
#
#
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n % 2 == 0:
#         return f(n // 2)
#     else:
#         return f(n // 2) + f(n // 2 + 1)
#
#
# result = f(n)
# print(result)

# def password_check(password):
#
#     if len(password) >= 8:
#
#         if any(char.islower() for char in password):
#
#             if any(char.isupper() for char in password):
#
#                 if any(char.isdigit() for char in password):
#                     return True
#     else:
#         return False
#
#
# test_password = len()
# result = password_check(test_password)
# print(result)

# s = input().split()


# def password_check(s):
#     if len(s) >= 8:
#         if (i.islower() for i in s):
#             if (i.isupper() for i in s):
#                 if (i.isdigit() for i in s):
#                     if (i.isalnum() for i in s):
#                         return True
#     else:
#         return False
#
#
# test_password = len()
# result = password_check(test_password)
# print(result)


# def password_check(password):
#
#     if len(password) >= 8:
#
#         if any(char.islower() for char in password):
#
#             if any(char.isupper() for char in password):
#
#                 if any(char.isdigit() for char in password):
#                     return True
#     else:
#         return False
#
#
# test_password = len()
# result = password_check(test_password)
# print(result)


from math import log,cos,e

a, x = map(int, input().split())
y =  e**x + a**x+cos(x)-log(a,x)