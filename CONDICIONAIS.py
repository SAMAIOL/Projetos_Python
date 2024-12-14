idade = int(input("informe a idade: "))

#if/else   traduzindo -> se/senao
if idade < 18:
    print("Menor de Idade")
elif idade >= 50:
    print("Terceira Idade")
else: 
    print("Maior de Idade")


    #if/else   traduzindo -> se/senao
if idade >= 18 and idade < 50:
    print("Maior de Idade")
elif idade >= 50:
    print("Terceira Idade")
else: 
    print("Menor de Idade")