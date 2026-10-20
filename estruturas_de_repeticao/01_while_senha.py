cadastro = input("Digite a senha correta cadastrada: ")

while cadastro != "python123":
    print(f"A senha {cadastro} está errada!!! Digite novamente.")
    cadastro = input("Digite a senha correta cadastrada: ")
print("Senha correta!!")