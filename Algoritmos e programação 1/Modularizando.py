def verficate_Gender():
    sexo=input('Infrome o sexo da pessoa.[M/F]: ').strip().upper()
    while sexo not in 'MF':
        print('O sexo informado é inválido!!!!')
        sexo=input('Infrome o sexo da pessoa.[M/F]: ').strip().upper()
    return sexo
#---------------------------------------------------------------------------------------------------------------
def verficate_Salary():
    salary=input(('Informe o salário da pessoa: ')).strip()
    while int(salary)<850 or salary=='':
        print('O salário informado é inválido!!!!')
        salary=input(('Informe o salário da pessoa: ')).strip()
    return int(salary)
#---------------------------------------------------------------------------------------------------------------
def verficate_Name():
    name=input(('Informe o nome da pessoa da pessoa: ')).strip()
    while name=='':
        print('O salário informado é inválido!!!!')
        name=input(('Informe o nome da pessoa da pessoa: ')).strip()
    return name
#---------------------------------------------------------------------------------------------------------------
def reajuste(lista, gender, name):
    counter_Six_Half=0
    ajuste_H_total=0
    man_Counter=0
    for e in range(len(lista)):
        if lista[e]>=3000:
            ajuste=lista[e]*1.045
        elif lista[e]<3000 and lista[e]>=2000:
            ajuste=lista[e]*1.065
            counter_Six_Half+=1
        elif lista[e]<2000:
            ajuste=lista[e]*1.085
        if gender[e]=='M':
            man_Counter+=1
            ajuste_H_total= (ajuste_H_total) + ajuste- lista[e]
    for e in range(len(lista)):
        if lista[e]>=3000:
            lista[e]=lista[e]*1.045
        elif lista[e]<3000 and lista[e]>=2000:
            lista[e]=lista[e]*1.065
        elif lista[e]<2000:
            lista[e]=lista[e]*1.085
    print('-'*40)
    print('Dados com reajuste!!!')
    for ind in range(len(lista)):
        print(f'Funcionario: {name[ind]}|| Sexo:{gender[ind]}|| Salário: R${lista[ind]}')
    print('-'*40)
    print(f'{counter_Six_Half} pessoa(s) tiveram um aumento de 6,5%!')
    print(f"A media de aumento salarial para os homens foi de R${ajuste_H_total/man_Counter}.")
    
#---------------------------------------------------------------------------------------------------------------
def percentage_F_Gender(lista):
    counter=0
    for ind in range(len(lista)):
        if lista[ind]=='F':
            counter+=1
    return (counter*100)/len(lista)

#---------------------------------------------------------------------------------------------------------------
#Colocar o pessoal em listas e fazer entrada das pessoas
choice='S'
salary_list=[]
gender_list=[]
name_list=[]
while True:
    name_list.append(verficate_Name())
    gender_list.append(verficate_Gender())
    salary_list.append(verficate_Salary())
    
    choice=input("Você deseja inserir mais pessoas?[S/N]: ").strip().upper()
    if choice=='N':
        break
print('-'*40)
print('Dados informados')
for ind in range(len(salary_list)):
    print(f'Funcionario: {name_list[ind]}|| Sexo:{gender_list[ind]}|| Salário: R${salary_list[ind]}')
print('-'*40)
#---------------------------------------------------------------------------------------------------------------
#a) #b) #c)
print('-'*40)
reajuste(salary_list,gender_list, name_list)

#d)
wm_Percentage=percentage_F_Gender(gender_list)
print(f'A pocentagem de mulheres em relação ao total de empregados que trabalham na empresa é de {wm_Percentage}%')
