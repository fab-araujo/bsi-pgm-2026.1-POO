class Monstro:
    """Representa um monstro inimigo. Sem inventário."""

    def __init__(self, nome: str, vida: int, ataque: int, defesa: int, tipo: str) -> None:
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.tipo = tipo

    def atacar(self, alvo) -> int:
        """Ataca o alvo e retorna o dano causado."""
        dano = max(0, self.ataque - alvo.defesa)
        alvo.receber_dano(dano)
        return dano

    def receber_dano(self, quantidade: int) -> None:
        self.vida = max(0, self.vida - quantidade)

    def esta_vivo(self) -> bool:
        return self.vida > 0

    def __str__(self) -> str:
        return (f"{self.nome} [{self.tipo}] | vida: {self.vida} | "
                f"ataque: {self.ataque} | defesa: {self.defesa}")
