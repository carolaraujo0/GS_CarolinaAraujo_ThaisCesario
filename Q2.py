print(f"\n Questão 2: armazenando as informações das listas {i + 1} ---")
    # Armazenar as informações nas listas
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

# 2. Armazenamento em Listas
# Já feito acima nas variáveis: tipos_desastres, paises, cidades, bairros, ruas, total_afetados,
# criancas, adultos, idosos, mobilidade_reduzida, feridos.


print(f"\n Questão 3: realizando a análise de dados {i + 1} ---")
# 3. Análise de Dados
# a. Exibir o total de desastres registrados
print(f"\nTotal de desastres registrados: {len(tipos_desastres)}")

# b. Calcular o total geral de pessoas afetadas
total_geral_afetados = sum(total_afetados)
print(f"Total geral de pessoas afetadas: {total_geral_afetados}")

# c. Calcular o total de pessoas em cada categoria
total_criancas = sum(criancas)
total_adultos = sum(adultos)
total_idosos = sum(idosos)
total_mobilidade_reduzida = sum(mobilidade_reduzida)
total_feridos = sum(feridos)

print("\nResumo de pessoas afetadas por categoria:")
print(
    f"Crianças: {total_criancas} | Adultos: {total_adultos} | Idosos: {total_idosos} | Mobilidade reduzida: {total_mobilidade_reduzida} | Feridos: {total_feridos}")

# d. Identificar qual categoria foi mais afetada
categorias = ["Crianças", "Adultos", "Idosos", "Mobilidade reduzida", "Feridos"]
valores_categorias = [total_criancas, total_adultos, total_idosos, total_mobilidade_reduzida, total_feridos]
categoria_mais_afetada = categorias[valores_categorias.index(max(valores_categorias))]

print(f"Categoria mais afetada: {categoria_mais_afetada}")

# e. Identificar o desastre com o maior número de afetados
maior_numero_afetados = max(total_afetados)
indice_maior_afetado = total_afetados.index(maior_numero_afetados)

# Exibir o local completo
local_maior_desastre = f"{ruas[indice_maior_afetado]}, {bairros[indice_maior_afetado]}, {cidades[indice_maior_afetado]}, {paises[indice_maior_afetado]}"
print(f"\nDesastre com maior número de afetados:")
print(f"Tipo: {tipos_desastres[indice_maior_afetado]}")
print(f"Local: {local_maior_desastre}")