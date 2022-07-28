""" Algoritmos por Laura Lima em 2022
    Github: @ladyllg
"""

from functools import reduce

def cria_lista(x):
    return list(range(1, x+1))

def produto(acc, elem):
    return acc * elem

def somatoria_float(acc, elem):
    return float(acc) + float(elem)
    
def quadrado(a):
    return a * a

""" 1) recebe como argumento um número natural n e devolve a soma
    de todos os números naturais até n
"""
def soma_nat(n):
    if n == 0:
        return 0
    else:
        return n + soma_nat(n-1)

""" 2) recebe como argumento um número natural n devolve a lista
    dos n primeiros quadrados perfeitos """
def quadrados(n):
    return list(map(quadrado, range(1, n+1)))

""" 3) recebe como argumento um número natural n devolve a lista
    dos n primeiros quadrados perfeitos, por ordem DESCRESCENTE
"""
def quadrados_inv(n):
    return list(map(quadrado, range(n, 0, -1)))

""" 4) recebe como argumento um número inteiro positivo e devolve
    True se esse número for um número perfeito e False em caso contrário.
"""
def num_perf(n):
    def recursividade(n, i=1):
        if n == i:
            return 0
        elif n % i == 0:
            return i+recursividade(n, i+1)
        else:
            return recursividade(n, i+1)

    return False if n < 2 else recursividade(n) == n

""" 5) recebe como argumento uma lista e devolve essa lista invertida
"""
def inverte_lista(lista):
    if len(lista) <= 1:
        return lista
    else:
        return lista[-1:] + inverte_lista(lista[:-1]) 

""" 6) recebe como argumento uma lista de números inteiros w e
    devolve a lista dos elementos de w em posições pares
"""
def indices_pares(lista):
    if len(lista) == 0:
        return lista
    if len(lista) % 2 == 0:
        return lista[:1] + indices_pares(lista[1:])
    else:
        return indices_pares(lista[1:])

""" 7) recebe como argumento um número natural n e devolve uma lista
    em que o primeiro elemento é a lista [1], o segundo elemento é a lista [1, 2]
    e assim sucessivamente até n
"""
def triangulo(n):
    lista = range(1, n+1)
    return list(map(cria_lista, lista))

""" 8) recebe como argumento uma lista de números inteiros e devolve
    o produto dos seus elementos
"""
def prod_lista(lista):
    if len(lista) > 0:
        return lista[len(lista) - 1] * prod_lista(lista[:-1])
    else:
        return 1

""" 9) recebe como argumentos uma lista de números inteiros w e um
    número inteiro x e devolve o número de ocorrências de x em w
"""
def conta(lista, elem):
    return lista.count(elem)

""" 10) recebe como argumento uma lista de números inteiros w e
    devolve True se w contém um número par e False em caso contrário
"""
def contem_parQ(lista):
    return any(map(lambda k: k%2==0, lista))

""" 11) recebe como argumento uma lista de números inteiros w e
    devolve True se w contém apenas números ímpares e False em caso contrário
"""
def contem_imparesQ(lista):
    return not contem_parQ(lista) 

""" 12) recebe como argumentos uma lista de números inteiros w e um
    número inteiro n e devolve True se n ocorre em w e False em caso contrário
"""
def pertenceQ(lista, n):
    return any(map(lambda k: k==n, lista))

""" 13) recebe como argumento uma lista e devolve True se a lista for
    constituída exclusivamente por números inteiros e False em caso contrário
"""
def int_listaQ(lista):
    try:
        return not any(map(lambda k: type(k) != int, lista))
    except:
        ## Caso nao seja uma lista
        return False 

""" 14) recebe como argumento uma lista e devolve True se a lista for
    constituída exclusivamente por números naturais e False em caso contrário
"""
def nat_listaQ(lista):
    only_inteiros = int_listaQ(lista) ## Chega se existem valores do tipo float
    if only_inteiros:
        return not any(map(lambda k: k < 0, lista)) ## Se encontrar algum inteiro negativo: !True
    else:
        return False

""" 15) recebe como argumento uma lista e devolve True se a lista
    for constituída exclusivamente por listas de números inteiros e False em caso contrário
"""
def int_lista_listaQ(lista):    
    ## Caso encontre algum elemento da lista que NÃO é uma lista de INTEIROS, retorna True que posteriormente significa False 
    return not any(map(lambda k: int_listaQ(k) == False, lista)) 

""" 16) recebe como argumento uma lista de números inteiros w e
    devolve a lista dos elementos pares de w
"""
def escolhe_pares(lista):
    return list(filter(lambda k: k%2==0,lista)) # Filtra indexes dos numeros pares

