import numpy as np

hours = np.arange(0, 24, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)
print("hours =", hours)
print("shape, ndim, size, dtype:", hours.shape, hours.ndim, hours.size, hours.dtype)

print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй:", hours[::2])
print("Обратный порядок:", hours[::-1])

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print("shape, ndim, size:", temperatures.shape, temperatures.ndim, temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:", temperatures[:2, 1:])
print("Центральный фрагмент:", temperatures[:2, 1:3])

matrix = np.arange(1, 26).reshape(5, 5)
for label, fragment in [
    ("Первые три строки", matrix[:3]),
    ("Последние две строки", matrix[-2:]),
    ("Первые два столбца", matrix[:, :2]),
    ("Строки 1–3, столбцы 2–4", matrix[1:4, 2:5]),
    ("Правый нижний угол", matrix[-2:, -2:]),
]:
    print(label, fragment, sep="\n")
    print("shape:", fragment.shape)

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print("changed_hours =", changed_hours)
print("hours =", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print("changed_matrix =", changed_matrix, sep="\n")
print("matrix =", matrix, sep="\n")

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T
print("numbers.shape =", numbers.shape)
print("table.shape =", table.shape)
print("transposed.shape =", transposed.shape)
