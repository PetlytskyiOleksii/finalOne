from functools import reduce

users = [
    {
        "name": "Lesha",
        "age": 31,
        "salary": 1500,
        "hasBonus": True
    },
    {
        "name": "Andrey",
        "age": 23,
        "salary": 1200,
        "hasBonus": False
    },
    {
        "name": "Oleg2",
        "age": 18,
        "salary": 1400,
        "hasBonus": True
    }
]
# 1 Посчитать сколько в сумме получают пользователи, возраст которых больше 20
# salary = 0
# for person in users:
#     if person["age"] > 20:
#         salary += person["salary"]
# print(salary)

# 1.1 reduce
# salaries = reduce(lambda sum_salary, user: sum_salary + user["salary"], filter(lambda user: user["age"] > 20, users), 0)
# print(salaries)


# 2 Преобразовать этот список в список строк вида "Lesha earns 1500$"
# new_list = []
# for person in users:
#     new_list.append(person["name"] + " earns " + str(person["salary"]))
# print(new_list)

# 2.1
# new_list = list(map(lambda user: user["name"] + " earns " + str(user["salary"]), users))
# print(new_list)

# 3. Преобразовать текущий список в новый список пользователей, каждый элемент которого состоит из 2 полей: name, salary
# Если у пользователя есть бонус, то его зарплата должна быть увеличена на 20%, иначе она должна остаться без изменений
# new_list = []
# for person in users:
#     new_list.append({"name": person["name"], "salary": person["salary"] * 1.2 if person["hasBonus"] else person["salary"]})
# print(new_list)

# 3.1
# new_list = map(lambda person: {"name": person["name"], "salary": person["salary"] * 1.2}, filter(lambda person: person["hasBonus"], users))
# print(list(new_list))


# test = reduce(lambda sum_salary, user: sum_salary + user["salary"], filter(lambda user: user["name"] == 'Oleg2', users), 0)
# print(test)
# можно ли решить эту задачу без filter???


test = reduce(lambda sum_salary, user: sum_salary + user["salary"] if user["name"] == 'Oleg2' else sum_salary, users, 0)