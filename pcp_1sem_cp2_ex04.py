def calcular_horas_extras(salario_base, horas):
    valor_hora_extra = salario_base*1.5/100
    valor_total_hora_extra = valor_hora_extra*horas
    return valor_total_hora_extra

def calcular_descontos_faltas(salario_base, faltas):
    valor_desconto_falta = salario_base*20/100
    valor_total_desconto_falta = valor_desconto_falta*faltas
    return valor_total_desconto_falta

def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == 'sim':
        if cargo == 'gerente':
            return 1000
        elif cargo == 'analista':
            return 500
        elif cargo == 'assistente':
            return 300
        elif cargo == 'estagiário':
            return 100
    if recebeu_bonus == 'não':
            return 0    

# Pede os dados do funcionário
nome = input("Digite o nome do funcionário: ")
salario_base = float(input("Digite o salário base do funcionário: "))
Cargo = input("Digite o cargo do funcionário (Gerente, Analista, Assistente, Estagiário): ")
cargo = Cargo.lower()
horas_extras = int(input("Digite o número de horas extras trabalhadas: "))
faltas = int(input("Digite o número de faltas do funcionário: "))
recebeu_bonus = input("O funcionário recebeu bônus? (Sim/Não): ")
recebeu_bonus = recebeu_bonus.lower()

# Calcula os acréscimos, descontos e salário final
total_de_acrescimos = calcular_horas_extras(salario_base, horas_extras) + calcular_bonus(cargo, recebeu_bonus)
total_de_descontos = calcular_descontos_faltas(salario_base, faltas)
salario_final = salario_base + total_de_acrescimos - total_de_descontos

# Exibe a folha de pagamento
print( );
print("============= Folha de Pagamento =============")
print(f"Funcionário: {nome}")
print(f"Salário bruto: R$ {salario_base:.2f}")
print(f"Total de acréscimos: R$ {total_de_acrescimos:.2f}")
print(f"Total de descontos: R$ {total_de_descontos:.2f}")
print(f"Salário final: R$ {salario_final:.2f}") 