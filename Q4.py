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