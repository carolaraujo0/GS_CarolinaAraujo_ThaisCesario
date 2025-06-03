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