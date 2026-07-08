from __future__ import annotations
from rpg.item import Item
from rpg.exceptions import InventarioCheioError


class Inventario:
    """Gerencia os itens de um personagem com limite de slots."""

    # Atributo de CLASSE: o limite é o mesmo para todos os inventários.
    # Não há razão para cada instância carregar sua própria cópia.
    LIMITE = 10

    def __init__(self) -> None:
        # convenção de uso interno: o sublinhado sinaliza que código
        # externo não deve mexer diretamente na lista
        self._itens: list[Item] = []

    @classmethod
    def criar_inicial(cls) -> Inventario:
        """Fábrica: cria um inventário inicial com duas poções padrão.

        Quantidade fixa em 2 — evita encher o inventário até o LIMITE por
        engano e mantém os testes da Aula 13 operacionais.
        """
        inv = cls()
        inv.adicionar(Item.padrao())  # 1ª poção
        inv.adicionar(Item.padrao())  # 2ª poção
        return inv

    def adicionar(self, item: Item) -> bool:
        """Adiciona item ao inventário. Valida tipo e respeita LIMITE.

        Devolve True se adicionou. Tipo inválido continua devolvendo False
        (validação de dado de entrada que o chamador consegue checar antes,
        contrato da Aula 4). Inventário cheio, porém, é fluxo que NÃO pode
        continuar: levanta InventarioCheioError (Aula 8). A validação de
        tipo é delegada para Item.tipo_valido — quem decide o que é tipo
        válido é a classe Item.
        """
        if not Item.tipo_valido(item.tipo):
            return False
        if len(self._itens) >= self.LIMITE:
            raise InventarioCheioError(
                f"inventário cheio ({self.LIMITE} slots) — não coube: {item.nome}"
            )
        self._itens.append(item)
        return True

    def retirar(self, nome: str) -> Item | None:
        """Retira e devolve o item pelo nome. None se não encontrar.

        Note: None é o sentinela do tipo de retorno. Item não encontrado
        é resultado válido de uma busca, não um erro — quem chama trata.
        """
        for i, item in enumerate(self._itens):
            if item.nome == nome:
                return self._itens.pop(i)
        return None

    def listar(self) -> list[Item]:
        """Devolve uma cópia defensiva da lista de itens.

        Encapsulamento: código externo pode iterar e ler, mas não pode
        mutar o estado interno sem passar por adicionar/retirar.
        """
        return list(self._itens)

    def __len__(self) -> int:
        return len(self._itens)

    def __str__(self) -> str:
        if not self._itens:
            return "(vazio)"
        return ", ".join(str(i) for i in self._itens)
