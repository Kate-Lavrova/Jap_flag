def flag(N): # 8 requirement
    ''' The function takes the parameter N and outputs a string 
        with an ASCII art of the japanese flag.'''

    width_without_border = 3 * N  
    width_with_border = 3 * N + 2
    vertical_distance = N // 2 

    rectangle_border = ['#' * width_with_border]

    empty_area = []
    for i in range(vertical_distance):
        line = '#' + " " * width_without_border + '#'
        empty_area.append(line)

    l_f = (width_without_border // 2) - 1
    l_s = (width_without_border // 2) - 1
    
    circle_area = []
    for i in range(vertical_distance):
        circle = '*' + "o" * i * 2 + '*'
        l_s -= 1
        line = '#' + " " * l_f + circle + " " * l_s + ' ' + '#'
        l_f  -= 1
        circle_area.append(line)
    
    first_array = rectangle_border + empty_area + circle_area
    second_array = first_array[:]
    second_array.reverse()
    general_array = first_array + second_array

    # 7 requirement 
    japanese_flag = '\n'.join(general_array)    
    return japanese_flag

prompt = "Введите значение N = "
N = input (prompt)

# Исключение ValueError vs ArgumentError в данном случае также обрабатывает 
# ситуацию при вводе значения N, отличного от целого четного числа. 
try:
    # 1 requirement 
    N = int(N)
    if N % 2 == 0:
        jap_flag = flag(N)
        print (jap_flag)
    elif N % 2 == 1:
        print ('Введенное значение должно быть четным числом')
except ValueError:
    print ('Неверный формат ввода. Введенное значение должно быть целым числом')