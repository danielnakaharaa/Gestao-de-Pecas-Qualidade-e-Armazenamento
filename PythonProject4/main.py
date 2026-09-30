import json

CAPACIDADE_CAIXA = 10

def carregar_arquivo(arquivo):
    with open(arquivo, "r", encoding="utf-8") as banco:
        return json.load(banco)

def salvar_arquivo(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as banco:
        json.dump(dados, banco, ensure_ascii=False, indent=4)

def ver_caixa():
    caixas = carregar_arquivo("banco.json")
    for i, caixa in enumerate(caixas, start=1):
        print(f"\nCAIXA {i}")
        for produto in caixa:
            print(produto)

def pegar_id_aprovado():
    caixas = carregar_arquivo("banco.json")
    maior_id = 0

    for caixa in caixas:
        for produto in caixa:
            if produto["id"] > maior_id:
                maior_id = produto["id"]

    return maior_id + 1

def pegar_id_reprovado():
    produtos = carregar_arquivo("bancoReprovado.json")
    maior_id = 0

    for produto in produtos:
        if produto["id"] > maior_id:
            maior_id = produto["id"]

    return maior_id + 1

def verdadeiro(peso, cor, comprimento):
    caixas = carregar_arquivo("banco.json")

    if caixas == []:
        caixas.append([])

    caixa_atual = caixas[-1]

    if len(caixa_atual) >= CAPACIDADE_CAIXA:
        caixas.append([])
        caixa_atual = caixas[-1]

    id_produto = pegar_id_aprovado()

    produto = {
        "id": id_produto,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento
    }

    caixa_atual.append(produto)

    print("PEÇA APROVADA!")

    if len(caixa_atual) == CAPACIDADE_CAIXA:
        print("CAIXA CHEIA!")

    salvar_arquivo("banco.json", caixas)

def falso(peso, cor, comprimento):
    produtos = carregar_arquivo("bancoReprovado.json")

    id_produto = pegar_id_reprovado()

    produto = {
        "id": id_produto,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento
    }

    produtos.append(produto)

    print("PEÇA REPROVADA!")

    salvar_arquivo("bancoReprovado.json", produtos)

def cadastrar_peca():
    peso = float(input("Digite o seu peso: "))
    cor = input("Digite a sua cor: ").lower()
    comprimento = float(input("Digite o seu comprimento: "))

    if (
        peso >= 95
        and peso <= 105
        and (cor == "azul" or cor == "verde")
        and comprimento >= 10
        and comprimento <= 20
    ):
        verdadeiro(peso, cor, comprimento)
    else:
        falso(peso, cor, comprimento)

def listar_pecas():
    caixas = carregar_arquivo("banco.json")
    produtos = carregar_arquivo("bancoReprovado.json")

    print("\nPEÇAS APROVADAS")

    for i, caixa in enumerate(caixas, start=1):
        for produto in caixa:
            print(f"ID: {produto['id']} | Peso: {produto['peso']} | Cor: {produto['cor']} | Comprimento: {produto['comprimento']} | Caixa: {i}")

    print("\nPEÇAS REPROVADAS")

    for produto in produtos:
        print(f"ID: {produto['id']} | Peso: {produto['peso']} | Cor: {produto['cor']} | Comprimento: {produto['comprimento']}")

def remover_peca(tipo, numero):
    if tipo == "1":
        caixas = carregar_arquivo("banco.json")

        for caixa in caixas:
            for produto in caixa:
                if produto["id"] == numero:
                    caixa.remove(produto)
                    salvar_arquivo("banco.json", caixas)
                    print("Peça aprovada removida com sucesso.")
                    return

        print("Peça não encontrada.")

    elif tipo == "2":
        produtos = carregar_arquivo("bancoReprovado.json")

        for produto in produtos:
            if produto["id"] == numero:
                produtos.remove(produto)
                salvar_arquivo("bancoReprovado.json", produtos)
                print("Peça reprovada removida com sucesso.")
                return

        print("Peça não encontrada.")

    else:
        print("Opção inválida.")

def listar_caixas_fechadas():
    caixas = carregar_arquivo("banco.json")

    print("\nCAIXAS FECHADAS")

    encontrou = False

    for i, caixa in enumerate(caixas, start=1):
        if len(caixa) == CAPACIDADE_CAIXA:
            encontrou = True
            print(f"\nCAIXA {i}")

            for produto in caixa:
                print(produto)

    if not encontrou:
        print("Nenhuma caixa fechada.")

def relatorio_final():
    caixas = carregar_arquivo("banco.json")
    reprovados = carregar_arquivo("bancoReprovado.json")

    quantidade_aprovadas = 0
    quantidade_reprovadas = len(reprovados)
    quantidade_caixas_fechadas = 0

    for caixa in caixas:
        quantidade_aprovadas += len(caixa)

        if len(caixa) == CAPACIDADE_CAIXA:
            quantidade_caixas_fechadas += 1

    total_pecas = quantidade_aprovadas + quantidade_reprovadas

    print("\nRELATÓRIO FINAL")
    print(f"Peças aprovadas: {quantidade_aprovadas}")
    print(f"Peças reprovadas: {quantidade_reprovadas}")
    print(f"Total de peças: {total_pecas}")
    print(f"Caixas fechadas: {quantidade_caixas_fechadas}")

boleano = True

while boleano:
    print("")
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("6. Sair")

    opcao = input("Digite a opcao: ")

    if opcao == "1":
        cadastrar_peca()
    elif opcao == "2":
        listar_pecas()
    elif opcao == "3":
        tipo = input("Digite 1 para aprovada ou 2 para reprovada: ")
        numero = int(input("Digite o ID da peça que deseja remover: "))
        remover_peca(tipo, numero)
    elif opcao == "4":
        listar_caixas_fechadas()
    elif opcao == "5":
        relatorio_final()
    elif opcao == "6":
        boleano = False
    else:
        print("### Digite uma opcao valida! ###")