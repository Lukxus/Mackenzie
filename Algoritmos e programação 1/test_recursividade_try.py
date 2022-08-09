'''
2) Uma pesquisa sobre a população de uma determinada região coletou os seguintes
dados, referentes a cada habitante, para serem analisados:
• Idade (em anos)
• Sexo (M - masculino, F - feminino)
A fim de indicar o final da entrada, após a sequência de dados dos habitantes, o usuário
entrará com o valor -1 para a idade, o que deve ser interpretado pelo programa como
fim de entrada de dados.
O programa deve encontrar e mostrar:
- a maior idade de um conjunto de indivíduos e
- o percentual de indivíduos do sexo feminino com idade entre 18 e 35 anos.
'''

def confirm_Age():
    idade=(input(f'Qual é a idade da pessoa: ')).split()
    try:
        return int(idade)
            
    except:
        while True:
            print('Idade inválida!!!!')
            confirm_Age()
    

all=[]

while True:
    idade=confirm_Age()
    sexo=input('Informe o sexo da pessoa[M/F]: ').split().upper()
    while sexo not in 'MF':
        print('Sexo inválido!!!!')
        sexo=input('Informe o sexo da pessoa[M/F]: ').split().upper()

    all.append(sexo, idade)
    choice=(input(f'Deseja inserir os dadso de outra pessoa[S/N]: ')).split().upper()
    while choice not in'SN':
        choice=(input(f'Deseja inserir os dados de outra pessoa[S/N]: ')).split().upper()
    if choice=='N':
        break
    
print(all)
print(f'{len(all)/2} pessoas foram registradas')
print(f'A maior idade registrada foi {max(all)} ')

count=0
num_Mulheres=0
for p in all:
   
    if p=='F' and (all[count+1]>=18 and all[count+1]<=35):
        num_Mulheres=num_Mulheres+1
print(f'{num_Mulheres} mulheres tem idade entre 18 e 35 anos.')


        