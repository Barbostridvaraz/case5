import math
 
print("Введите координаты точки: ")
x = float(input("x = "))
y = float(input("y = "))
print("Введите центр окружности и его радиус: ")
r = float(input("R = "))
xk = float(input("x(k) = "))
yk = float(input("y(k) = "))
 
 
if (x - xk)**2 / r**2 + (y - yk)**2 / r**2 < 1:
    print("Точка принадлежит кругу")
elif (x - xk)**2 / r**2 + (y - yk)**2 / r**2 == 1:
    print("Точка лежит на круге")
else:
    print("Точка не принадлежит кругу")