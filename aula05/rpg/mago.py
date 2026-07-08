from rpg.personagem import Personagem


class Mago(Personagem):
    """Herói focado em magia.

    Padrão de override: EXTENSÃO POR super().

    Chama o ataque da classe-base (super().atacar) e, em seguida,
    acrescenta dano mágico. Preserva tudo o que a base faz e estende
    com comportamento próprio. O retorno soma os dois danos.
    """

    def __init__(self, nome: str, vida: int, forca: int,
                 nivel: int = 1, xp: int = 0, mana: int = 100) -> None:
        super().__init__(nome, vida, forca, nivel, xp)
        # mana é decorativo nesta aula — ganha papel real em aulas seguintes
        self.mana = mana

    def atacar(self, alvo) -> int:
        """Golpe físico base + dano mágico fixo."""
        dano_base = super().atacar(alvo)  # aplica a parte física
        dano_magico = 5
        alvo.receber_dano(dano_magico)     # adiciona a parte mágica
        return dano_base + dano_magico
