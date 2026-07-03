def organizingContainers(container: list[list[int]]) -> str:
    n = len(container)

    row = [0] * n
    col = [0] * n

    for i in range(n):
        for j in range(len(container[i])):  # evita IndexError
            row[i] += container[i][j]
            col[j] += container[i][j]

    if sorted(row) == sorted(col):
        return "Possible"

    return "Impossible"


def main():
    q = int(input().strip())

    for _ in range(q):
        n = int(input().strip())
        container = []

        for _ in range(n):
            container.append(list(map(int, input().split())))

        print(organizingContainers(container))


if __name__ == "__main__":
    main()