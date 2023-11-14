x = int(input())
segundos = 0
minutos = 0
horas = 0
i = 0
while i < x:
  segundos += 1
  if segundos == 60:
    minutos += 1
    segundos = 0
    if minutos == 60:
      horas += 1
      minutos = 0
  i += 1

print(f"{horas}:{minutos}:{segundos}")