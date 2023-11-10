import math

x1, y1 = [float(x) for x in input().split(' ')]
x2, y2 = [float(x) for x in input().split(' ')]

x = math.pow(x2 - x1, 2)
y = math.pow(y2 - y1, 2)

distancia = math.sqrt(x + y)

print(f"distancia:.4f")