def contar_a(string):
    minusculas = string.count('a')
    maiusculas = string.count('A')
    
    total = minusculas + maiusculas

    if total > 0:
        print(f"A letra 'a' aparece {total} vez(es) no total.")
        print(f"Sendo {minusculas} minúscula(s) e {maiusculas} maiúscula(s).")
    else:
        print("A letra 'a' não aparece na string.")

# Informe a string
string = input("Informe uma string: ")
contar_a(string)
