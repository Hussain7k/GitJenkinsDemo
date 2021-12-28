data = 2, -3, 1, 4, 5, -6, 10, -2

lm = list(filter(lambda x: abs(x)>3, data))

print(lm)