from rpg.personagem import Personagem
from rpg.efeito import Efeito


class Mago(Personagem):
    """Herói focado em magia.

    Padrão de override: EXTENSÃO POR super().

    Sobrescreve _calcular_dano chamando o cálculo da base (super()) e
    somando dano mágico. Preserva tudo o que a base calcula e estende com
    comportamento próprio. Como o dano agora é UM número só, quem o aplica
    (uma vez, via receber_dano com self.tipo_dano) é o atacar da base —
    diferente da Aula 6, em que havia DUAS chamadas a receber_dano.

    tipo_dano sobrescrito para "magico" (Aula 6): o dano total entra como
    "magico" — por isso o Mago ignora a resistência física do Esqueleto.
    """

    tipo_dano: str = "magico"

    def __init__(self, nome: str, vida: int, forca: int,
                 nivel: int = 1, xp: int = 0, mana: int = 100) -> None:
        super().__init__(nome, vida, forca, nivel, xp)
        # mana é decorativo nesta aula — ganha papel real em aulas seguintes
        self.mana = mana

    def atacar(self, alvo) -> int:
        """Ataque normal + queimadura no alvo (Aula 11).

        Delega o dano ao atacar da base (validação, cálculo e aplicação) e,
        DEPOIS de causar o dano, deixa um Efeito de Queimadura no alvo
        (-5 por turno, 3 turnos). É no atacar, não no golpe_especial, porque
        o golpe_especial será refatorado na Aula 12 — a queimadura é
        independente disso.
        """
        dano = super().atacar(alvo)
        alvo.adicionar_efeito(Efeito("Queimadura", -5, 3))
        return dano

    def _calcular_dano(self, alvo) -> int:
        """Dano-base da classe (super) + dano mágico fixo."""
        return super()._calcular_dano(alvo) + 5

    def golpe_especial(self, alvo) -> int:
        """Explosão Arcana: forca + 10, com tipo_dano "magico".

        Implementa o contrato abstrato da base (Aula 10). Será refatorado
        na Aula 12 para lançar uma magia do grimório — esta versão é o
        gancho que a Aula 12 reaproveita.
        """
        dano = self.forca + 10
        alvo.receber_dano(dano, self.tipo_dano)
        return dano
