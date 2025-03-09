saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3
usuarios = []
numero_conta = 1
contas_correntes = {}

def criar_usuario():
    global numero_conta

    cpf = input("Informe o CPF (somente números): ")

    # Verificar se CPF já existe na lista de usuários
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Usuário já cadastrado!")
            return

    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    logradouro = input("Informe o endereço (Rua, número - Bairro - Cidade/Estado): ")

    conta = f"{numero_conta:04d}"  # Formata o número da conta (0001, 0002, etc.)

    novo_usuario = {
        "nome": nome,
        "data de nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": logradouro,
        "conta": conta
    }

    usuarios.append(novo_usuario)

    # Criar uma conta corrente associada ao usuário
    contas_correntes[conta] = {
        "saldo": 0.0,
        "extrato": "",
        "numero_saques": 0
    }

    print(f"Usuário cadastrado com sucesso! Número da conta: {conta}")
    
    numero_conta += 1  # Incrementa para a próxima conta ser 0002, 0003, etc.


def sacar():
    conta = input("Informe o número da sua conta: ")
    
    if conta not in contas_correntes:
        print("Conta não encontrada!")
        return

    conta_corrente = contas_correntes[conta]
    
    valor = float(input("Informe o valor do saque (limite R$500): "))

    if valor > conta_corrente["saldo"]:
        print("Erro! Saldo insuficiente.")
    elif valor > 500:
        print("Seu saque ultrapassa o limite de R$500.")
    elif conta_corrente["numero_saques"] >= 3:
        print("Tentativa de saque diário excedida, volte amanhã.")
    elif valor > 0:
        conta_corrente["saldo"] -= valor
        conta_corrente["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta_corrente["numero_saques"] += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Falha! Operação inválida.")


def deposito():
    conta = input("Informe o número da sua conta: ")

    if conta not in contas_correntes:
        print("Conta não encontrada!")
        return

    conta_corrente = contas_correntes[conta]

    valor = float(input("Informe o valor do depósito: "))

    if valor <= 0:
        print("Valor inválido! O depósito deve ser positivo.")
    else:
        conta_corrente["saldo"] += valor
        conta_corrente["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")


def ver_extrato():
    conta = input("Informe o número da sua conta: ")

    if conta not in contas_correntes:
        print("Conta não encontrada!")
        return

    conta_corrente = contas_correntes[conta]

    print("\n==================== EXTRATO =====================")
    if not conta_corrente["extrato"]:
        print("Não há movimentação registrada.")
    else:
        print(conta_corrente["extrato"])
    print(f"Saldo atual: R$ {conta_corrente['saldo']:.2f}")
    print("==================================================\n")


def listar_contas():
    if not usuarios:
        print("Nenhum usuário cadastrado! Cadastre um usuário primeiro.")
        return

    print("\n===== Lista de Contas Correntes =====")
    for usuario in usuarios:
        conta = usuario["conta"]
        print(f"Conta: {conta} | Nome: {usuario['nome']} | CPF: {usuario['cpf']} | Saldo: R$ {contas_correntes[conta]['saldo']:.2f}")
    print("=====================================\n")


menu = """

###### MENU ######

[u] Criar Usuário
[d] Depositar
[s] Sacar
[e] Extrato
[c] Listar Contas
[q] Sair

-> """

while True:
    opcao = input(menu).lower()

    if opcao == 'u':
        criar_usuario()
    elif opcao == 'd':
        deposito()
    elif opcao == 's':
        sacar()
    elif opcao == 'e':
        ver_extrato()
    elif opcao == 'c':
        listar_contas()
    elif opcao == 'q':
        print("Obrigado por usar nosso sistema! Saindo...")
        break
    else:
        print("Selecione uma opção válida!")       

        
            

        



            


        



