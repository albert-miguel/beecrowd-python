values = input().split(' ')
codigoX = int(values[0])
quantidadeX = int(values[1])
valorX = float(values[2])

values = input().split(' ')
codigoY = int(values[0])
quantidadeY = int(values[1])
valorY = float(values[2])

total = quantidadeX * valorX + quantidadeY * valorY

print(f'VALOR A PAGAR: R$ {total:.2f}')a