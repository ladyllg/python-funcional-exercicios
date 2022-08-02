# Cubo de uma numero real
from functools import reduce


def cubo(numero):
    def recursiva(potencia):
        if potencia == 0:
            return 1
        else:
            return numero * recursiva(potencia-1)

    return recursiva(3)

# Terceiro elemento da lista
def terceiro_elem(lista):
    def recursiva(n, lista):
        if n == 2: # terceiro elemento = segunda chamada da func
            return lista[0]
        else:
            return recursiva(n+1,lista[1:])
    
    if len(lista) < 3:
        return "Lista tem menos que 3 elementos"
        
    else:
        return recursiva(0,lista)


## Fatorial 
def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n-1)

## Soma de todos os elementos de uma lista
def somatoria(lista):
    def soma(acc, elem):
        return acc + elem
    return reduce(soma, lista)
