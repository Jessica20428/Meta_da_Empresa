#Construa um programa que calcule: Qual deve ser o bônus de um Funcionário? Se a empresa bateu a meta de 10.000 vendas 
#e se ele vendeu mais de 1.000 unidades, o bônus tem que ser de R$250, caso contrário, o bônus tem que ser de R$50.
#Se a empresa não bateu a meta de R$10.000, o bônus dele em que ser 0.

vendas = 2.000
meta = 1.000
vendas_empresa = 8.000
meta_empresa = 10.00

if vendas_empresa > meta_empresa:
    bonus = 250
else:
    bonus = 50
if vendas_empresa < meta_empresa:
    bonus = 0
print(bonus)