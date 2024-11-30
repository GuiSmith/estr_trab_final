def selection_sort(lista_informada,debug = False):
    list = lista_informada[:]
    if debug: print(f"Lista inicial: {list}")
    for i in range(0,len(list)):
        if debug: 
            print()
            print('Posição:',i)
            print('valor:',list[i])
            print()
        lower = list[i]
        lower_index = i
        for j in range(i+1,len(list)):
            if i == len(list)-1:
                break
            if debug: print(list[j],'é menor que',lower,'?')
            if list[j] < lower:
                lower = list[j]
                lower_index = j
                if debug: 
                    print('Sim')
                    print('Menor agora é ',lower)
            else:
                if debug: print('Não')
            if debug: print()
        if lower_index == i:
            if debug: print('Nenhuma mudança é necessária')
        else:
            if debug:
                print(f"Trocando {list[lower_index]} e {list[i]} de posição")
                print(f"Antes: {list}")
            list[lower_index],list[i] = list[i],list[lower_index]
            if debug: print(f"Depois: {list}")
    if debug: print(f"Resultado final: {list}")
    return list

nomes_quantidade = int(input()) # Pegando quantidade de nomes
nomes = []
comportaram = 0
nao_comportaram = 0
for i in range(nomes_quantidade):
    nome = input()
    parts = nome.split(' ')
    if parts[0] == '+':
        comportaram += 1
    else:
        nao_comportaram += 1
    nomes.append(parts[1])
nomes_ordenados = selection_sort(nomes)
for nome in nomes_ordenados:
    print(nome)
print(f"Se comportaram: {comportaram} | Nao se comportaram: {nao_comportaram}")