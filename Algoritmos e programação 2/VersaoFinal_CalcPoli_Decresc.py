'''
Entrega do Trabalho ___- Algoritmos e Programação II
Nós,
Luiz Octavio Tassinari Saraiva
Fabio Domingues Pereira Sabino
declaramos que
todas as respostas são fruto de nosso próprio trabalho,
não copiamos respostas de colegas externos à equipe,
não disponibilizamos nossas respostas para colegas externos ao grupo e
não realizamos quaisquer outras atividades desonestas para nos beneficiar
ou prejudicar outros.
'''
#__________________________________________________________________________________________________________________
def menu():
    print("\nCALCULADORA DE POLINÔMIOS")
    print('\nDigite -1 para finalizar programa.')
    print("\nDigite 0 para calcular a soma entre dois polinômios.")
    print("\nDigite 1 para resolver um polinômio.")
#__________________________________________________________________________________________________________________
def formaPolinomio(vetor): 
    # %d é um placeholder para números |||| 1==>1 |||| -1==>-1  
    # %+d é um placeholder que pega o sinal do número também |||| 1==>+1 |||| -1==>-1  
    polinomio=''
    for i in range(len(vetor)-1, 0, -1):
        indice = vetor[i]
        termo = ''
        if indice == 0:
            continue
        elif i == 1:
            termo = '%+d' % (indice)
            polinomio = polinomio + termo + 'x'
        else:
            termo = '%+d' % (indice)
            polinomio = polinomio + termo + 'x^' + str(i)

    polinomio=polinomio.replace('+1x', '+x')
    polinomio=polinomio.replace('-1x', '-x')

    #Adicionar o termo que multiplica x^0
    termo_independente = '%+d' % (vetor[0])
    if termo_independente!='+0': #Apenas adicionamos o termo independente caso ele não seja 0.
        polinomio = polinomio + termo_independente

    #Por termos o %+d o primeiro valor do polinomio acaba ficando com sinal|| +1x^4... . Vamos retirar o sinal caso ele seja +.
    primeiro_char = polinomio[0] 
    if primeiro_char == '+':
        polinomio = polinomio[1:]

    #Colocar espaços para melhoras a formatação.
    polinomio = polinomio.replace('+', ' + ')
    polinomio = polinomio.replace('-', ' - ')
    return polinomio
            
#__________________________________________________________________________________________________________________
def lenMenorVetor(vetor_um, vetor_dois):
    if len(vetor_um)<=len(vetor_dois):
        return len(vetor_um)
    else:
        return(len(vetor_dois))
#__________________________________________________________________________________________________________________
def lenMaiorVetor(vetor_um, vetor_dois):
    if len(vetor_um)>=len(vetor_dois):
        return len(vetor_um)
    else:
        return(len(vetor_dois))
#__________________________________________________________________________________________________________________
def somaPolinomio(polinomio_um, polinomio_dois):
    maiorVetor=lenMaiorVetor(polinomio_um,polinomio_dois) #Pegamos o comprimento do maior vetor
    menorVetor=lenMenorVetor(polinomio_um,polinomio_dois) #pegamos o comprimento do menor vetor
    vetorResultadoSoma=[0]*maiorVetor
    for elemento in range(menorVetor): #Fazemos a soma de acordo com o polinômio de menor grau
        vetorResultadoSoma[elemento]=polinomio_um[elemento]+polinomio_dois[elemento]
    if len(polinomio_um)!=len(polinomio_dois): #Caso os polinômios tenham tamanhos diferentes precisamos completar o resultado com os elementos que estavam em uma posição maior do que o valor do comprimento do menor vetor
        if len(polinomio_um)==maiorVetor:
            for elemento in range(menorVetor,len(polinomio_um)):
                vetorResultadoSoma[elemento]=polinomio_um[elemento]
        if len(polinomio_dois)==maiorVetor:
            for elemento in range(menorVetor,len(polinomio_dois)):
                vetorResultadoSoma[elemento]=polinomio_dois[elemento]
    return('('+formaPolinomio(polinomio_um)+") + ("+ formaPolinomio(polinomio_dois)+") = ("+ formaPolinomio(vetorResultadoSoma)+')' )
#__________________________________________________________________________________________________________________
def resolvePolinomio(vetor,valorDeX):
    resultadoPolinomio=0
    for numero in range(len(vetor)):
        resultadoPolinomio+=vetor[numero]*(valorDeX**numero)
    return resultadoPolinomio
#__________________________________________________________________________________________________________________
def main():
    while True:
        menu()
        try:
            main_choice=int(input("\nESCOLHA: "))
            if main_choice==-1: #Para a execução do programa
                break

            elif main_choice==0: #Função de soma de polinômios
                contador=0
                while contador<2:
                    while True: #Verificação do input
                        try:
                            grau_polinomio_soma=int(input(f"\nDigite o grau do {contador+1}° polinômio: "))
                            if grau_polinomio_soma>=0:
                                break
                        except ValueError:
                                print("\nInsira um valor válido!!")
                    print(f"\nInsira os valores do {contador+1}° polinômio")
                    vetor_polinomio_gerado=[0]*(grau_polinomio_soma+1)
                    for grau in range(grau_polinomio_soma, -1, -1):
                        while True: #Verificação do input
                            try:
                                vetor_polinomio_gerado[grau]=int(input(f"Digite o valor para o elemento de grau {grau}: "))
                                break
                            except ValueError:
                                print("\nInsira um valor válido!!")
                        print('Polinômio 1: '+formaPolinomio(vetor_polinomio_gerado))
                    if contador==0:
                        polinomio_um=vetor_polinomio_gerado
                    else:
                        polinomio_dois=vetor_polinomio_gerado
                    contador+=1
                print(somaPolinomio(polinomio_um, polinomio_dois))

            elif main_choice==1: #Função de resolução de polinômios
                while True: #Verificação do input
                    try:
                        grau_polinomio_resolve=int(input(f"\nDigite o grau do polinômio: "))
                        if grau_polinomio_resolve>=0:
                                break
                    except ValueError:
                            print("\nInsira um valor válido!!")
                vetor_polinomio_gerado=[0]*(grau_polinomio_resolve+1)
                for grau in range(grau_polinomio_resolve, -1, -1):
                    while True: #Verificação do input
                        try:
                            vetor_polinomio_gerado[grau]=int(input(f"Digite o valor para o elemento de grau {grau}: "))
                            break
                        except ValueError:
                            print("\nInsira um valor válido!!")
                    print('Polinômio 1: '+formaPolinomio(vetor_polinomio_gerado))
                print(formaPolinomio(vetor_polinomio_gerado))
                while True: #Verificação do input
                    try:
                        valorDeX=int(input(f"\nDigite o valor de X: "))
                        break
                    except ValueError:
                            print("\nInsira um valor válido!!")
                print(resolvePolinomio(vetor_polinomio_gerado, valorDeX))
        except TypeError:
            print("Digite um valor válido!")
#__________________________________________________________________________________________________________________
main()
