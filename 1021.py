x = float(input())
x = x * 100

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]
print("NOTAS:")
for i in notas:
  print(f"{int(x // i)} nota(s) de R$ {(i/100):.2f}")
  x %= i

print('MOEDAS:')
for j in moedas:
  print(f"{int(x // j)} moeda(s) de R$ {(j/100):.2f}")
  x %= j
