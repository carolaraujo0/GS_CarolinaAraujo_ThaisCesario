print(f"\n Questão 1 {i + 1} ---")
# 1. Entrada de Dados
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

# Solicitar a quantidade de desastres
num_desastres = int(input("Insira a quantidade de desastres: "))

# Coleta de dados para cada desastre
for i in range(num_desastres):
    print(f"\n--- Desastre {i + 1} ---")
    tipo_desastre = input("Tipo de desastre: ")
    pais = input("País: ")
    cidade = input("Cidade: ")
    bairro = input("Bairro: ")
    rua = input("Rua: ")
    pessoas_afetadas = int(input("Total de pessoas afetadas: "))

    # Coletando dados de cada categoria
    num_criancas = int(input("Número de crianças: "))
    num_adultos = int(input("Número de adultos: "))
    num_idosos = int(input("Número de idosos: "))
    num_mobilidade_reduzida = int(input("Número de pessoas com mobilidade reduzida: "))
    num_feridos = int(input("Número de feridos: "))

    # Verificar se a soma das categorias é igual ao total de pessoas afetadas
    while (num_criancas + num_adultos + num_idosos + num_mobilidade_reduzida + num_feridos) != pessoas_afetadas:
        print("Erro! A soma das categorias não corresponde ao total de pessoas afetadas.")
        num_criancas = int(input("Número de crianças: "))
        num_adultos = int(input("Número de adultos: "))
        num_idosos = int(input("Número de idosos: "))
        num_mobilidade_reduzida = int(input("Número de pessoas com mobilidade reduzida: "))
        num_feridos = int(input("Número de feridos: "))


