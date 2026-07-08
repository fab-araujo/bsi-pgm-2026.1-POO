from dataclasses import dataclass


@dataclass
class Efeito:
    """Efeito contínuo aplicado a um combatente, turno a turno (Aula 11).

    Classe de DADOS: o @dataclass gera __init__, __repr__ e __eq__ a partir
    dos campos anotados. NÃO usa frozen — na Aula 13 a duracao será
    decrementada a cada turno, então o Efeito precisa continuar mutável.
    """

    nome: str
    valor_por_turno: int  # negativo = dano, positivo = regeneração
    duracao: int          # por quantos turnos o efeito dura

    def aplicar(self, combatente) -> None:
        """Aplica o efeito de UM turno ao combatente.

        Método escrito à mão (o @dataclass não o gera). Guarda de domínio:
        um combatente morto NÃO é afetado — em especial, uma regeneração
        não ressuscita quem está em vida zero. A duracao não é tocada aqui;
        o consumo turno a turno entra na Aula 13.
        """
        if not combatente.esta_vivo():
            return
        combatente.vida = combatente.vida + self.valor_por_turno
