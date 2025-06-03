# Global Solution
# Alunas: Carolina Araujo RM562916 e Thais Cesario Souza RM562987

print("\nQuestão 1")

tipos_desastres = []
paises = []
cidades = []
bairros = []
ruas = []
total_afetados = []
criancas = []
adultos = []
idosos = []
mobilidade_reduzida = []
feridos = []

num_desastres = int(input("Insira a quantidade de desastres: "))

for i in range(num_desastres):
    print(f"\n--- Desastre {i + 1} ---")
    tipo_desastre = input("Tipo de desastre: ")
    pais = input("País: ")
    cidade = input("Cidade: ")
    bairro = input("Bairro: ")
    rua = input("Rua: ")
    pessoas_afetadas = int(input("Total de pessoas afetadas: "))

    num_criancas = int(input("Número de crianças: "))
    num_adultos = int(input("Número de adultos: "))
    num_idosos = int(input("Número de idosos: "))
    num_mobilidade_reduzida = int(input("Número de pessoas com mobilidade reduzida: "))
    num_feridos = int(input("Número de feridos: "))

    while (num_criancas + num_adultos + num_idosos + num_mobilidade_reduzida + num_feridos) != pessoas_afetadas:
        print("Erro! A soma das categorias não corresponde ao total de pessoas afetadas.")
        num_criancas = int(input("Número de crianças: "))
        num_adultos = int(input("Número de adultos: "))
        num_idosos = int(input("Número de idosos: "))
        num_mobilidade_reduzida = int(input("Número de pessoas com mobilidade reduzida: "))
        num_feridos = int(input("Número de feridos: "))

    tipos_desastres.append(tipo_desastre)
    paises.append(pais)
    cidades.append(cidade)
    bairros.append(bairro)
    ruas.append(rua)
    total_afetados.append(pessoas_afetadas)
    criancas.append(num_criancas)
    adultos.append(num_adultos)
    idosos.append(num_idosos)
    mobilidade_reduzida.append(num_mobilidade_reduzida)
    feridos.append(num_feridos)

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

print(f"\n Questão 3 ")
print(f"\na) Total de desastres registrados: {len(tipos_desastres)}")


total_geral_afetados = sum(total_afetados)
print(f"b) Total geral de pessoas afetadas: {total_geral_afetados}")


total_criancas = sum(criancas)
total_adultos = sum(adultos)
total_idosos = sum(idosos)
total_mobilidade_reduzida = sum(mobilidade_reduzida)
total_feridos = sum(feridos)

print("c) Resumo de pessoas afetadas por categoria:")
print(f"Crianças: {total_criancas} | Adultos: {total_adultos} | Idosos: {total_idosos} | Mobilidade reduzida: {total_mobilidade_reduzida} | Feridos: {total_feridos}")

categorias = ["Crianças", "Adultos", "Idosos", "Mobilidade reduzida", "Feridos"]
valores_categorias = [total_criancas, total_adultos, total_idosos, total_mobilidade_reduzida, total_feridos]
categoria_mais_afetada = categorias[valores_categorias.index(max(valores_categorias))]

print(f"d) Categoria mais afetada: {categoria_mais_afetada}")


maior_numero_afetados = max(total_afetados)
indice_maior_afetado = total_afetados.index(maior_numero_afetados)

local_maior_desastre = f"{ruas[indice_maior_afetado]}, {bairros[indice_maior_afetado]}, {cidades[indice_maior_afetado]}, {paises[indice_maior_afetado]}"
print(f"e) Desastre com maior número de afetados:")
print(f"Tipo: {tipos_desastres[indice_maior_afetado]}")
print(f"Local: {local_maior_desastre}")

print("\nQuestão 4: RELATÓRIO FINAL DE RESULTADOS")

print(f"\nQuantidade total de desastres registrados: {len(tipos_desastres)}")

print("Total de pessoas afetadas em cada categoria:")
print(
    f"Crianças: {total_criancas} | Adultos: {total_adultos} | "
    f"Idosos: {total_idosos} | Mobilidade reduzida: {total_mobilidade_reduzida} | Feridos: {total_feridos}"
)

print(f"\nCategoria mais afetada: {categoria_mais_afetada}")
print(f"Total geral de pessoas afetadas: {total_geral_afetados}")

print("\nLocal do desastre mais grave (maior número de vítimas):")
print(f"Tipo: {tipos_desastres[indice_maior_afetado]}")
print(f"Local: {local_maior_desastre}")
