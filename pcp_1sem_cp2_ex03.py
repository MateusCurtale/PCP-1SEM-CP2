cp1 = float(input("Nota do Checkpoint 1: "))
cp2 = float(input("Nota do Checkpoint 2: "))
cp3 = float(input("Nota do Checkpoint 3: "))
sp1 = float(input("Nota da Sprint 1: "))
sp2 = float(input("Nota da Sprint 2: "))
gs = float(input("Nota da Global Solution: "))

# Encontrar e remover a menor nota dos checkpoints
menor_cp = min(cp1, cp2, cp3)
soma_cp = cp1 + cp2 + cp3 - menor_cp  # soma das duas maiores

# Média parcial (2 maiores CPs + 2 Sprints)
media_parcial = (soma_cp + sp1 + sp2) / 4

# Média final
media = (media_parcial * 0.4) + (gs * 0.6)

# Média com peso do semestre
media_peso = media * 0.4

# Saída
print(f"\nMenor checkpoint desconsiderado: {menor_cp:.2f}")
print(f"Média parcial: {media_parcial:.2f}")
print(f"Média final: {media:.2f}")
print(f"Média com peso (40%): {media_peso:.2f}")