def esta_seguro(processos, disponivel, maximo, alocado):
    necessidade = [0]*len(processos)

    for i in range(len(processos)):
        necessidade[i] = maximo[i] - alocado[i]

    finalizado = [0]*len(processos)
    sequencia_segura = [0]*len(processos)

    trabalho = disponivel
    contagem = 0
    while contagem < len(processos):
        encontrado = False
        for p in range(len(processos)):
            if finalizado[p] == 0 and necessidade[p] <= trabalho:
                trabalho += alocado[p]
                sequencia_segura[contagem] = p
                contagem += 1
                finalizado[p] = 1
                encontrado = True
        print("Instâncias livres após a rodada {}: {}".format(contagem, trabalho))
        if not encontrado:
            print("Sistema não está em estado seguro")
            return False, []
    print("Sistema está em estado seguro. Sequência segura é: ", *sequencia_segura)
    return True, sequencia_segura

num_processos = 5
num_recursos = 12
num_alocados = 10
num_livres = num_recursos - num_alocados

processos = list(range(num_processos))
disponivel = num_livres
maximo = [5, 5, 6, 7, 4]
alocado = [2, 3, 2, 2, 1]
esta_seguro(processos, disponivel, maximo, alocado)