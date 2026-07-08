from rpg.inventario import Inventario
from rpg.exceptions import PersonagemMortoError


class Personagem:
    """Representa um personagem jogável. Tem um Inventario por composição."""

    # Atributo de CLASSE: o tipo de dano que este combatente aplica.
    # Introduzido na Aula 6 para o protocolo de tipo de dano — quem reage
    # ao tipo (o Esqueleto resiste a "fisico") é o próprio defensor, no seu
    # receber_dano. O default "fisico" mantém a compatibilidade.
    tipo_dano: str = "fisico"

    def __init__(self, nome: str, vida: int, forca: int,
                 nivel: int = 1, xp: int = 0) -> None:
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.nivel = nivel
        self.xp = xp
        # composição: o Inventario pertence a este Personagem
        self.inventario: Inventario = Inventario.criar_inicial()

    def atacar(self, alvo) -> int:
        """Ataca o alvo e retorna o dano causado.

        Três responsabilidades, nesta ordem (Aula 8): (1) VALIDAR — morto
        não ataca, levanta PersonagemMortoError; (2) CALCULAR — delega o
        dano ao método interno _calcular_dano; (3) APLICAR — entrega o dano
        ao alvo com self.tipo_dano e devolve o valor. A validação mora aqui,
        num só lugar; as subclasses só sobrescrevem _calcular_dano.
        """
        if not self.esta_vivo():
            raise PersonagemMortoError(f"{self.nome} está morto e não pode atacar")
        dano = self._calcular_dano(alvo)
        alvo.receber_dano(dano, self.tipo_dano)
        return dano

    def _calcular_dano(self, alvo) -> int:
        """Dano-base do personagem. Uso interno (sublinhado, Aula 4).

        Ponto de extensão do polimorfismo: cada subclasse sobrescreve ESTE
        método (não o atacar) com a sua estratégia de cálculo.
        """
        return self.forca

    def receber_dano(self, quantidade: int, tipo_dano: str = "fisico") -> None:
        """Reduz a vida, sem deixar abaixo de zero.

        O parâmetro tipo_dano (Aula 6) tem default "fisico", então todo
        código anterior que chamava receber_dano(quantidade) segue válido.
        A base ignora o tipo; subclasses que reagem a ele (Esqueleto)
        sobrescrevem este método.
        """
        self.vida = max(0, self.vida - quantidade)

    def esta_vivo(self) -> bool:
        return self.vida > 0

    def usar_item(self, nome: str) -> bool:
        """Usa (retira) um item do inventário pelo nome. False se não tiver."""
        item = self.inventario.retirar(nome)
        if item is None:
            return False
        if item.tipo == "pocao":
            # sem teto por enquanto; vida_maxima vem na Aula 9 com @property
            self.vida += item.valor
            print(f"  {self.nome} usou {item.nome} e recuperou {item.valor} pontos de vida!")
        return True

    def mostrar_status(self) -> None:
        """Imprime o estado atual do personagem."""
        print(f"{self.nome} — nível {self.nivel}, vida {self.vida}, XP {self.xp}")
