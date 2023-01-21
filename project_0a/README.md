# Проект 0а. Угадай число не более чем за 20 попыток

## Оглавление
1. [Описание проекта](https://github.com/Aemikh/ae_data_science/tree/main/project_0a/README.md/#Описание-проекта)
2. [Какой кейс решаем](https://github.com/Aemikh/ae_data_science/tree/main/project_0a/README.md/#Какой-кейс-решаем)
3. [Краткая информация о данных](https://github.com/Aemikh/ae_data_science/tree/main/project_0a/README.md/#Краткая-информация-о-данных)
4. [Этапы работы над проектом ](https://github.com/Aemikh/ae_data_science/tree/main/project_0a/README.md/#Этапы-работы-над-пректом)
5. [Результат](https://github.com/Aemikh/ae_data_science/tree/main/project_0a/README.md/#Результат)
7. [Выводы](https://github.com/Aemikh/ae_data_science/tree/main/project_0a/README.md/#Выводы)

### Описание проекта
Угадать загаданное компьютером число за минимальное количество попыток.

:arrow_up:[к оглавлению](https://github.com/Aemikh/ae_data_science/tree/main/project_0a/README.md/#Оглавление)


## Какой кейс решаем?:
Нужно написать программу, которая угадывает число не более чем за 20 попыток

**Условия соревнования:**
- Компьютер загадывает целое число от 1 до 100 и сам его угадывает. Под "угадать", подразумевается "написать программу, которая загадывает и угадывает число не более чем за 20 попыток".
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества:**
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем:**
Учимся писать хороший код на Python
Учимся работать с IDE
Учимся работать с GitHub


### Этапы работы над проектом: 
В ходе реализации проекта было опробован  алгоритм решения данной задачи:
Метод дихотомии - число вначале определялось случайным образом, далее для угадывания выбиралось равным примерно середине диапазона и каждый раз диапазон для угадывания уменьшался в два раза ([код](https://github.com/Aemikh/ae_data_science/tree/main/project_0a/game_v3.py)).


:arrow_up:[к оглавлению](https://github.com/Aemikh/ae_data_science/tree/main/project_0a/README.md/#Оглавление)

### Результаты:
По [результатам опробирования](https://github.com/Aemikh/ae_data_science/tree/main/project_0a/game_v3.ipynb) установлено:
Алгоритм, реализованный по методу дихотомии, в среднем угадывал число с 6 попытки. 

:arrow_up:[к оглавлению](https://github.com/Aemikh/ae_data_science/tree/main/project_0a/README.md/#Оглавление)

### Выводы:
Метод дихотомии позволяет угадывать число за количество попыток менее 20

:arrow_up:[к оглавлению](https://github.com/Aemikh/ae_data_science/tree/main/project_0a/README.md/#Оглавление)