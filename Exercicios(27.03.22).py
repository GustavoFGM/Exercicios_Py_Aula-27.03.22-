# Exercício 4.2 

velocidadeAutomovel = float(input("velocidade atual do automovel \n"));

if velocidadeAutomovel > 80:
    diferença = velocidadeAutomovel - 80
    multa = diferença * 5
    print("você recebera uma multa de R$%5.2f por estar acima do limite de velocidade" % multa);

else:
    print("esta dentro do limite permitido");
# -------------------------------------------------------------------------------------------------

# Exercício 4.3
maior_numero = 0
menor_numero = 0 
x = 1
while x <= 3:
    a = float(input("digite numero %d \n" %x));
    if x == 1:
        maior_numero = a
        menor_numero = a
    else:
        if a < menor_numero:
            menor_numero = a
        elif a > maior_numero:
            maior_numero = a
        
    x = x + 1
print("o maior numero digitado foi %5.2f, e o menor numero digitado foi %5.2f"% (maior_numero, menor_numero))
#---------------------------------------------------------------------------------------------------------------------

# Exercício 4.4

salario = float(input("Salario atual: "));
if salario > 1250.00:
    aumento = salario * 0.1
    salarioFinal = salario + aumento
    
elif salario <= 1250.00:
    aumento = salario * 0.15
    salarioFinal = salario + aumento


    
print("O salario após o aumento sera de R$%5.2f" % salarioFinal);
# ----------------------------------------------------------------------------------------------------------------------


    


