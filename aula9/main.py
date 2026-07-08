from rpg.guerreiro import Guerreiro
from rpg.monstros import Goblin
from rpg.combate import Combate
from rpg.exceptions import XPInvalidoError


if __name__ == "__main__":
    # Aula 9: as três properties de Personagem, cada uma com sua estratégia
    # de setter (clamp / ValueError / XPInvalidoError), e o XP no combate.
    # O programa roda do início ao fim SEM traceback.

    print("=== 1. Validação da vida (clamp) ===")
    g = Guerreiro("Boromir", 100, 20)      # vida_maxima = 100
    g.vida = -50
    print(f"  vida = -50  →  {g.vida}   (piso 0)")
    g.vida = 999
    print(f"  vida = 999  →  {g.vida}   (teto vida_maxima = {g.vida_maxima})")

    print("\n=== 2. Validação do nível (ValueError) ===")
    try:
        g.nivel = 0
    except ValueError as erro:
        print(f"  nível inválido barrado: {erro}")

    print("\n=== 3. Validação do XP (XPInvalidoError) + subida de nível ===")
    g.ganhar_xp(120)                       # imprime a subida para o nível 2
    print(f"  após ganhar 120 XP  →  xp = {g.xp}, nível = {g.nivel}")
    try:
        g.xp = 50                          # tentar regredir de 120 para 50
    except XPInvalidoError as erro:
        print(f"  regressão de XP barrada: {erro}")

    print("\n=== 4. Combate que dá XP ===")
    heroi = Guerreiro("Aragorn", 100, 20)
    print("  antes: ", end="")
    heroi.mostrar_status()
    Combate(heroi, Goblin()).lutar()       # Goblin nível 1 → 50 XP ao vencer
    print("  depois: ", end="")
    heroi.mostrar_status()

    print("\nFim da demonstração.")
