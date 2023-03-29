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


# Exercíío 4.6

distancia = float(input("qual a distância a ser percorrida em km: \n"));

if distancia <= 200:
    custo = distancia * 0.50
    
elif distancia > 200:
    custo = distancia * 0.50

print("o custo da sua passagem sera de R$%5.2f" % custo);
# ---------------------------------------------------------------------------------------------

#Exercício 4.8

numero1 = float(input("o numero a ser utilizado: \n"));
numero2 = float(input("o numero a ser utilizado: \n"));

soma = 1
subtraçao = 2
divisao = 3
multiplicaçao =4
operaçao = int(input("qual operação você deseja realizar:\n soma(1) \n subtração(2) \n divisão(3) \n multiplicação(4) \n "));
a = 0             
             
if operaçao == 1:
    a = numero1 + numero2;
    
elif operaçao == 2:
    a = numero1 - numero2;
    
elif operaçao == 3:
    a = numero1 / numero2;
    
elif operaçao == 4:
    a = numero1 * numero2
    

print(a);
#--------------------------------------------------------------------------------------------------------------------------------------------
    
    



