menu_opcoes = ""
while menu_opcoes != "sair":
    print("1. Novo Salario")
    print("2. Ferias")
    print("3. Decimo Terceiro")
    print("4. Sair")

    menu_opcoes = input("\nDigite a opcao desejada: ")
    if menu_opcoes == "Novo Salario":
        salario = float(input("Digite seu salario: R$ "))
        if salario <= 350:
            salario_novo = salario * 1.15
            print(f"Seu novo salario e R$ {salario_novo} ")
        elif salario >= 600:
            salario_novo = salario * 1.1
            print(f"Seu novo salario e R$ {salario_novo} ")
        else:
            salario_novo = salario * 1.05
            print(f"Seu novo salario e R$ {salario_novo} ")

    elif menu_opcoes == "Ferias":
        salario = float(input("Digite seu salario: R$ "))
        ferias = salario * 1.5
        print(f"salario_apos_acrescimo: R$ {ferias}")

    elif menu_opcoes == "Decimo terceiro":
        salario = float(input("Digite seu salario: R$ "))
        meses_trabalhados = float(input("Digite a quntidade de meses que voce trabalhou neste ano: "))
        Decimo_parcial = salario / 12
        Decimo = Decimo_parcial * meses_trabalhados
        print(f"O valor do seu decimo terceiro sera de R$ {Decimo}")
        

    else:
        menu_opcoes = "sair"
