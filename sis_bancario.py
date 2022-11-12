menu = """   

[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

= > """

saldo = 0
limite = 500
extrato = ""
numero_depositos = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

# 1 - Operação de Deposito
    if opcao == "1":
        valor_deposito = float(input("Informe o valor do Depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            numero_depositos += 1
            extrato += f"Deposito: R$ {valor_deposito:.2f}\n"
            print("Depósito Realizado com Sucesso!")
        else:
            print("Valor Inválido!")

# 2 - Operação de Saque
    elif opcao == "2":
        valor_saque = float(input("Informe o valor a ser sacado: "))

        if valor_saque > saldo:
            print("Saldo Insuficiente!")

        elif valor_saque > limite:
            print("o valor do saque excede o limite!")

        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saque diário excedido!")

        elif valor_saque > 0:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
        else:
            print("Valor Inválido!")


# 3 - Opção de Extrato
    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        if numero_depositos == 0 and numero_saques == 0:
            print("Conta sem movimentação!")
        else:
            print(extrato)
            print(f"Saldo: R${saldo:.2F}")
        print("\n==============================")

# 0 - Opção para sair
    elif opcao == "0":
        break
    else:
        print("Opção Inválida!")
