class Item:
    """Representa um item que pode ser guardado no inventário."""

    def __init__(self, nome: str, tipo: str, valor: int = 0) -> None:
        self.nome = nome
        self.tipo = tipo
        self.valor = valor

    def __str__(self) -> str:
        return f"{self.nome} ({self.tipo}, val: {self.valor})"
