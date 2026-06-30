def organizingContainers(container):
    n = len(container)
    
    container_capacities = [0] * n
    for i in range(n):
        row_sum = 0
        for j in range(n):
            row_sum += container[i][j]
        container_capacities[i] = row_sum

    ball_types_count = [0] * n
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += container[i][j]
        ball_types_count[j] = col_sum

    for i in range(n):
        for j in range(0, n - i - 1):
            if container_capacities[j] > container_capacities[j + 1]:
                temp = container_capacities[j]
                container_capacities[j] = container_capacities[j + 1]
                container_capacities[j + 1] = temp

    for i in range(n):
        for j in range(0, n - i - 1):
            if ball_types_count[j] > ball_types_count[j + 1]:
                # Troca manual
                temp = ball_types_count[j]
                ball_types_count[j] = ball_types_count[j + 1]
                ball_types_count[j + 1] = temp

    for i in range(n):
        if container_capacities[i] != ball_types_count[i]:
            return "Impossible"
            
    return "Possible"
