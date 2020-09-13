# coding: utf-8
def romanize(number):
    pairs = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    if number <= 0:
        raise ValueError("Romans didn't know of 0s and negative numbers")
    if number >= 3999:
        raise ValueError(f"{number} you ask to much")

    tokens = {n: l for n, l in pairs}
    if number in tokens:
        return tokens[number]

    counter = {}
    for value, literal in pairs:
        n = number // value
        if literal not in counter:
            counter[literal] = 0
        counter[literal] += n
        number -= n * value
    res = ""
    for literal, n in counter.items():
        res += literal * n
    return res
