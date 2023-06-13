# Задача 40: Работать с файлом california_housing_train.csv,
# который находится в папке sample_data. Определить среднюю
# стоимость дома, где кол-во людей от 0 до 500 (population).

# Используем метод .loc для фильтрации данных, где значение
# столбца 'population' находится в диапазоне от 0 до 500.
# Затем мы вычисляем среднее значение столбца 'median_house_value'
# для отфильтрованных данных и выводим результат.

import pandas as pd

data = pd.read_csv('california_housing_test.csv')

average_price = data.loc[(data['population'] >= 0) & (data['population'] <= 500), 'median_house_value'].mean()

print("Средняя стоимость дома для домов с количеством людей от 0 до 500:", average_price)

