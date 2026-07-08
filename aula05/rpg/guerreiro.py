from rpg.personagem import Personagem


class Guerreiro(Personagem):
    """Herói focado em dano físico bruto.

    Padrão de override: SUBSTITUIÇÃO COMPLETA.

    Reescreve atacar sem chamar super(). O contrato é preservado —
    mesma assinatura, mesmo efeito observável (reduz a vida do alvo,
    devolve o dano) —, o que muda é a estratégia interna de cálculo:
    em vez do dano base, soma um bônus fixo da arma.
    """

    def __init__(self, nome: str, vida: int, forca: int,
                 nivel: int = 1, xp: int = 0, arma: str = "Espada") -> None:
        # chama o construtor da base para inicializar os atributos herdados
        super().__init__(nome, vida, forca, nivel, xp)
        # atributo próprio: usado no flavor (aparece no __str__ futuramente)
        self.arma = arma

    def atacar(self, alvo) -> int:
        """Golpe físico com bônus de arma (forca + 5)."""
        dano = self.forca + 5
        alvo.receber_dano(dano)
        return dano
