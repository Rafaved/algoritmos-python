"""
Desafio 19: Simulador de Combate Turno (RPG)
Objetivo: Determinar o resultado de um ataque com base em rolagem de dados.
Regras de Negócio:
- Entrada: Ataque do Jogador, Defesa do Inimigo e Rolagem de Dado (1 a 20).
- Se Dado = 1: Falha Crítica (Errou o ataque).
- Se Dado = 20: Acerto Crítico (Ignora a defesa).
- Casos normais: Se (Ataque + Dado) for maior que a Defesa, ataque bem-sucedido. Caso contrário, bloqueado.
"""
import random 

dado = random.randint(1, 20)
print(f"O dado rolou e caiu no número: {dado}")
ataque = int(input("Qual o ataque do seu personagem: "))
defesa = int(input("Qual a defesa do seu personagem: "))
vida = int(input("Digite a vida do seu inimigo: "))
dano = 0

if dado == 1:
    print("Falha Crítica (Errou o ataque).")
elif dado == 20:
    vida = vida - (ataque + dado)
    print("Acerto Crítico (Ignora a defesa), a vida do inimigo ficou em {vida}")
elif (ataque + dado) > defesa:
    vida = vida - ((ataque + dado) - defesa)
    print(f"ataque acertou! Deixando o inimigo com {vida} de vida")
else:
    print("Defesa do inimigo é forte de mais, seu dano junto com o dado não causou efeitos!")
