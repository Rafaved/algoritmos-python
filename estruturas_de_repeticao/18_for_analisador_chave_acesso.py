"""
Arquivo: 18_for_analisador_chave_acesso.py

Desafio 02 (Bloco 1 - FOR com Strings): Analisador de Chave de Acesso
Objetivo: Percorrer uma string caractere por caractere para auditar a composição de uma chave de segurança e classificar seu nível de força.

Regras de Negócio:
1. O sistema deve solicitar ao usuário que digite uma chave de acesso (texto).
2. Caso a chave tenha menos de 8 caracteres, o sistema deve exibir "Chave inválida: mínimo de 8 caracteres." e encerrar sem analisar.
3. Se o tamanho for válido, o sistema deve percorrer a chave caractere por caractere e contabilizar separadamente:
   - Quantidade de letras maiúsculas.
   - Quantidade de letras minúsculas.
   - Quantidade de dígitos numéricos.
   - Quantidade de caracteres especiais (qualquer caractere que não seja letra nem número).
4. Ao final da análise, o sistema deve exibir o total encontrado em cada uma das 4 categorias.
5. Por fim, o sistema deve classificar a chave como:
   - "Chave Forte": se possuir pelo menos 1 letra maiúscula, 1 letra minúscula, 1 número e 1 caractere especial.
   - "Chave Fraca": caso falte qualquer um desses 4 requisitos.
"""

chave_acesso = input("Digite uma chave de acesso:")
maiuscula = 0
minuscula = 0
numeros = 0
especiais = 0

if len(chave_acesso) < 8:
    print("Chave inválida: mínimo de 8 caracteres.")
else:
    for l in chave_acesso:
        if l.isupper():
            maiuscula += 1
        elif l.islower():
            minuscula += 1
        elif l.isdigit():
            numeros +=1
        else:
            especiais +=1
    if maiuscula >= 1 and minuscula >= 1 and numeros >= 1 and especiais >= 1:
            print("Chave forte")
    else:
            print("Chave fraca")   
    print(f"- Quantidade de letras maiúsculas. {maiuscula}\n- Quantidade de letras minúsculas.{minuscula}\n- Quantidade de dígitos numéricos.{numeros}\n- Quantidade de caracteres especiais.{especiais}")
            
    

 