""" 17) recebe como argumento uma lista m e devolve True se m for
    uma matriz de números inteiros e False em caso contrário
"""
def int_matrizQ(lista):
    if int_lista_listaQ(lista): # Se for uma lista APENAS com lista de inteiros
        ordem = len(max(lista, key=list)) # Definindo qual a ordem da matriz
        return not any(map(lambda k: len(k) != ordem, lista)) # Se existe qualquer lista com tamanho diferente da ordem da matriz, cancela
    else:
        return False 

""" 18) recebe como argumento uma lista de números inteiros e
    devolve a lista resultante de retirar todos os números negativos
"""
def retira_negativos(lista):
    return list(filter(lambda k: k > 0, lista))

""" 19) recebe como argumentos dois números naturais m e n e devolve o
    resultado da divisão inteira de m por n
"""
def div(m,n):
    if m < n:
        return 0
    return 1 + div(m - n,n) # Repete ate o dividendo ser menor que o divisor 

""" 20) recebe como argumento um número natural n e devolve o
    primeiro algarismo (o mais significativo) na representação decimal de n
"""
def prim_alg(n):
    if n < 10:
        return int(n)
    else:
        return prim_alg(n/10)

""" 21) recebe como argumento um número natural e devolve a
    média dos seus dígitos
"""
def media_digitos(n):
    result = reduce(somatoria_float, list(str(n)))
    return result/len(list(str(n)))

""" 22) recebe como argumentos duas listas w1 e w2 e devolve True se
    w2 for permutação de w1, e devolve False em caso contrário
"""
def permutacao(a,b):
    if len(a) == 0:
        return len(b)==0 
    if a[0] in b:
        i = b.index(a[0])
        return permutacao(a[1:],b[0:i]+b[i+1:])
    return False

""" 23) recebe como argumento uma lista e devolve o seu
    comprimento. Não pode, como é óbvio, recorrer à função len
"""
def comprimento(lista):
    def recursivamente(lista):
        if not lista:
            return 0
        else:
            return 1 + recursivamente(lista[1:])

    return recursivamente(lista)

""" 24) recebe como argumentos duas listas w1 e w2 e devolve a lista
    resultante de intercalar os elementos de w1 com os de w2
"""
def intercala(w1, w2):
    # Caso base: quando uma lista termina, returna a outra lista e está vai ser colocada no final da lista resultante
    if not w1:
        return w2
    elif not w2:
        return w1
    else:
        # Faz a intercalação de 1 elemento de w1 com 1 elemento de w2 e chama a função novamente
        return [w1[0] , w2[0]] + intercala(w1[1:], w2[1:])

""" 25) recebe como argumentos uma lista de inteiros w e um número
    inteiro k e devolve a lista que resulta de apagar de w todas as ocorrências de k
"""
def apaga(lista, n):
    if not lista:
        return []   
    elif lista[0] != n: # Se cabeça da lista for DIFERENTE do valor n, entao retorna esse valor e chama a func de novo com a calda da lista
        return [lista[0]] + apaga(lista[1:], n)
    else:
        return apaga(lista[1:], n) # Caso contrario, ignora a cabeça da lista

""" 26) recebe como argumento uma lista não vazia de números inteiros
    e devolve o seu máximo
"""
def maximo(lista):
    def recursiva(lista, n):
        if not lista:
            return n
        elif lista[0] > n:
            return recursiva(lista[1:], lista[0])
        else:
            return recursiva(lista[1:], n)   

    return recursiva(lista, lista[0])

""" 27) recebe como argumentos uma lista de números inteiros w e um
    número inteiro k e devolve a lista das posições em que k ocorre em w
"""
def lposicoes(lista, w):
    pos = 0
    def recursiva(lista, pos, w):        
        if not lista:
            return []
        elif lista[0] == w:
            return [pos] + recursiva(lista[1:], pos+1, w)
        else:
            return recursiva(lista[1:], pos+1, w)   

    return recursiva(lista, pos, w)

""" 28) recebe como argumento uma lista de números inteiro e devolve a
    lista das posições onde ocorre o máximo da lista
"""
def pos_max(lista):
    maximo_valor = maximo(lista)
    return lposicoes(lista, maximo_valor)

""" 29) recebe como argumento uma lista de listas de números inteiros w={w1,...,wn}
    e devolve a lista r={r1,...,rn} em que ri é composta pelas posições dos números
    pares em wi
"""
def ind_pares(lista_de_listas):
    
    def pos_pares(lista, pos):
        if len(lista) == 0:
            return []
        if lista[0] % 2 == 0:
            return [(pos)] + pos_pares(lista[1:],pos+1)
        else:
            return pos_pares(lista[1:],pos+1)

    def recursiva(lista):
        if not lista:
            return []
        else:
            return [pos_pares(lista[0],0)] + recursiva(lista[1:])

    return recursiva(lista_de_listas)

""" 30) recebe como argumento um número natural n e devolve o
    n-ésimo número da sucessão de Fibonacci
"""
def fibonacci(n):    
    if n == 1:
        return 1
    else:
        if n == 2:
            return 1  
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    