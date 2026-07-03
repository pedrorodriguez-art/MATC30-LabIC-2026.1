def get_and_validate_user_input():
    is_valid_input = False
    numbers = []

    while not is_valid_input:
        n = int(input())
        input_items = input().split()
        for i in range(n):
            number = int(input_items[i])
            numbers.append(number)

        is_valid_input = True

    return numbers

def sum_arr_elements(numbers: list[int]):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return sum

if __name__=="__main__":
    numbers = get_and_validate_user_input()
    total = sum_arr_elements(numbers)
    print(total)