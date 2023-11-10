x = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]
print(x)

for i in notas:
  y = int(x / i)
  print(f"{y} nota(s) de R$ {i},00")
  x = x % i
