# Задача 42: Узнать какая максимальная households
# в зоне минимального значения population.

# Cначала находим минимальное значение population с помощью
# метода min().Затем фильтруем данные, чтобы получить только
# строки, где значение population равно минимальному значению, и
# из этих строк выбираем максимальное значение households
# с помощью  метода max().

import pandas as pd

data = pd.read_csv('california_housing_test.csv')

min_population = data['population'].min()
max_households = data[data['population'] == min_population]['households'].max()

print("Максимальное количество households в зоне минимального значения population:", max_households)
