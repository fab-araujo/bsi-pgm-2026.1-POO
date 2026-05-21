from __future__ import annotations
from rpg.item import Item


class Inventario:
    """Gerencia os itens de um personagem com limite de slots."""

    LIMITE = 10

    def __init__(self) -> None:
        self._itens: list[Item] = []

    @classmethod
    def criar_inicial(cls) -> Inventario:
        """Fábrica: cria um inventário já com uma Poção de Vida."""
        inv = cls()
        inv.adicionar(Item("Poção de Vida", "consumível", 30))
        return inv

    def adicionar(self, item: Item) -> bool:
        """Adiciona item ao inventário. Retorna False se estiver cheio."""
        if len(self._itens) >= self.LIMITE:
            return False
        self._itens.append(item)
        return True

    def remover(self, nome: str) -> Item | None:
        """Remove e retorna o item pelo nome. Retorna None se não encontrar."""
        for i, item in enumerate(self._itens):
            if item.nome == nome:
                return self._itens.pop(i)
        return None

    def listar(self) -> list[Item]:
        """Retorna cópia da lista de itens."""
        return list(self._itens)

    def __len__(self) -> int:
        return len(self._itens)

    def __str__(self) -> str:
        if not self._itens:
            return "(vazio)"
        return ", ".join(str(i) for i in self._itens)
