class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return f'{self.esquerda and self.esquerda.chave} <- {self.chave} -> {self.direita and self.direita.chave}'

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        
    def arvore_vazia(self):
        return self.raiz is None
        
    def insere(self, raiz, nodo):
        # Nodo deve ser inserido na raiz.
        if raiz is None:
            return nodo
        
        # Nodo deve ser inserido na subárvore direita.
        if nodo.chave > raiz.chave:
            if raiz.direita is None:
                raiz.direita = nodo
            else:
                raiz.direita = self.insere(raiz.direita, nodo)
        # Nodo deve ser inserido na subárvore esquerda.
        else:
            if raiz.esquerda is None:
                raiz.esquerda = nodo
            else:
                raiz.esquerda = self.insere(raiz.esquerda, nodo)
        
        return raiz

    def pre_ordem(self, raiz):
        if not raiz:
            return []
        # Visita nodo corrente.
        resultado = [raiz.chave]
        # Visita filho da esquerda.
        resultado.extend(self.pre_ordem(raiz.esquerda))
        # Visita filho da direita.
        resultado.extend(self.pre_ordem(raiz.direita))
        return resultado
        
    def in_ordem(self, raiz):
        if not raiz:
            return []
        resultado = self.in_ordem(raiz.esquerda)
        resultado.append(raiz.chave)
        resultado.extend(self.in_ordem(raiz.direita))
        return resultado
        
    def pos_ordem(self, raiz):
        if not raiz:
            return []
        resultado = self.pos_ordem(raiz.esquerda)
        resultado.extend(self.pos_ordem(raiz.direita))
        resultado.append(raiz.chave)
        return resultado

    def existe(self, raiz, valor):
        if raiz is None:
            print(valor, 'nao existe')
            return False
        if raiz.chave == valor:
            print(valor, 'existe')
            return True
        if valor < raiz.chave:
            return self.existe(raiz.esquerda, valor)
        else:
            return self.existe(raiz.direita, valor)
        
# Instancia a árvore binária
arvore = ArvoreBinaria()

while True:
    try:
        entrada = input()
        parts = entrada.split(' ')
        if len(parts) == 1:
            if entrada == 'INFIXA':
                print(" ".join(str(x) for x in arvore.in_ordem(arvore.raiz)))
            elif entrada == 'POSFIXA':
                print(" ".join(str(x) for x in arvore.pos_ordem(arvore.raiz)))
            elif entrada == 'PREFIXA':
                print(" ".join(str(x) for x in arvore.pre_ordem(arvore.raiz)))
        else:
            if parts[0] == 'I':
                nodo = NodoArvore(parts[1])
                arvore.raiz = arvore.insere(arvore.raiz, nodo)
            elif parts[0] == 'P':
                arvore.existe(arvore.raiz, parts[1])
    except EOFError:
        break
