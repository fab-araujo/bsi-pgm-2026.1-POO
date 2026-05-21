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


def turno_heroi(heroi, monstro):
    """Lê a escolha do jogador e executa a ação correspondente.
    Retorna False se o herói decidir fugir, True caso contrário."""
    print("\nO que você quer fazer?")
    print("  1 - Atacar")
    print("  2 - Usar Poção de Vida")
    print("  3 - Fugir")
    escolha = input("Escolha: ").strip()

    if escolha == "1":
        atacar(heroi, monstro)
    elif escolha == "2":
        if "Poção de Vida" in heroi["inventario"]:
            heroi["inventario"].remove("Poção de Vida")
            heroi["vida"] = min(100, heroi["vida"] + 30)
            print(f"  {heroi['nome']} usou Poção de Vida e recuperou 30 pontos! "
                  f"Vida: {heroi['vida']}")
        else:
            print("  Sem Poções de Vida no inventário!")
    elif escolha == "3":
        print(f"  {heroi['nome']} fugiu da batalha...")
        return False
    else:
        print("  Escolha inválida. Turno perdido!")

    return True


def combate(heroi, monstro):
    """Laço principal de combate. Alterna turnos até alguém morrer ou o herói fugir."""
    print(f"\n{'='*50}")
    print(f"  BATALHA: {heroi['nome']} vs {monstro['nome']}")
    print(f"{'='*50}")

    turno = 1
    while heroi["vida"] > 0 and monstro["vida"] > 0:
        print(f"\n--- Turno {turno} ---")
        exibir_status(heroi)
        exibir_status(monstro)

        if not turno_heroi(heroi, monstro):
            return  # herói fugiu

        if monstro["vida"] > 0:
            atacar(monstro, heroi)

        turno += 1

    print(f"\n{'='*50}")
    if heroi["vida"] > 0:
        print(f"  VITÓRIA! {heroi['nome']} venceu a batalha!")
    else:
        print(f"  DERROTA. {monstro['nome']} venceu.")
    print(f"{'='*50}")


# Programa principal
if __name__ == "__main__":
    print("=== Mini RPG de Terminal — versão procedural ===")
    print("(POO começa na próxima aula — aqui só funções e dicionários)\n")
    combate(heroi, monstro)
