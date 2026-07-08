from __future__ import annotations


class Item:
    """Representa um item que pode ser guardado no inventário."""

    def __init__(self, nome: str, tipo: str, valor: int) -> None:
        self.nome = nome
        self.tipo = tipo
        self.valor = valor

    @staticmethod
    def tipo_valido(tipo: str) -> bool:
        """Decide se uma string nomeia um tipo aceito de item.

        Validador puro — não depende de instância nem do estado da classe,
        por isso é @staticmethod. Centraliza a lista de tipos aceitos num
        único lugar; quem chama (Inventario.adicionar) não precisa conhecer.
        """
        return tipo in ("arma", "pocao")

    @classmethod
    def padrao(cls) -> Item:
        """Fábrica alternativa: devolve uma poção padrão.

        Usa @classmethod (em vez de método de instância) porque cria um
        objeto novo a partir da classe — não precisa de self. cls em vez
        de Item explícito mantém o método correto se for herdado.
        """
        return cls("Poção", "pocao", 20)

    def __str__(self) -> str:
        return f"{self.nome} ({self.tipo}, val: {self.valor})"
