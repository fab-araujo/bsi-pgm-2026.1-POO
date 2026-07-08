from personagem import Personagem
from monstro import Monstro


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
    heroi = Personagem("Aragorn", vida=100, ataque=20, defesa=10)
    goblin = Monstro("Goblin", vida=50, ataque=15, defesa=5, tipo="humanoide")

    print(heroi)
    print(goblin)

    combate(heroi, goblin)
