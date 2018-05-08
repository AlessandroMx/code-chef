def main_logic(text):
    char_dict = {}
    for char in text:
        if char not in char_dict:
            char_dict.update({char: 1})
        else:
            char_dict[char] += 1
    count = 0
    total = 0
    first_value = 0
    for key, value in char_dict.items():
        if count == 0:
            first_value = value
        else:
            total += value
        count += 1
    msg = 'Dynamic' if total == first_value or len(char_dict) < 3 else 'Not'
    print(msg)


def control_logic(num_cases):
    for n in range(num_cases):
        main_logic(input())


if __name__ == '__main__':
    number_test_cases = int(input())
    control_logic(number_test_cases)
