from __future__ import annotations

from rpg.efeito import Efeito


class Monstro:
    """Representa um monstro inimigo. Sem inventário."""

    # Atributo de CLASSE: tipo de dano aplicado (Aula 6). Mesmo protocolo
    # do Personagem — subclasses como o Dragao sobrescrevem ("fogo").
    tipo_dano: str = "fisico"

    def __init__(self, nome: str, vida: int, forca: int, tipo: str,
                 nivel: int = 1) -> None:
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.tipo = tipo
        # nivel é usado pelo sistema de XP na Aula 9 — o XP que o
        # personagem ganha ao matar um monstro depende do nível dele.
        # Monstro NÃO tem xp: esse atributo é exclusivo do jogador.
        self.nivel = nivel
        # efeitos contínuos ativos (Aula 11): o Mago aplica queimadura ao
        # monstro alvo, então o Monstro também precisa suportar efeitos.
        self.efeitos_ativos: list[Efeito] = []

    def atacar(self, alvo) -> int:
        """Ataca o alvo e retorna o dano causado."""
        alvo.receber_dano(self.forca, self.tipo_dano)
        return self.forca

    def receber_dano(self, quantidade: int, tipo_dano: str = "fisico") -> None:
        self.vida = max(0, self.vida - quantidade)

    def esta_vivo(self) -> bool:
        return self.vida > 0

    def adicionar_efeito(self, efeito: Efeito) -> None:
        """Acrescenta um Efeito à lista de efeitos ativos (Aula 11)."""
        self.efeitos_ativos.append(efeito)

    def mostrar_status(self) -> None:
        """Imprime o estado do monstro (sem XP — esse é do Personagem)."""
        print(f"{self.nome} ({self.tipo}) — nível {self.nivel}, vida {self.vida}")
