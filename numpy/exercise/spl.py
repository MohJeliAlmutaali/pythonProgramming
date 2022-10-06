import numpy as np

def iter_input(row,input_row):
    for i in input_row:
        row.append(int(i))


input_row1 = input("Masukkan baris pertama: ").split(" ")
row1 = []
iter_input(row1,input_row1)

input_row2 = input("Masukkan baris kedua: ").split(" ")
row2 = []
iter_input(row2,input_row2)

input_row3 = input("Masukkan baris ketiga: ").split(" ")
row3 = []
iter_input(row3,input_row3)

input_equal = input("Masukkan persamaan: ").split(" ")
equal = []
iter_input(equal,input_equal)

rows = np.array([row1, row2, row3])
equal = np.array(equal)
result = np.linalg.solve(rows,equal)
print("X = ", result[0])
print("y = ", result[1])
print("Z = ", result[2])



