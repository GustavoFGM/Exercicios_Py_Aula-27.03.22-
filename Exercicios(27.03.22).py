# Exercício 4.2 

velocidadeAutomovel = float(input("velocidade atual do automovel \n"));

if velocidadeAutomovel > 80:
    diferença = velocidadeAutomovel - 80
    multa = diferença * 5
    print("você recebera uma multa de R$%5.2f por estar acima do limite de velocidade" % multa);

else:
    print("esta dentro do limite permitido");
# -------------------------------------------------------------------------------------------------