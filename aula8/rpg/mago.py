from rpg.personagem import Personagem


class Mago(Personagem):
    """Herói focado em magia.

    Padrão de override: EXTENSÃO POR super().

    Chama o ataque da classe-base (super().atacar) e, em seguida,
    acrescenta dano mágico. Preserva tudo o que a base faz e estende
    com comportamento próprio. O retorno soma os dois danos.

    tipo_dano sobrescrito para "magico" (Aula 6): tanto o golpe base
    (via super().atacar, que usa self.tipo_dano) quanto o dano mágico
    extra entram como "magico" — por isso o Mago ignora a resistência
    física do Esqueleto.
    """

    tipo_dano: str = "magico"

    def __init__(self, nome: str, vida: int, forca: int,
                 nivel: int = 1, xp: int = 0, mana: int = 100) -> None:
        super().__init__(nome, vida, forca, nivel, xp)
        # mana é decorativo nesta aula — ganha papel real em aulas seguintes
        self.mana = mana

    def atacar(self, alvo) -> int:
        """Golpe físico base + dano mágico fixo."""
        dano_base = super().atacar(alvo)        # parte física, já com tipo_dano="magico"
        dano_magico = 5
        # a segunda chamada também precisa passar self.tipo_dano — senão o
        # dano extra entraria como "fisico" e seria cortado pelo Esqueleto
        alvo.receber_dano(dano_magico, self.tipo_dano)
        return dano_base + dano_magico
