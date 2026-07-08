from rpg.personagem import Personagem


class Guerreiro(Personagem):
    """Herói focado em dano físico bruto.

    Padrão de override: SUBSTITUIÇÃO COMPLETA.

    Reescreve _calcular_dano sem chamar super() (Aula 8: o override migrou
    de atacar para o método interno de cálculo). O contrato é preservado —
    mesma assinatura, mesmo efeito observável (reduz a vida do alvo,
    devolve o dano) —, o que muda é a estratégia interna de cálculo:
    em vez do dano base, soma um bônus fixo da arma.

    tipo_dano herdado ("fisico"): o Guerreiro é o caso contra o qual a
    resistência do Esqueleto se manifesta (Aula 6).
    """

    def __init__(self, nome: str, vida: int, forca: int,
                 nivel: int = 1, xp: int = 0, arma: str = "Espada") -> None:
        # chama o construtor da base para inicializar os atributos herdados
        super().__init__(nome, vida, forca, nivel, xp)
        # atributo próprio: usado no flavor (aparece no __str__ futuramente)
        self.arma = arma

    def _calcular_dano(self, alvo) -> int:
        """Golpe físico com bônus de arma (forca + 5).

        Substituição completa: reescreve o cálculo da base sem chamar
        super(). Quem valida (morto não ataca) e aplica o dano é o atacar
        da base — este método só devolve o número.
        """
        return self.forca + 5

    def golpe_especial(self, alvo) -> int:
        """Golpe Brutal: dano físico dobrado (forca * 2).

        Implementa o contrato abstrato da base (Aula 10). Como o atacar,
        aplica o dano ao alvo com self.tipo_dano e devolve o valor.
        """
        dano = self.forca * 2
        alvo.receber_dano(dano, self.tipo_dano)
        return dano
