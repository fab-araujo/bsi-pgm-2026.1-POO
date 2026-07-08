from rpg.mago import Mago
from rpg.monstros import Goblin
from rpg.efeito import Efeito


if __name__ == "__main__":
    # Aula 11: Efeito é uma @dataclass e o Mago aplica queimadura ao atacar.
    # O programa roda do início ao fim SEM traceback.

    print("=== 1. Efeito é uma dataclass ===")
    # repr e == gerados automaticamente pelo @dataclass.
    queima = Efeito("Queimadura", -5, 3)
    print(f"  repr gerado: {queima!r}")
    print(f"  == gerado:   {Efeito('Queimadura', -5, 3) == queima}")

    print("\n=== 2. O ataque do Mago deixa uma queimadura no alvo ===")
    mago = Mago("Gandalf", 80, 15)
    alvo = Goblin(vida=100)
    dano = mago.atacar(alvo)
    print(f"  {mago.nome} atacou causando {dano} — alvo com {alvo.vida} de vida")
    print(f"  efeitos ativos no alvo: {alvo.efeitos_ativos}")

    print("\n=== 3. aplicar reduz a vida de quem está vivo ===")
    vivo = Goblin(vida=100)
    print(f"  antes:  vida = {vivo.vida}")
    Efeito("Queimadura", -5, 3).aplicar(vivo)
    print(f"  depois: vida = {vivo.vida}   (perdeu 5 de vida)")

    print("\n=== 4. aplicar NÃO afeta um combatente morto ===")
    morto = Goblin(vida=5)
    morto.receber_dano(5)                  # vida vai a 0
    Efeito("Regeneração", +10, 2).aplicar(morto)
    print(f"  regeneração em morto → vida = {morto.vida}   (não ressuscita)")

    print("\nFim da demonstração.")
