def organizingContainers(container: list[list[int]]) -> str:
    num_types = len(container)
    row = [0] * num_types
    col = [0] * num_types

    for i in range(num_types):
        for j in range(num_types):
            row[i] += container[i][j]
            col[j] += container[i][j]
    
    if sorted(row) == sorted(col):
        return "Possible"
    
    return "Impossible"


if __name__ == "__main__":
    q = int(input().strip())
    results = []
    for q_itr in range(q):
        n = int(input().strip())
        container = []
        for _ in range(n):
            container.append(list(map(int, input().split())))

        results.append(organizingContainers(container))
        
    print("\n".join(results))

