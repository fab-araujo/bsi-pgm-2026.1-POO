from rpg.inventario import Inventario
from rpg.exceptions import PersonagemMortoError, XPInvalidoError


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
        self.forca = forca
        # vida_maxima é o teto da barra de vida (Aula 9). ATENÇÃO À ORDEM:
        # o setter de vida consulta self.vida_maxima, então ela precisa
        # existir ANTES de atribuir self.vida.
        self.vida_maxima = vida
        # Inicializamos o campo interno antes de passar pelo setter, para
        # que a primeira atribuição já encontre o estado consistente.
        self._vida = 0
        self.vida = vida
        self._nivel = 1
        self.nivel = nivel
        self._xp = 0
        self.xp = xp
        # composição: o Inventario pertence a este Personagem
        self.inventario: Inventario = Inventario.criar_inicial()

    @property
    def vida(self) -> int:
        return self._vida

    @vida.setter
    def vida(self, valor: int) -> None:
        """Estratégia CLAMP: grampeia o valor no intervalo [0, vida_maxima].

        Nunca levanta exceção — apenas corrige. Consequência boa: uma poção
        não cura além do máximo, e o dano não deixa a vida negativa.
        """
        self._vida = max(0, min(valor, self.vida_maxima))

    @property
    def nivel(self) -> int:
        return self._nivel

    @nivel.setter
    def nivel(self, valor: int) -> None:
        """Estratégia REJEITAR com ValueError: nível < 1 é dado inválido.

        Usa a exceção padrão do Python para dado inválido (não uma exceção
        de domínio), porque "nível < 1" é uma violação genérica. A subida
        automática de nível NÃO passa por aqui — ela ajusta self._nivel
        diretamente (ver o setter de xp).
        """
        if valor < 1:
            raise ValueError(f"nível deve ser >= 1, recebido {valor}")
        self._nivel = valor

    @property
    def xp(self) -> int:
        return self._xp

    @xp.setter
    def xp(self, valor: int) -> None:
        """Estratégia REJEITAR com exceção de DOMÍNIO: XP não regride.

        "XP é cumulativo" é uma regra do jogo, por isso usa XPInvalidoError
        (e não ValueError). Depois de aumentar o XP, sobe de nível enquanto
        o acumulado atingir o limiar (N-1)*100. A subida incrementa o
        atributo interno diretamente — não passa pelo setter de nível, que
        serve só para barrar atribuições externas inválidas.
        """
        if valor < self._xp:
            raise XPInvalidoError(
                f"XP não pode regredir: {valor} < {self._xp} (XP é cumulativo)"
            )
        self._xp = valor
        while self._xp >= self._nivel * 100:
            self._nivel += 1
            print(f"  {self.nome} subiu para o nível {self._nivel}!")

    def ganhar_xp(self, quantidade: int) -> None:
        """Soma XP ao total, passando pelo setter (respeita a regra)."""
        self.xp = self._xp + quantidade

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
        sobrescrevem este método. Escreve na property vida (Aula 9): o
        clamp do setter garante o piso 0 automaticamente.
        """
        self.vida = self.vida - quantidade

    def esta_vivo(self) -> bool:
        return self.vida > 0

    def usar_item(self, nome: str) -> bool:
        """Usa (retira) um item do inventário pelo nome. False se não tiver."""
        item = self.inventario.retirar(nome)
        if item is None:
            return False
        if item.tipo == "pocao":
            # escreve na property vida (Aula 9): o clamp impede curar além
            # de vida_maxima — a poção nunca ultrapassa o teto.
            self.vida = self.vida + item.valor
            print(f"  {self.nome} usou {item.nome} e recuperou {item.valor} pontos de vida!")
        return True

    def mostrar_status(self) -> None:
        """Imprime o estado atual do personagem."""
        print(f"{self.nome} — nível {self.nivel}, vida {self.vida}, XP {self.xp}")
