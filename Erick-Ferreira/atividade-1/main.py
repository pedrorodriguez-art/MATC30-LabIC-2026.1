def get_and_validate_user_input():
    is_valid_input = False

    while not is_valid_input:
        a = int(input("a: "))
        b = int(input("b: "))

        if a < 1 or a > 1000:
            print("Valor de a deve estar entre 1 e 1000")
            continue

        if b < 1 or b > 1000:
            print("Valor de b deve estar entre 1 e 1000")
            continue

        is_valid_input = True

    return a, b 


if __name__=="__main__":
    a, b = get_and_validate_user_input()
    total = a + b
    print(total)


