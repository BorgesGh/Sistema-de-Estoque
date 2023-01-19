####### VETORES #######

#ATENÇÃO, RODE O PROGRAMA PRIMEIRO PARA SE TER CONHECIMENTO DE COMO FUNCIONA!!!!!

codigos = [] #Armazenar os codigos
valores = []
############ MENU  ############## Opções disponiveis para acessar 
def menu() :
    op = -1
    while op < 0 or op > 6:
        print("SISTEMA DE ESTOQUE:")
        print("1-INSERIR PRODUTO")
        print("2-PESQUISAR POR CÓDIGO")
        print("3-AUMENTAR PREÇO")
        print("4-MAIOR PREÇO")
        print("5-EXCLUIR")
        print("6-LISTAR")
        print("0-SAIR")
        op = int(input("Escolha sua opção: "))
    return op

############# LEITOR CODIGO ############# Funções responsáveis para inserir o código do produto
def LerCodigo(): 
    x = input("Código do produto: ") 
    while x.isdigit() == False: 
        print("Valor inválido!") 
        x = input("Código do produto: ") 
    return int(x) 

def ValidarCodigo(): 
    x = LerCodigo()
    while x < 0 or x > 999999999: 
        print("Valor inválido!")
        x = LerCodigo() 
    return x 
############# LEITOR PREÇO ############# Funções responsáveis para inserir o preço do produto
def LerValor(): 
    x = input("Digite o valor: ") 
    while x.replace(".","",1).isdigit() == False: #Se o valor não for número real, o código pede para inserir novamente
        print("Valor inválido!!") 
        x = input("Digite o valor: ") 
    return float(x) 

def ValidarValor(): 
    x = LerValor() 
    while x < 0: 
        print("Valor inválido!!") 
        x = LerValor() 
    return x 
############ FUNÇÕES LEITORAS ############# Função Mestra, resposável por caçar um produto e retornar o Índice 
def PESQUISAR(a,b):
    for i, e in enumerate(a): 
        if e == b:
            return i

    return -1 


def Maior(a,b): # Verificação de maior produto, o maior restornará o seu índice
    if a > b: 
        return a 
    else: 
        return b  

##############################################################
#################### OPÇÕES DO PROGRAMA ######################
##############################################################

############ FUNÇÃO ADICIONAR ############ 
def ADC(x,y):

    codigo = ValidarCodigo()
    g = PESQUISAR(x,codigo)
    while g > -1: 
        print("\nO código já existe!!\n")
        codigo = ValidarCodigo()
        g = PESQUISAR(x,codigo)

    preco = ValidarValor() 

    x.append(codigo)
    y.append(preco)

############ FUNÇÃO PESQUISAR ############### Inserir o codigo do produto e retornará o preço
def PESQ(a):
    x = ValidarCodigo() 
    t = PESQUISAR(a,x) 
    return t

############# AUMENTAR O PREÇO ############## 
def AP(a,b): 
    print("Digite a porcentagem de aumento(Não é necessario digitar - % -)")

    porcent = ValidarValor()
    i = PESQ(a)
    while i == -1: 
        print("Código inválido!!")
        i = PESQ(a) 

    print("Antigo valor:\n%.2f\n" %b[i]) 
    b[i] = b[i] + (b[i] * (porcent/100)) 
    print("Novo valor do produto:\n%.2f\n" %b[i]) 

############# MAIOR PREÇO ################### 
def Maioral(a,b):
    grande = 0
    indice = 0
    for i,e in enumerate(b): 
        grande = Maior(e,grande)
        if grande == e: 
            indice = i
    print("Maior valor!\nCodigo: %d\nValor: %.2f"%(a[indice],b[indice]))
          
################ EXCLUIR ################### 
def Excluir(a,b):
    x = PESQ(a) 
    del(a[x]) 
    del(b[x]) 
    print("Produto excluído com sucesso!") 

############### LISTAR ###################### Vai mostrar todos os produtos na tela
def LIST(a,b): 
    print("CÓDIGO DO PRODUTO      VALOR")
    for i,e in enumerate(a): 
        print(f"{a[i]:<15} {b[i]:>15}")  #ESTILIZAÇÃO 
        

###################################### PRINCIPAL ########################
# local onde ocorre as chamadas de funções feitas acima :)
op = 1
while op != 0:
    op = menu()
    
    if op == 0:
        print("\n\nFIM DO PROGRAMA\n\n")
        
    elif op == 1:
        print("\n\nADICIONAR\n\n")
        ADC(codigos,valores)       
        
    elif op == 2:
        print("\n\nPESQUISAR\n\n")
        t= PESQ(codigos)
        if t == -1: 
            print("Produto não encontrado!!")
        else: 
            print("CODIGO DO PRODUTO  e  PREÇO \n %d   e   %.2f  \n\n"%(codigos[t],valores[t]))

    elif op == 3:
        print("\n\nAUMENTAR PREÇO\n\n")
        AP(codigos,valores)

    elif op == 4:
        print("\n\nMAIOR VALOR\n\n")
        Maioral(codigos,valores) 

    elif op == 5:
        print("\n\nEXCLUIR\n\n")
        Excluir(codigos,valores)

    elif op == 6:
        print("\n\nLISTAR\n\n")
        LIST(codigos,valores)

    else:
        print("Opção inválida!")

    input("\nPressione <enter> para continuar ...\n")
    
