"""Игра угадай число. 
Компьютер сам загадывает и угадывает число
"""
import numpy as np
def random_predict(number: int=1) ->int:
    """рандомно угадываем число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return(count)


def score_game(random_predict) ->int:
    """за какое кличество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
        
    """
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'ваш алгоритм угадывает в среднем за {score} попыток')
    return(score) 
if __name__ == '__mane__':  
    score_game(random_predict) 

