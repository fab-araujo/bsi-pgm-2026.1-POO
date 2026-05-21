from rpg.personagem import Personagem
from rpg.monstro import Monstro
from rpg.item import Item


def combate(atacante, defensor) -> None:
    """Roda um combate em turnos até um dos dois morrer."""
    print(f"\n{'='*50}")
    print(f"  BATALHA: {atacante.nome} vs {defensor.nome}")
    print(f"{'='*50}")
    turno = 1
    while atacante.esta_vivo() and defensor.esta_vivo():
        print(f"\n  Turno {turno}")
        dano = atacante.atacar(defensor)
        print(f"    {atacante.nome} → {defensor.nome}: {dano} de dano | vida: {defensor.vida}")
        if defensor.esta_vivo():
            dano = defensor.atacar(atacante)
            print(f"    {defensor.nome} → {atacante.nome}: {dano} de dano | vida: {atacante.vida}")
        turno += 1

    vencedor = atacante if atacante.esta_vivo() else defensor
    print(f"\n  Vencedor: {vencedor.nome}")


if __name__ == "__main__":
    # Criação dos personagens — inventário já começa com Poção de Vida
    heroi = Personagem("Aragorn", vida=100, ataque=20, defesa=10)
    monstro = Monstro("Goblin", vida=50, ataque=15, defesa=5, tipo="humanoide")

    print("=== Estado inicial ===")
    print(heroi)
    print(monstro)

    # Demonstra inventário e @staticmethod
    heroi.inventario.adicionar(Item("Espada de Ferro", "arma", 15))
    heroi.inventario.adicionar(Item("Escudo de Madeira", "armadura", 5))
    print(f"\nApós equipar: {heroi.inventario}")
    print(f"Dano bruto (staticmethod): {Personagem.calcular_dano(heroi.ataque, monstro.defesa)}")

    # Usa um item antes de combater
    heroi.usar_item("Poção de Vida")

    combate(heroi, monstro)
