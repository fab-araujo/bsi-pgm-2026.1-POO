import random

# Personagens representados como dicionários
heroi = {
    "nome": "Aragorn",
    "vida": 100,
    "ataque": 20,
    "defesa": 10,
    "inventario": ["Poção de Vida", "Poção de Vida", "Elixir"]
}

monstro = {
    "nome": "Goblin Chefe",
    "vida": 80,
    "ataque": 15,
    "defesa": 5,
    "inventario": []
}


def exibir_status(personagem):
    """Imprime os atributos e inventário do personagem."""
    print(f"  {personagem['nome']} | "
          f"Vida: {personagem['vida']} | "
          f"Ataque: {personagem['ataque']} | "
          f"Defesa: {personagem['defesa']}")
    if personagem["inventario"]:
        print(f"  Inventário: {', '.join(personagem['inventario'])}")


def atacar(atacante, defensor):
    """Atacante causa dano ao defensor. 20% de chance de crítico (dano dobrado)."""
    critico = random.random() < 0.2
    dano_base = max(0, atacante["ataque"] - defensor["defesa"])
    dano = dano_base * 2 if critico else dano_base
    defensor["vida"] = max(0, defensor["vida"] - dano)
    sufixo = " (CRÍTICO!)" if critico else ""
    print(f"  {atacante['nome']} ataca {defensor['nome']}: "
          f"{dano} de dano{sufixo} | Vida restante: {defensor['vida']}")
