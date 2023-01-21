import numpy as np
"""Игра угадай число не более чем за 20 попыток

"""

def game_v3(number: int = 1) -> int:
    """
Компьютер сам загадывает и сам угадывает число за количество попыток не более 20

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min = 1 # нижняя граница
    max = 101 # верхняя граница
    predict_number = np.random.randint(1, 101)  # предполагаемое число, начинаем cо случайного числа
    
    while True:
        count += 1
        if number > predict_number:
            min = predict_number
            predict_number = max - (max - min)//2
        elif number < predict_number:
            max = predict_number
            predict_number = min + (max - min)//2
        else:
            break  # выход из цикла если угадали

    return count


def score_game(random_predict) ->int:
    """за какое кличество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
        
    """
    
    count_ls = []
    #np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))# загадали список чисел 

    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'ваш алгоритм угадывает в среднем за {score} попыток')
    return(score) 
# RUN
if __name__ == '__mane__':  
    score_game(game_v3)






