from rpg.monstro import Monstro


class Goblin(Monstro):
    """Monstro fraco. Herda tudo da base — categorização pura.

    Padrão de herança: SEM OVERRIDE. Herdar sem sobrescrever também é
    herança válida — o ganho aqui é categorização + ajuste de defaults
    no construtor.
    """

    def __init__(self, nome: str = "Goblin", vida: int = 30,
                 forca: int = 5, nivel: int = 1) -> None:
        super().__init__(nome, vida, forca, tipo="humanoide", nivel=nivel)


class Dragao(Monstro):
    """Monstro poderoso com baforada de fogo.

    Padrão de herança: OVERRIDE de atacar com tipo de dano distinto.
    Sobrescreve tipo_dano ("fogo") e atacar (dano aumentado), aplicando
    via receber_dano(dano, self.tipo_dano) — o contrato observável é
    preservado.
    """

    tipo_dano: str = "fogo"

    def __init__(self, nome: str = "Dragão Vermelho", vida: int = 150,
                 forca: int = 25, nivel: int = 5) -> None:
        super().__init__(nome, vida, forca, tipo="besta", nivel=nivel)

    def atacar(self, alvo) -> int:
        dano = self.forca + 10
        alvo.receber_dano(dano, self.tipo_dano)
        return dano


class Esqueleto(Monstro):
    """Morto-vivo resistente a dano físico.

    Padrão de herança: OVERRIDE de receber_dano com resistência parcial.
    Recebe metade do dano "fisico" (resistência parcial, não imunidade —
    imunidade total geraria combate infinito contra atacantes puramente
    físicos). Qualquer outro tipo de dano passa integral. Delega o cálculo
    final à base via super().
    """

    def __init__(self, nome: str = "Esqueleto", vida: int = 60,
                 forca: int = 12, nivel: int = 3) -> None:
        super().__init__(nome, vida, forca, tipo="morto-vivo", nivel=nivel)

    def receber_dano(self, quantidade: int, tipo_dano: str = "fisico") -> None:
        if tipo_dano == "fisico":
            quantidade = quantidade // 2
        super().receber_dano(quantidade, tipo_dano)
