from rpg.guerreiro import Guerreiro
from rpg.mago import Mago
from rpg.arqueiro import Arqueiro
from rpg.monstros import Goblin, Dragao, Esqueleto
from rpg.combate import Combate


if __name__ == "__main__":
    # Quatro batalhas que exercitam o polimorfismo em combinações distintas.
    # O Combate é o mesmo nos quatro casos — quem varia o comportamento são
    # os próprios combatentes (override de atacar/receber_dano) e o protocolo
    # de tipo de dano. O Combate nunca usa isinstance.

    print("=== Batalha 1: Guerreiro vs Goblin ===")
    # Físico vs físico — vitória fácil do Guerreiro.
    Combate(Guerreiro("Boromir", 100, 20), Goblin()).lutar()

    print("\n=== Batalha 2: Guerreiro vs Esqueleto ===")
    # Físico vs resistente a físico — o Esqueleto recebe metade do dano,
    # então o Guerreiro demora mais para vencer.
    Combate(Guerreiro("Boromir", 100, 20), Esqueleto()).lutar()

    print("\n=== Batalha 3: Mago vs Esqueleto ===")
    # Mágico vs resistente a físico — o dano "magico" do Mago passa integral,
    # ignorando a resistência. Caso pedagogicamente central: o Combate não
    # sabe disso; quem resolve é o protocolo de tipo_dano nos objetos.
    Combate(Mago("Gandalf", 80, 15), Esqueleto()).lutar()

    print("\n=== Batalha 4: Arqueiro vs Dragão ===")
    # Físico vs fogo, com derrota do herói: com flechas=2, o Arqueiro causa
    # 27 nos dois primeiros turnos e cai para 9 quando as flechas acabam,
    # morrendo antes de derrubar o Dragão. O dano "fogo" passa integral.
    Combate(Arqueiro("Legolas", 90, 18, flechas=2), Dragao()).lutar()
