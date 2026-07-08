from rpg.guerreiro import Guerreiro
from rpg.mago import Mago
from rpg.monstros import Goblin
from rpg.item import Item
from rpg.combate import Combate
from rpg.exceptions import RpgError, InventarioCheioError, PersonagemMortoError


if __name__ == "__main__":
    # Aula 8: as exceções do domínio nascem fundo na pilha (Inventario,
    # Personagem) e são capturadas na borda (Combate, aqui no main). O
    # programa roda do início ao fim SEM nenhum traceback.

    print("=== 1. Batalha normal ===")
    # Combate comum: nenhuma exceção do domínio é levantada.
    Combate(Guerreiro("Boromir", 100, 20), Goblin()).lutar()

    print("\n=== 2. Inventário cheio ===")
    # Captura ESPECÍFICA de InventarioCheioError: enchemos o inventário
    # além do LIMITE (começa com 2 poções; cabem 8 antes de estourar).
    heroi = Guerreiro("Aragorn", 100, 20)
    try:
        for numero in range(3, 12):
            heroi.inventario.adicionar(Item(f"Poção {numero}", "pocao", 20))
    except InventarioCheioError as erro:
        print(f"  Mochila lotada! ({erro})")

    print("\n=== 3. Personagem morto tenta atacar ===")
    # Captura ESPECÍFICA de PersonagemMortoError: derrubamos o herói com
    # receber_dano e mandamos ele atacar.
    caido = Mago("Gandalf", 80, 15)
    caido.receber_dano(999)                 # vida vai a zero
    try:
        caido.atacar(Goblin())
    except PersonagemMortoError as erro:
        print(f"  Ataque cancelado: {erro}")

    print("\n=== 4. Captura genérica com RpgError ===")
    # A base RpgError pega QUALQUER falha do domínio — aqui, a mesma
    # PersonagemMortoError, mas tratada pela classe-base.
    try:
        caido.atacar(Goblin())
    except RpgError as erro:
        print(f"  Alguma regra do jogo impediu a ação: {erro}")

    print("\nFim da demonstração.")
