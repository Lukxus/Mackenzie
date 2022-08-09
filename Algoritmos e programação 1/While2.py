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

    

Idade=[]
Sexo=[]

while True:
    
    idade=idade=(input(f'Qual é a idade da pessoa: ')).strip()
    
    while idade=='':
        print('Idade inválida!!!!')
        idade=(input(f'Qual é a idade da pessoa: ')).strip()
    
    
    sexo=input('Informe o sexo da pessoa[M/F]: ').strip().upper()
   
    while True:
        if sexo =='M' or sexo=='F':
            break
        else:
            print('Sexo inválido!!!!')
            sexo=input('Informe o sexo da pessoa[M/F]: ').strip().upper()

    Sexo.append(sexo)
    Idade.append(idade)
    choice=(input('Deseja inserir os dadso de outra pessoa[S/N]: ')).strip()
    
    
    while choice.upper() not in'SN':
        choice=(input(f'Deseja inserir os dados de outra pessoa[S/N]: ')).strip()
    
    if choice.upper()=='N':
        break

for x in range(0, len(Idade)):
    print(Sexo[x],'|',Idade[x])


print(f'{len(Idade)} pessoas foram registradas')


num_Mulheres=0
maior=0

for x in range(0, len(Idade)):
    
    maior=max(Idade, key=int)

    if Sexo[x]=='F':
        
        if int(Idade[x])>=18 and int(Idade[x])<=35:
            num_Mulheres=num_Mulheres+1
print(f'A maior idade registrada foi {maior} ')
print(f'{num_Mulheres} mulheres tem idade entre 18 e 35 anos.')
print(f'O percentual de mulheres com idade entre 18 e 35 anos é de {(num_Mulheres*100)/len(Idade)} %')
