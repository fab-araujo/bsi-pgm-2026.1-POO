from rpg.inventario import Inventario
from rpg.item import Item


class Personagem:
    """Representa um personagem jogável. Tem um Inventario por composição."""

    def __init__(self, nome: str, vida: int, ataque: int, defesa: int) -> None:
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        # composição: o Inventario pertence a este Personagem
        self.inventario: Inventario = Inventario.criar_inicial()

    def atacar(self, alvo: "Personagem") -> int:
        """Ataca o alvo e retorna o dano causado."""
        dano = max(0, self.ataque - alvo.defesa)
        alvo.receber_dano(dano)
        return dano

    def usar_item(self, nome: str) -> bool:
        """Usa (remove) um item do inventário pelo nome. Retorna False se não tiver."""
        item = self.inventario.remover(nome)
        if item is None:
            return False
        if item.tipo == "consumível":
            self.vida = min(self.vida + item.valor, self.vida + item.valor)
            print(f"  {self.nome} usou {item.nome} e recuperou {item.valor} pontos de vida!")
        return True

    def receber_dano(self, quantidade: int) -> None:
        """Reduz a vida, sem deixar abaixo de zero."""
        self.vida = max(0, self.vida - quantidade)

    def esta_vivo(self) -> bool:
        return self.vida > 0

    @staticmethod
    def calcular_dano(ataque: int, defesa: int) -> int:
        """Utilitário: calcula dano líquido dado ataque e defesa."""
        return max(0, ataque - defesa)

    def __str__(self) -> str:
        return (f"{self.nome} | vida: {self.vida} | "
                f"ataque: {self.ataque} | defesa: {self.defesa} | "
                f"inventário: {self.inventario}")
