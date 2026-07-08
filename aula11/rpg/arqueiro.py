from rpg.personagem import Personagem


class Arqueiro(Personagem):
    """Herói focado em ataques à distância.

    Padrão de override: ESPECIALIZAÇÃO VIA ESTADO PRÓPRIO.

    O atributo self.flechas existe apenas na subclasse e é consultado
    pelo _calcular_dano para decidir o dano — com flechas, tiro à distância
    (dano alto); sem flechas, golpe corpo-a-corpo (dano fraco).

    A assinatura herdada (_calcular_dano(self, alvo)) é PRESERVADA. Nada de
    parâmetros novos. Esse cuidado mantém a substituição de subtipo:
    código cliente que aceita Personagem também aceita Arqueiro sem
    quebrar — é a forma idiomática quando a variação depende de algo
    que só a subclasse conhece.

    tipo_dano herdado ("fisico").
    """

    def __init__(self, nome: str, vida: int, forca: int,
                 nivel: int = 1, xp: int = 0, flechas: int = 20) -> None:
        super().__init__(nome, vida, forca, nivel, xp)
        self.flechas = flechas

    def _calcular_dano(self, alvo) -> int:
        """Com flechas: tiro à distância (forca × 1.5).
        Sem flechas: golpe físico fraco (forca // 2)."""
        if self.flechas > 0:
            self.flechas -= 1
            return int(self.forca * 1.5)
        return self.forca // 2

    def golpe_especial(self, alvo):
        """Saraivada: gasta 3 flechas para forca * 3.

        Sem 3 flechas, é um tiro fraco (forca // 2). Implementa o contrato
        abstrato da base (Aula 10): aplica o dano ao alvo e devolve o valor.
        """
        if self.flechas >= 3:
            self.flechas -= 3
            dano = self.forca * 3
        else:
            dano = self.forca // 2
        alvo.receber_dano(dano, self.tipo_dano)
        return dano
