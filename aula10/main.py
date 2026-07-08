from rpg.personagem import Personagem
from rpg.guerreiro import Guerreiro
from rpg.monstros import Goblin


if __name__ == "__main__":
    # Aula 10: Personagem virou classe abstrata (ABC), o id de domínio
    # dá identidade a cada herói e os métodos mágicos definem str/repr/
    # igualdade/hash. O programa roda do início ao fim SEM traceback.

    print("=== 1. Personagem é abstrato ===")
    # Instanciar Personagem direto falha — golpe_especial é abstrato.
    try:
        Personagem("Genérico", 100, 10)
    except TypeError as erro:
        print(f"  Não dá para criar um Personagem genérico: {erro}")

    print("\n=== 2. Igualdade pelo id de domínio ===")
    a = Guerreiro("Boromir", 100, 20)
    b = Guerreiro("Boromir", 100, 20)      # mesmo nome e classe, herói diferente
    print(f"  a = {a!r}")
    print(f"  b = {b!r}")
    print(f"  a == a  →  {a == a}   (um personagem é igual a si mesmo)")
    print(f"  a == b  →  {a == b}   (ids diferentes → heróis diferentes)")
    print(f"  str(a)  →  {a}")

    print("\n=== 3. set não funde personagens distintos ===")
    equipe = {a, a, b}                      # 'a' repetido + 'b'
    print(f"  {{a, a, b}} tem {len(equipe)} elementos (descartou só a repetição de 'a')")

    print("\n=== 4. golpe_especial (contrato cumprido pela subclasse) ===")
    alvo = Goblin(vida=1000)
    dano = a.golpe_especial(alvo)
    print(f"  {a.nome} usou o Golpe Brutal: {dano} de dano (alvo com {alvo.vida} de vida)")

    print("\nFim da demonstração.")
