#Global Solutuon
# Alunas: Carolina Araujo RM562916 e Thais Cesario Souza RM562987

print("\n Questão 2 ")
for i in range(len(tipos_desastres)):
    print(f"\nDesastre {i + 1}:")
    print(f"Tipo: {tipos_desastres[i]}")
    print(f"Local: {ruas[i]}, {bairros[i]}, {cidades[i]}, {paises[i]}")
    print(f"Pessoas afetadas: {total_afetados[i]}")
    print(f" - Crianças: {criancas[i]}")
    print(f" - Adultos: {adultos[i]}")
    print(f" - Idosos: {idosos[i]}")
    print(f" - Mobilidade reduzida: {mobilidade_reduzida[i]}")
    print(f" - Feridos: {feridos[i]}")


