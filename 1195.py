class NodoArvore:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def insere(self, chave):
        novo_nodo = NodoArvore(chave)
        if not self.raiz:
            self.raiz = novo_nodo
            return
        
        atual = self.raiz
        while True:
            if chave < atual.chave:
                if not atual.esquerda:
                    atual.esquerda = novo_nodo
                    return
                atual = atual.esquerda
            else:
                if not atual.direita:
                    atual.direita = novo_nodo
                    return
                atual = atual.direita

    def pre_ordem(self, raiz, resultado):
        if raiz:
            resultado.append(str(raiz.chave))
            self.pre_ordem(raiz.esquerda, resultado)
            self.pre_ordem(raiz.direita, resultado)

    def in_ordem(self, raiz, resultado):
        if raiz:
            self.in_ordem(raiz.esquerda, resultado)
            resultado.append(str(raiz.chave))
            self.in_ordem(raiz.direita, resultado)

    def pos_ordem(self, raiz, resultado):
        if raiz:
            self.pos_ordem(raiz.esquerda, resultado)
            self.pos_ordem(raiz.direita, resultado)
            resultado.append(str(raiz.chave))

# Entrada
import sys
input = sys.stdin.read
dados = input().splitlines()

qtd_arvores = int(dados[0])  # Quantidade de árvores
linha_atual = 1

# Processa cada caso de teste
saidas = []
for i in range(qtd_arvores):
    arvore = ArvoreBinaria()
    qtd_valores = int(dados[linha_atual])  # Quantidade de valores
    linha_atual += 1
    valores = map(int, dados[linha_atual].split())  # Lista de valores
    linha_atual += 1

    # Insere os valores na árvore
    for valor in valores:
        arvore.insere(valor)
    
    # Percursos
    resultado_pre = []
    resultado_in = []
    resultado_pos = []

    arvore.pre_ordem(arvore.raiz, resultado_pre)
    arvore.in_ordem(arvore.raiz, resultado_in)
    arvore.pos_ordem(arvore.raiz, resultado_pos)

    # Formata a saída
    saidas.append(f"Case {i + 1}:")
    saidas.append(f"Pre.: {' '.join(resultado_pre)}")
    saidas.append(f"In..: {' '.join(resultado_in)}")
    saidas.append(f"Post: {' '.join(resultado_pos)}")
    saidas.append("")

# Saída final
sys.stdout.write("\n".join(saidas) + "\n")
