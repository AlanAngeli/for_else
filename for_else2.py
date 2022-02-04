"""

For/Else


"""

var = ["Alan", "Paulo", "Anna", "Maria", "Adolfo"]


for valor in var:
    if valor.lower().startswith("a"):#Serve tanto para letra maiúscula quanto para minúscula
        print("O nome",valor, "começa com A")
    else:
        print(valor, "não tem A")

