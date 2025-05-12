
### Declaração de Funções

# Função que realiza o depósito solicitado
def depositar():

    global saldo
    global extrato

    deposito = float(input("\nDigite o valor a ser depositado: R$ "))
    
    # verifica se o usuário não digitou 0 ou um valor negativo
    if deposito <= 0: 
        print("\nDepósito inválido. Por gentileza digite valores positivos.") 

    else: 
        saldo += deposito #acrescenta o valor do depósito no saldo
        extrato += f"+ R$ {deposito:.2f}\n" #adiciona uma linha no histórico do extrato
        print(f"\nDepósito de R$ {deposito:.2f} realizado com sucesso! \nSaldo atual: R$ {saldo:.2f}.")
    
    return saldo, extrato



# Função para verificar se pode ser realizado o saque
def verifica_saque(valor_saque_solicitado):
    
    global numero_saques

    # Verifica se o usuário digitou um valor negativo ou 0
    if valor_saque_solicitado <= 0 or valor_saque_solicitado > saldo:
        print("\nPor gentileza, verifique o valor inserido e tente novamente.")
        return False
    
    # Verifica se o usuário solicitou um saque maior que R$500 (limite definido nas variáveis globais)
    elif valor_saque_solicitado > LIMITE_VALOR_SAQUE:
        print(f"\nSaque solicitado ultrapassa o limite de R$ {LIMITE_VALOR_SAQUE:.2f}")
        return False

    else:
        
        numero_saques += 1

        # verifica se o numero de saques ainda é menor que o limite permitido nas variáveis globais
        if numero_saques < LIMITE_SAQUES_DIARIOS:
            return True
        
        # verifica se o numero de saque atingiu o limite e alerta o usuário
        elif numero_saques == LIMITE_SAQUES_DIARIOS:
            print("\nLimite de 3 saques diários atingido! Para novos saques, por gentileza aguarde até amanhã")
            return True
        
        # não permite o saque por ultrapassar o limite diário de saques
        elif numero_saques > LIMITE_SAQUES_DIARIOS:
            print("\nLimite de saques diários atingido! Por gentileza tente novamente amanhã")
            return False



# Função que realiza o saque
def sacar():

    global saldo
    global extrato

    saque = float(input("\nDigite o valor a ser sacado: R$ "))

    # não permite o saque após retorno False da função verifica_saque()
    if verifica_saque(saque) == False:
        print("Operação Recusada!")
    
    # permite o saque após return True da função verifica_saque()
    else: 
        saldo -= saque # retira o valor solicitado do saldo total
        extrato += f"- R$ {saque:.2f}\n" #acrescenta uma linha no histórico do extrato
        print(f"\nSaque de R$ {saque:.2f} realizado com sucesso! \nSaldo atual: R$ {saldo:.2f}.")

    return saldo, extrato


# Função para exibir o extrato
def exibir_extrato():
        

        print()
        print(" Extrato ".center(40,"="))
        print()
        print(extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")


## Variáveis Globais

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



### Execução do programa com looping infinito
while True:

    opcao = input(menu).lower()

    if opcao == "d":
        depositar() 

    elif opcao == "s":
        sacar() 

    elif opcao == "e":
        exibir_extrato() 

    elif opcao == "q":
        print("\nEncerrando...") 
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")

    