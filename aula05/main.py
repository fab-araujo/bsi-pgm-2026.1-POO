from rpg.personagem import Personagem
from rpg.monstro import Monstro
from rpg.guerreiro import Guerreiro
from rpg.mago import Mago
from rpg.arqueiro import Arqueiro


def apresentar(p: Personagem) -> None:
    """Demonstra polimorfismo: a função aceita qualquer Personagem.

    O parâmetro está tipado como Personagem, mas funciona para Guerreiro,
    Mago e Arqueiro — cada subclasse É-UM Personagem. Esse é o coração
    do que a Aula 6 vai aprofundar.
    """
    print(f"  {p.nome} é instância de {type(p).__name__}")
    p.mostrar_status()


def combate(atacante, defensor) -> None:
    """Roda um combate em turnos até um dos dois morrer."""
    print(f"\n{'='*60}")
    print(f"  BATALHA: {atacante.nome} vs {defensor.nome}")
    print(f"{'='*60}")
    turno = 1
    while atacante.esta_vivo() and defensor.esta_vivo():
        print(f"\n  Turno {turno}")
        dano = atacante.atacar(defensor)
        print(f"    {atacante.nome} → {defensor.nome}: {dano} de dano | "
              f"vida do alvo: {defensor.vida}")
        if defensor.esta_vivo():
            dano = defensor.atacar(atacante)
            print(f"    {defensor.nome} → {atacante.nome}: {dano} de dano | "
                  f"vida do alvo: {atacante.vida}")
        turno += 1

    vencedor = atacante if atacante.esta_vivo() else defensor
    print(f"\n  Vencedor: {vencedor.nome}")


if __name__ == "__main__":
    # Os três herdeiros — cada um com seu padrão de override
    guerreiro = Guerreiro("Boromir", vida=120, forca=22)
    mago = Mago("Gandalf", vida=80, forca=18, mana=100)
    arqueiro = Arqueiro("Legolas", vida=90, forca=20, flechas=20)

    print("=== Estado inicial das três classes ===")
    for personagem in [guerreiro, mago, arqueiro]:
        apresentar(personagem)

    # Cada um luta contra um monstro fresco — Goblin de força modesta
    # para a diferença entre os três padrões ficar visível na duração
    # do combate (Guerreiro vence em poucos turnos; Arqueiro também,
    # mas só enquanto tiver flechas; Mago vence somando duas camadas
    # de dano por turno).
    for personagem in [guerreiro, mago, arqueiro]:
        goblin = Monstro("Goblin", vida=50, forca=8, tipo="humanoide")
        combate(personagem, goblin)
