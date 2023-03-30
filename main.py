#Sistema de Supermercado

#Inicializar a lista de cliente

clientes = ["Alexandre", "Rodrigo", "Eduardo"]
print("Sistema de Supermercado")
opção = 0
while(opção!=5):
    print("Sistema do Supermercado")
    print("1 - Listar Clientes")
    print("2 - Cadastrar Clientes")
    print("3 - Remover Cliente")
    print("4 - Alterar Cliente")
    print("5 - Sair")
    opção = int(input("Escolha a opção: "))
    if(opção==1):
        print("Você escolheu opção 1 - Listar Clientes")
        for i in clientes:
            print(i)
    elif(opção==2):
        print("Você escolheu opção 2 - Cadastrar Clientes")
        nome = input("Digite o nome do novo cliente: ")
        clientes.append(nome)
    elif(opção==3):
        print("Você escolheu opção 3 - Remover Cliente")
    elif(opção==4):
        print("Você escolheu opção 4 - Alterar Cliente")
    elif(opção==5):
        print("Você escolheu opção 5 - Sair")
    else:
        print("Opção Inválida")