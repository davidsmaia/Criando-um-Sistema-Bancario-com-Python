menu = """

=======================================

Selecione a operação desejada: 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = ""
numero_saques = 0

LIMITE_VALOR_SAQUE = 500
LIMITE_SAQUES_DIARIOS = 3


while True:

    opcao = input(menu).lower()

    if opcao == "d":
        deposito = float(input("\nDigite o valor a ser depositado: R$ "))

        if deposito <= 0:
            print("\nDepósito inválido. Por gentileza digite valores positivos.") 
        
        else:
            saldo += deposito
            extrato += f"+ R$ {deposito:.2f}\n" # adiciona uma linha no histórico do extrato
            print(f"\nDepósito de R$ {deposito:.2f} realizado com sucesso!")

        
    elif opcao == "s":
        saque = float(input("\nDigite o valor a ser sacado: R$ "))

        if LIMITE_SAQUES_DIARIOS <= 0:
            print("Operação Recusada! Limite de número de saques diário atingido") 

        elif saque <= 0:
            print("\nOperação Recusada! Por gentileza, verifique o valor inserido e tente novamente.")
        
        elif saque > saldo:
            print("\nOperação Recusada! Não há saldo suficiente disponível.")
        
        elif saque > LIMITE_VALOR_SAQUE:
            print("\nOperação Recusada! Saque solicitado ultrapassa o limite permitido.")

        else:
            LIMITE_SAQUES_DIARIOS -= 1
            saldo -= saque
            extrato += f"- R$ {saque:.2f}\n"
            print(f"\nSaque de R$ {saque:.2f} realizado com sucesso!")
        

    elif opcao == "e":
        
        print("\n"," Extrato ".center(40,"="), "\n")
        print(extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
    
    elif opcao == "q":
        print("\nEncerrando...") 
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")

    