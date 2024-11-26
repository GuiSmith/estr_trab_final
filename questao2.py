#Referencia - https://algoritmosempython.com.br/cursos/algoritmos-python/estruturas-dados/arvores/

import os

class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
        self.nivel = 1

    def subirNivel(self):
        self.nivel += 1
    
    def pegarNivel(self):
        return self.nivel

    def __repr__(self):
        return '%s <- %s (%s) -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.nivel,
                                    self.direita and self.direita.chave)

class ArvoreBinaria:
    def __init__(self):
        self.inicio = None
        self.contadorMaiorQue = 0
        self.quantidadeNodosInternos = 0
        self.contadorNivel = 0
        
    def ArvoreVazia(self,raiz):
        return raiz == None
        
    def insere(self, raiz, nodo):
        # Nodo deve ser inserido na raiz.
        if raiz is None:
            raiz = nodo
        
        # Nodo deve ser inserido na sub�rvore direita.
        elif int(nodo.chave) > int(raiz.chave):
            print(raiz.chave," -> ",nodo.chave)
            print('Inseriu a direita')
            nodo.subirNivel()
            print('Nivel ',raiz.nivel, " -> ",nodo.nivel)
            if raiz.direita is None:
                raiz.direita = nodo
                if raiz.esquerda is None:
                    self.quantidadeNodosInternos += 1
            else:
                self.insere(raiz.direita, nodo)
        # Nodo deve ser inserido na sub�rvore esquerda.
        else:
            print(nodo.chave," <- ",raiz.chave)
            print('Inseriu a esquerda')
            nodo.subirNivel()
            print('Nivel ',raiz.nivel, " -> ",nodo.nivel)
            if raiz.esquerda is None:
                raiz.esquerda = nodo
                if raiz.direita is None:
                    self.quantidadeNodosInternos += 1
            else:
                self.insere(raiz.esquerda, nodo)

    def pre_ordem(self, raiz):
        if not raiz:
            return
        # Visita nodo corrente.
        #print(raiz)
        print(raiz.__repr__())
        # Visita filho da esquerda.
        self.pre_ordem(raiz.esquerda)
        # Visita filho da direita.
        self.pre_ordem(raiz.direita)
        
    def in_ordem(self, raiz):
        if not raiz:
            return
        self.in_ordem(raiz.esquerda)
        print(raiz.__repr__())
        self.in_ordem(raiz.direita)
        
    def pos_ordem(self, raiz):
        if not raiz:
            return
        self.pos_ordem(raiz.esquerda)
        self.pos_ordem(raiz.direita)
        print(raiz.__repr__())
    
    # Esta função mostra na tela a quantidade de nodos internos de uma arvore
    def nodosInternos(self, raiz):
        if not raiz:
            return
        print(self.quantidadeNodosInternos)

    # Esta função atualiza o contador interno de nodos maior que um numero informado pelo usuário (opção 6 do menu)
    def definirQuantidadeMaiorQue(self, raiz, valor):
        if not raiz:
            return
        self.definirQuantidadeMaiorQue(raiz.esquerda, valor)
        if int(raiz.chave) > int(valor):
            self.contadorMaiorQue += 1
        self.definirQuantidadeMaiorQue(raiz.direita, valor)
    
    # Esta função resgata o contador interno de nodos maior que o numero informado pelo usuário
    def pegarQuantidadeMaiorQue(self):
        temp = self.contadorMaiorQue
        self.contadorMaiorQue = 0
        return temp
    
    # Esta função chama as duas funções acima e realiza a opção 6 do menu por completo
    def quantidadeMaiorQue(self, raiz, valor):
        if not raiz:
            return
        self.definirQuantidadeMaiorQue(raiz, valor)
        print(self.pegarQuantidadeMaiorQue())

    def nivelNodo(self,raiz,valor):
        if not raiz:
            return
        self.nivelNodo(raiz.esquerda,valor)
        if int(raiz.chave) == int(valor):
            print('Nivel: ', raiz.pegarNivel())
        self.nivelNodo(raiz.direita,valor)
          
Arvore = ArvoreBinaria()
raiz = None
while True:
    os.system('clear')
    print("1 - Insere valores na arvore.")
    print("2 - Exibir Pre-ordem.")
    print("3 - Exibir In-ordem.")    
    print("4 - Exibir Pos-ordem.")
    print("5 - Exibir quantidade de nodos internos.")
    print("6 - Exibir quantidade de nodos com valor maior que numero informado.")    
    print("7 - Exibir nivel de valor informado.")    
    print("0 - Sair.")
    OP = int(input("Entre com a opcao desejada: "))
    if OP == 0:
        break
    elif OP == 1:
        valor = input("Entre com o valor: ")
        if Arvore.ArvoreVazia(raiz):
            print('Nodo Raiz')
            raiz = NodoArvore(valor)
        else:
            nodo = NodoArvore(valor)
            Arvore.insere(raiz,nodo)        
    elif OP == 2:
        if Arvore.ArvoreVazia(raiz):
            print("�RVORE VAZIA!!!!!!!!!!!")                       
        Arvore.pre_ordem(raiz)        
    elif OP == 3:
        if Arvore.ArvoreVazia(raiz):
            print("��RVORE VAZIA!!!!!!!!!!!")                       
        Arvore.in_ordem(raiz)                      
    elif OP == 4:
        if Arvore.ArvoreVazia(raiz):
            print("��RVORE VAZIA!!!!!!!!!!!")                       
        Arvore.pos_ordem(raiz)  
    elif OP == 5:
        if Arvore.ArvoreVazia(raiz):
            print("��RVORE VAZIA!!!!!!!!!!!")
        Arvore.nodosInternos(raiz)
    elif OP == 6:
        if Arvore.ArvoreVazia(raiz):
            print("��RVORE VAZIA!!!!!!!!!!!")
        valor = input('Valor: ')
        Arvore.quantidadeMaiorQue(raiz,valor)
    elif OP == 7:
        if Arvore.ArvoreVazia(raiz):
            print("��RVORE VAZIA!!!!!!!!!!!")
        valor = input('Valor: ')
        Arvore.nivelNodo(raiz,valor)
    else:
      print("OPCAO INVALIDA!!!!!!!!!!!")                       
    input("Digite uma tecla para continuar.")