from rpg.personagem import Personagem


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

    def _calcular_dano(self, alvo) -> int:
        """Dano-base da classe (super) + dano mágico fixo."""
        return super()._calcular_dano(alvo) + 5
