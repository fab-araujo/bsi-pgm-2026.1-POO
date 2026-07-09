# BSI — Programação Orientada a Objetos 2026.1

Repositório de acompanhamento da disciplina. Cada pasta contém a solução de referência para a atividade da aula correspondente, com commits que mostram a construção passo a passo.

## Estrutura

| Pasta | Aula | O que tem |
|-------|------|-----------|
| `aula01/` | Aula 1 | RPG procedural — dicionários, funções, laço de combate |
| `aula02/` | Aula 2 | Análise de classes — tabela, esboço visual, decisões de modelagem |
| `aula03/` | Aula 3 | Primeiras classes OO — `Personagem`, `Monstro`, `main.py` |
| `aula04/` | Aula 4 | Pacote `rpg/` com composição — `Item`, `Inventario`, `@classmethod` |
| `aula05/` | Aula 5 | Herança — `Guerreiro`, `Mago`, `Arqueiro` com três padrões de override + ensaio |
| `aula06/` | Aula 6 | Polimorfismo e duck typing — subclasses de `Monstro` (`monstros.py`), classe `Combate`, protocolo de tipo de dano |
| `aula08/` | Aula 8 | Tratamento de exceções — hierarquia `RpgError` (`exceptions.py`), `raise` no `Inventario`/`Personagem`, captura na borda do `Combate` |
| `aula09/` | Aula 9 | Properties com validação — `vida` (clamp), `nivel` (`ValueError`), `xp` (`XPInvalidoError`) + sistema de XP no `Combate` |
| `aula10/` | Aula 10 | Classes abstratas e sobrecarga de operadores — `Personagem(ABC)`, `golpe_especial`, id de domínio e `__str__`/`__repr__`/`__eq__`/`__hash__` |
| `aula11/` | Aula 11 | Type hints e dataclasses — anotações nos métodos públicos + `Efeito` (`@dataclass`, `efeito.py`) e a queimadura no ataque do `Mago` |
| `trabalho_interface_grafica/` | recesso | **Ponto de partida** do Trabalho de GUI (Tkinter). A pasta `gui_start/` já roda (`cd gui_start && python3 gui_rpg.py`): traz o `rpg/` no estado da Aula 11 + o esqueleto `gui_rpg.py`. **Não é solução** — o aluno completa os `TODO`. Base Aula 11; não depende da atividade da Aula 12. |

## Como usar

Navegue pelos commits para ver como cada solução foi construída passo a passo. Use `git log --oneline` para ver o histórico.

## Aviso sobre o estado dos snapshots (Aulas 3–4 × Aula 5 em diante)

- Os snapshots de `aula03/` e `aula04/` refletem **o estado construído em sala** naquelas semanas: `Personagem`/`Monstro` com `ataque`/`defesa`, `Inventario.remover`, item de tipo `"consumível"`.
- A partir de `aula05/`, o pacote está no **formato definitivo do projeto** — `forca` (no lugar de `ataque`/`defesa`), `nivel`, `xp`, `mostrar_status()`, `Inventario.retirar`, tipos `"arma"`/`"pocao"` — resultado do **Passo 0 da Aula 5** (roteiro no comando da Aula 5). O histórico de commits registra essa transição (commits `aula5: refactor ...`).
- **Se for usar um snapshot como ponto de partida:** os comandos das Aulas 3 e 4 descrevem o formato definitivo, então os nomes podem diferir do snapshot — não é erro; você pode trabalhar com os nomes do snapshot (como foi feito em sala) e converter tudo de uma vez no Passo 0 da Aula 5. Da Aula 5 em diante, snapshot e comandos falam a mesma língua.
