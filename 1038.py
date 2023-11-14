item, quant = [float(x) for x in input().split(' ')]

def lanche(item, quant):
  if item == 1: return quant * 4.0
  if item == 2: return quant * 4.5
  if item == 3: return quant * 5.0
  if item == 4: return quant * 2.0
  if item == 5: return quant * 1.5

print(f"Total: R$ {lanche(item, quant):.2f}")