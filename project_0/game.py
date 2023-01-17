import numpy as np
number = np.random.randint(1, 101)
count = 0
while True:
    count += 1
    predict_number = int(input('predict number from 1 to 100:   1'))
    
    if predict_number > number:
        print('number should be less')
    elif predict_number < number:
        print('number should be more')
    else:
        print(f'your prediction was right! It is {number} for {count} attemps')
        break        