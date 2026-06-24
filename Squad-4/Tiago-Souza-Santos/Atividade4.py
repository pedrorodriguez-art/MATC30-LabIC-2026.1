def organizingContainers(container):
    n = len(container)
    container_capacities = [sum(row) for row in container]
    ball_type_totals = [sum(container[i][j] for i in range(n)) for j in range(n)]
    container_capacities.sort()
    ball_type_totals.sort()
    if container_capacities == ball_type_totals:
        return "Possible"
    else:
        return "Impossible"

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        n = int(input().strip())
        container = []
        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))
        result = organizingContainers(container)
        print(result)
