from rpg.personagem import Personagem


class Arqueiro(Personagem):
    """Herói focado em ataques à distância.

    Padrão de override: ESPECIALIZAÇÃO VIA ESTADO PRÓPRIO.

    O atributo self.flechas existe apenas na subclasse e é consultado
    pelo atacar para decidir o dano — com flechas, tiro à distância
    (dano alto); sem flechas, golpe corpo-a-corpo (dano fraco).

    A assinatura herdada (atacar(self, alvo)) é PRESERVADA. Nada de
    parâmetros novos. Esse cuidado mantém a substituição de subtipo:
    código cliente que aceita Personagem também aceita Arqueiro sem
    quebrar — é a forma idiomática quando a variação depende de algo
    que só a subclasse conhece.
    """

    def __init__(self, nome: str, vida: int, forca: int,
                 nivel: int = 1, xp: int = 0, flechas: int = 20) -> None:
        super().__init__(nome, vida, forca, nivel, xp)
        self.flechas = flechas

    def atacar(self, alvo) -> int:
        """Com flechas: tiro à distância (forca × 1.5).
        Sem flechas: golpe físico fraco (forca // 2)."""
        if self.flechas > 0:
            self.flechas -= 1
            dano = int(self.forca * 1.5)
        else:
            dano = self.forca // 2
        alvo.receber_dano(dano)
        return dano
