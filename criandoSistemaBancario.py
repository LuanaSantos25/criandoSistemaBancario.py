saldo = 0
saque = 500
extrato = ""
limiteSaque = 3
numero_saques = 0

print("bem vindo, escolha uma opção para iniciar [1]-saque, [2]-deposito, [3]-extrato, [4]-Sair")

while True:
    opcao = int(input())
    if opcao == 1: 
        print("Você escolheu a operação de saque")
        valor = int(input("Digite o valor que deseja sacar: "))
        excedeu_saque = numero_saques >= limiteSaque
        excedeu_limite = valor > limiteSaque
        excedeu_saldo = valor > saldo 

        if excedeu_saque:
            print("Você excedeu o número de saques")
        elif excedeu_limite:
            print("Valor excedeu o limite")
        elif excedeu_saldo:
            print("Saldo insuficiente")
        else:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R${valor:.2f}\n"

    elif opcao == 2:
        print("Você escolheu a operação de depósito")
        valor_deposito = int(input("Digite o valor para depósito: "))
            
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
        else:
            print("Opção inválida, digite uma opção válida")
    elif opcao == 3:
        print("Extrato bancário")
        print(f"Saldo: R${saldo:.2f}")
        print("Transações:")
        print(extrato)
    elif opcao == 4:
        break