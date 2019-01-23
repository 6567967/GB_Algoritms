# 1. Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple
from collections import deque
from collections import defaultdict
import random

def get_enterprise_data_strings(numb: int=0) -> tuple:
    _enterprise_string = input(f"Введите наименование предприятия {numb} "
                               "и прибыль по четвертям(csv): ")
    # _enterprise_string = f'Microsoft{random.randint(0, 9)}, ' \
    #     f'{random.randint(0, 5)}, 2, 3, 4'
    return tuple(map(str.strip, _enterprise_string.split(',')))


quarters = ['q1', 'q2', 'q3', 'q4']
Year: namedtuple = namedtuple('Year', quarters)

Enterprise:namedtuple = namedtuple('Enterprise', ['name', 'year'])
# year1 = Year(q1=10, q2=20, q3=30, q4=40)
# ent1 = Enterprise('Microsoft', year=year1)
# print(ent1)
# spam = deque(get_enterprise_data_strings())
# name = spam.popleft()
# print(name, Year(*spam))
# print(tuple(map(int, spam)))
# year1 = Year(*tuple(map(int, spam)))
# print(year1)

# ent1 = Enterprise(spam.popleft(), Year(*tuple(map(int, spam))))
# ent1 = Enterprise(spam.popleft(), Year(*tuple(map(float, spam))))
# print(ent1)

def enterprise_average_profit(ent: Enterprise) -> float:
    total_profit: float = 0
    for quarter in quarters:
        total_profit += getattr(ent.year, quarter)
    return total_profit / len(quarters)

# print(enterprise_average_profit(ent1))
#
# exit()
enterprises = deque()
total_average_profit: float = 0
for _ in range(int(input("Введите количество предприятий: "))):
    spam = deque(get_enterprise_data_strings(_ + 1))
    eggs = Enterprise(spam.popleft(), Year(*tuple(map(float, spam))))
    enterprises.append(eggs)
    ent_avg = enterprise_average_profit(eggs)
    total_average_profit = \
        (total_average_profit * (len(enterprises)-1) + ent_avg) \
        / (len(enterprises))
    # print(eggs, enterprise_average_profit(eggs), total_average_profit)
print("Total average profit =", total_average_profit)

leaders = list()
outsiders = list()

for ent in enterprises:
    avg = enterprise_average_profit(ent)
    if avg < total_average_profit:
        outsiders.append(ent.name)
        # print(f"{ent.name} аутсайдер ({avg}<{total_average_profit})")
    elif avg>total_average_profit:
        leaders.append(ent.name)
        # print(f"{ent.name} лидер ({avg}>{total_average_profit})")
    else:
        print(f"{ent.name} ни то ни сё ({avg}={total_average_profit})")

print("лидеры: ", *leaders)
print("аутсайдеры: ", *outsiders)

# 5
# a,1,2,3,4
# b,2,3,4,5
# c,3,4,5,6
# d,5,3 ,2, 0
# e,7, 5, 3, 3
