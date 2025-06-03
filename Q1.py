#Global Solution
#Alunas: Carolina Araujo RM562916 e Thais Cesario Souza RM562987
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