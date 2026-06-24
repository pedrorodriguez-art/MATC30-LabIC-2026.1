def organizar_conteineres():
    q = int(input())

    for _ in range(q):
        n = int(input())

        conteineres = []

        for _ in range(n):
            conteineres.append(list(map(int, input().split())))

        capacidades = []
        for conteiner in conteineres:
            total = 0
            for valor in conteiner:
                total += valor
            capacidades.append(total)

        quantidades = []

        for tipo in range(n):
            total_tipo = 0
            for conteiner in range(n):
                total_tipo += conteineres[conteiner][tipo]

            quantidades.append(total_tipo)

        for i in range(len(capacidades)):
            for j in range(i + 1, len(capacidades)):
                if capacidades[i] > capacidades[j]:
                    capacidades[i], capacidades[j] = capacidades[j], capacidades[i]

        for i in range(len(quantidades)):
            for j in range(i + 1, len(quantidades)):
                if quantidades[i] > quantidades[j]:
                    quantidades[i], quantidades[j] = quantidades[j], quantidades[i]

        if capacidades == quantidades:
            print("Possible")
        else:
            print("Impossible")


organizar_conteineres()
