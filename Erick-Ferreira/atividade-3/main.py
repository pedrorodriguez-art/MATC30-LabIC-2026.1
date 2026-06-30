def get_and_validate_user_input():
    is_valid_input = False
    words = []
    while not is_valid_input:
        t = int(input())
        if t < 1 or t > 10000:
            print("Valor de t deve estar entre 1 e 10000")
            continue

        has_invalid_word = False
        for i in range(t):
            word = input()
            if len(word) < 1 or len(word) > 10000:
                print("Tamanho da palavra deve estar entre 1 e 100")
                has_invalid_word = True
                break

            if not word.isalpha():
                print("Palavra deve conter apenas letras")
                has_invalid_word = True
                break

            words.append(word)

        if has_invalid_word:
            continue

        is_valid_input = True
    return words

def permute(text: str):
    if len(text) <= 1 or has_same_chars(text):
        return [text]

    permutation_list = []

    for i, curr_char in enumerate(text):
        tail = text[:i] + text[i + 1:]

        for sub_permutation in permute(tail):
            permutation_list.append(curr_char + sub_permutation)

    return permutation_list

def has_same_chars(text: str):
    return text.count(text[0]) == len(text)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    sorted_array = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

def remove_duplicates(sorted_arr):
    if len(sorted_arr) == 1:
        return sorted_arr

    unique_list = [sorted_arr[0]]
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] != sorted_arr[i - 1]:
            unique_list.append(sorted_arr[i])

    return unique_list

if __name__=="__main__":
    words = get_and_validate_user_input()
    for word in words:
        permutations = permute(word)
        sorted_permutations = merge_sort(permutations)
        unique_permutations = remove_duplicates(sorted_permutations)

        unique_permutations_size = len(unique_permutations)
        if unique_permutations_size == 1:
            print("no answer")
            continue

        word_position = 0
        for i in range(unique_permutations_size):
            if unique_permutations[i] == word:
                word_position = i
                break

        if word_position == unique_permutations_size - 1:
            print("no answer")
            continue

        print(unique_permutations[word_position + 1])