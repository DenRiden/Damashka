def check_numbers(input_list):
    if len(set(input_list)) == 1:
        return "Все числа равны"
    elif len(set(input_list)) == len(input_list):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"
