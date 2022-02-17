# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Задание 1

# Даны две строки: `s1` и `s2` с одинаковым размером.
#
# Проверьте, может ли некоторая перестановка строки `s1` “победить” некоторую перестановку строки `s2` или наоборот.
#
# Строка x может “победить” строку y (обе имеют размер n), если `x[i] >= y[i]` (в алфавитном порядке) для всех i от 0 до n-1.
#

# ## Ввод

# `abc`
# `xya`

# ## Вывод

# `True`
#
# ### Исполняемый код записать в ячейку ниже:
def ex1(s1: str, s2: str) -> bool:
    l1 = list(s1)
    l2 = list(s2)

    l1.sort()
    l2.sort()

    if l1[0] <= l2[0]:
        for i, letter in enumerate(l1[1:]):
            if letter > l2[i+1]:
                return False
    else:
        for i, letter in enumerate(l1[1:]):
            if letter < l2[i+1]:
                return False

    return True


tests: tuple[tuple[tuple[str, str], bool], ...] = tuple([
    (("abc", "xya"), True),
])
for test in tests:
    res: bool = ex1(*test[0])
    assert res == test[1]
print("All tests passed")

# # Задание 2

# Дана строка `s`, вернуть самую длинную полиндромную подстроку в `s`.

# ## Ввод

# `babad`

# ## Вывод

# `aba` или `bab`

# ## Исполняемый код записывать в ячейку ниже
from typing import Union


def ex2(s: str) -> Union[str, None]:
    print(f"In: {s}")
    r, i = manacher(s)

    res: Union[str, None] = s[i-r:i+r-1] if r != 1 else None
    print(f"{r=}, {i=}, {res=}")

    return res

def manacher(s: str) -> tuple[int, int]:
    s = "^&" + "&".join(s) + "&$"
    n: int = len(s)
    radiuses: list[int] = [0] * n
    max_len: int = 0
    max_len_index: int = 0
    l: int = 0
    r: int = 0

    for i in range(1, n - 1):
        radiuses[i] = max(0, min(r - i, radiuses[l + (r - i)]))
        while s[i - radiuses[i]] == s[i + radiuses[i]]:
            radiuses[i] += 1
        if radiuses[i] > max_len:
            max_len = radiuses[i]
            max_len_index = i
        if i + radiuses[i] > r:
            l = i - radiuses[i]
            r = i + radiuses[i]

    print(f"{radiuses=}")
    return tuple((max_len // 2, max_len_index // 2))


ex2("babad")
# # Задание 3

# Вернуть количество отдельных непустых подстрок текста, которые могут быть записаны как конкатенация некоторой строки с самой собой (т.е. она может быть записана, как `a + a`, где `a` - некоторая строка).

# ## Ввод

# `aabb`

# ## Вывод

# 2

# ## Исполняемый код записывать в ячейку ниже
def ex3(s: str) -> int:
    n: int = len(s)
    res: set[str] = set()

    for i in range(1, n):
        for j in range(i // 2 + 1, i + 1):
            r = i + 1 - j

            left_substr = s[j-r:j]
            right_substr = s[j:j+r]

            if left_substr == right_substr:
                res.add(right_substr)

    return len(res)

print(f"{ex3('abcabcabc')=}")
