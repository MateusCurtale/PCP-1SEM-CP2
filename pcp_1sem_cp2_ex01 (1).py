cod = int(input('Insira o número do estado de origem: '))
if cod < 1 or cod > 5:
    print('Esse não é um número válido.')

peso = float(input('Insira o peso do caminhão(em toneladas): '))

cod_carga = int(input('Insira o código da carga: '))
if cod_carga > 40 or cod_carga < 10:
    print('Esse não é um número válido.')

if cod == 1:
    imposto = 35
elif cod == 2:
    imposto = 25
elif cod == 3:
    imposto = 15
elif cod == 4:
    imposto = 5
else:
    imposto = 0

if 10 <= cod_carga <= 20:
    preco = 100
elif 21 <= cod_carga <= 30:
    preco = 250
elif 31 <= cod_carga <= 40:
    preco = 340
else:
    print("Código inválido")
    exit()


peso_kg = peso * 1000
preco_carga = peso_kg * preco
valor_imposto = preco_carga * (imposto / 100)
valor_total = valor_imposto + preco_carga

print(f'O peso em kg: {peso_kg:.2f} kg')
print (f'Preço da carga: R${preco_carga:.2f}')
print(f'Valor do imposto: R${valor_imposto:.2f}')
print(f'O valor total é de: R${valor_total:.2f}')