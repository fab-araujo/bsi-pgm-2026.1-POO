"""Hierarquia de exceções do domínio do RPG.

Vocabulário compartilhado: o Inventario e o Personagem LEVANTAM estas
exceções; o Combate e o main.py as CAPTURAM. Como este módulo não importa
nada do pacote, qualquer módulo pode importá-lo sem risco de import circular.

A base RpgError permite capturar qualquer falha do domínio com um único
`except RpgError`, sem nunca engolir bugs de programação (KeyError,
TypeError...), que não herdam dela.
"""


class RpgError(Exception):
    """Base de todas as falhas do domínio do RPG.

    Herda de Exception (nunca de BaseException). Capturar RpgError pega a
    base e todas as subclasses — herança aplicada ao tratamento de erro.
    """


class InventarioCheioError(RpgError):
    """Levantada quando se tenta adicionar um item a um inventário cheio."""


class PersonagemMortoError(RpgError):
    """Levantada quando um personagem morto tenta atacar."""


class XPInvalidoError(RpgError):
    """Levantada quando se tenta fazer o XP regredir (XP é cumulativo).

    Entra na mesma hierarquia (RpgError) — por isso o `except RpgError` do
    Combate captura também esta falha.
    """
