# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 
pName = str(input('Me informe o seu nome: ')).title().strip()
rName = pName.split()
print(f'Muito prazer {pName}. O seu primeiro nome é {rName[0]} e o último nome é {rName[-1]}')
