def pode_aprovar(idade, renda, valor):
    if idade > 18 and valor <= renda * 20:
        return True
    return False

def definir_taxa(parcelas):
    if 3 <= parcelas <= 6:
        return 0.05
    elif 7 <= parcelas <= 12:
        return 0.08
    elif 13 <= parcelas <= 24:
        return 0.10
    else:
        return None


def calcular_parcela(valor, taxa, parcelas):
    i = taxa
    n = parcelas
    pmt = valor * (i * (1 + i) * n) / ((1 + i) * n - 1)
    return pmt


def calcular_total(parcela, parcelas):
    total = parcela * parcelas
    return total


def calcular_juros(total, valor):
    return total - valor


# ================= PROGRAMA PRINCIPAL =================

nome = input("Digite o nome do cliente: ")
idade = int(input("Digite a idade: "))
renda = float(input("Digite a renda mensal: "))
valor = float(input("Digite o valor do empréstimo: "))
parcelas = int(input("Digite o número de parcelas (3 a 24): "))

if not pode_aprovar(idade, renda, valor):
    print("\nEmpréstimo NEGADO.")
else:
    taxa = definir_taxa(parcelas)

    if taxa is None:
        print("\nNúmero de parcelas inválido.")
    else:
        parcela = calcular_parcela(valor, taxa, parcelas)
        total = calcular_total(parcela, parcelas)
        juros = calcular_juros(total, valor)

        print("\n===== EMPRÉSTIMO APROVADO =====")
        print(f"Cliente: {nome}")
        print(f"Valor financiado: R$ {valor:.2f}")
        print(f"Taxa de juros: {taxa*100:.0f}% ao mês")
        print(f"Valor da parcela: R$ {parcela:.2f}")
        print(f"Total pago: R$ {total:.2f}")
        print(f"Total de juros: R$ {juros:.2f}")