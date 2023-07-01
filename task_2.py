# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента.
# (речь идет про **kwargs)


def keyword_arguments(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result[value] = key
    return result

arguments_dict = keyword_arguments(a=1, b=2, c=3)
print(arguments_dict)
