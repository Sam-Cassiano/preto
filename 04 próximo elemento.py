# Sequências
# a) 1, 3, 5, 7, ___
sequencia_a = [1, 3, 5, 7]
sequencia_a.append(sequencia_a[-1] + 2)
print(f"a) {sequencia_a}")

# b) 2, 4, 8, 16, 32, 64, ____
sequencia_b = [2, 4, 8, 16, 32, 64]
sequencia_b.append(sequencia_b[-1] * 2)
print(f"b) {sequencia_b}")

# c) 0, 1, 4, 9, 16, 25, 36, ____
sequencia_c = [0, 1, 4, 9, 16, 25, 36]
sequencia_c.append((len(sequencia_c)) ** 2)
print(f"c) {sequencia_c}")

# d) 4, 16, 36, 64, ____
sequencia_d = [4, 16, 36, 64]
sequencia_d.append((len(sequencia_d) * 2) ** 2)
print(f"d) {sequencia_d}")

# e) 1, 1, 2, 3, 5, 8, ____
sequencia_e = [1, 1, 2, 3, 5, 8]
sequencia_e.append(sequencia_e[-1] + sequencia_e[-2])
print(f"e) {sequencia_e}")

# f) 2,10, 12, 16, 17, 18, 19, ____
sequencia_f = [2, 10, 12, 16, 17, 18, 19]
sequencia_f.append(20)
print(f"f) {sequencia_f}")
