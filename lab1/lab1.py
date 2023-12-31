import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('dataset/forestfires.csv', delimiter=',')
numbers = ['X','Y','FFMC','DMC','DC','ISI','temp','RH','wind','rain','area']
cat = ['month','day']


# Найти характеристики данных:
# для числовых переменных:
n = data[numbers]
# c = data[cat]

# #  минимальное
# #  максимальное;
# #  среднее;
# #  квартили: 25%, 50% (медиана), 75%;
# #  стандартное отклонение;
chars = data.describe().to_string()
# #  дисперсия;
var = n.var().to_string()

cat_columns = data.select_dtypes(['object']).columns
# смотрим столбцы
# tmpDay = pd.factorize(data['day'])
# tmpM = pd.factorize(data['month'])

c = data[cat_columns].apply ( lambda x: pd.factorize (x)[ 0 ])
cList = cat_columns.to_list()
cMin = c.min().to_string()
cMax = c.max().to_string()
сMode = c.mode().to_string()

plt.boxplot(x=data['Y'])
plt.savefig('out/boxplot2.2_Y.png')

plt.boxplot(data['X'])
plt.savefig('out/boxplot2.2_X.png')

with open('out/out.md', 'w') as f:
    f.write(f"""
### 2.1 характеристики данных:
#### для числовых переменных:
{chars}
квартиль - значение, которое заданная случайная величина не превышает с фиксированной вероятностью
Мо́да — одно или несколько значений во множестве наблюдений, которое встречается наиболее часто 
##### Выводы:
75% пожаров пожаров происходят не дальше (7,5) по (X,Y)
Разброс замеров температуры от мат ожидания составляет 5.8 градусов

дисперсия:
{var}

#### для категориальных переменных ({cList}):
'fri', 'tue', 'sat', 'sun', 'mon', 'wed', 'thu'
0       1       2       3     4     5       6 
пт      вт      сб      вс  пн      ср      чт

'mar' - 0
'oct' - 1
'aug' - 2
'sep' - 3
'apr' - 4
'jun' - 5
'jul' - 6
'feb' - 7
'jan' - 8
'dec' - 9
'may' - 10
'nov' - 11

минимальное:
{cMin}

максимальное:
{cMax}

мода:
{сMode}

Выводы:
Пожары происходят наиболее часто в августе в субботу

2.2
Ящик с усами (box plot)

Ящик с усами, он же диаграмма размаха, можно сравнить с плотностью распределения.
Он тоже показывает диапазон значений, лежащих около среднего.
Помимо прочего, с его помощью можно определить выбросы — те данные, которые находятся далеко от среднего.
Удаление выбросов является важным шагом подготовки модели машинного обучения. В matplotlib ящик с усами называется boxplot:

### 2.3 Выводы:
- 75% пожаров пожаров происходят не дальше (7,5) по (X,Y)
- Разброс замеров температуры от мат ожидания составляет 5.8 градусов
- Пожары происходят наиболее часто в августе в субботу
##### по усам:
- средние X > Y - пожары были в основном вытянутой формы
- выбросы по X входят в дисперсию
- разброс между .25 и .75 по X > Y
""")



# X,Y,month,day,FFMC,DMC,DC,ISI,temp,RH,wind,rain,area
# 'X',
# 'Y',
# 'FFMC',
# 'DMC',
# 'DC',
# 'ISI',
# 'temp',
# 'RH',
# 'wind',
# 'rain',
# 'area',

# 'month',
# 'day',

# 
# X
# Y
# month
# day
# FFMC
# DMC
# DC
# ISI
# temp
# RH
# wind
# rain
# area