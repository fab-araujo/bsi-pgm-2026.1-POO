# BSI — Programação Orientada a Objetos 2026.1

Repositório de acompanhamento da disciplina. Cada pasta contém a solução de referência para a atividade da aula correspondente, com commits que mostram a construção passo a passo.

## Estrutura

| Pasta | Aula | O que tem |
|-------|------|-----------|
| `aula1/` | Aula 1 | RPG procedural — dicionários, funções, laço de combate |
| `aula2/` | Aula 2 | Análise de classes — tabela, esboço visual, decisões de modelagem |
| `aula3/` | Aula 3 | Primeiras classes OO — `Personagem`, `Monstro`, `main.py` |
| `aula4/` | Aula 4 | Pacote `rpg/` com composição — `Item`, `Inventario`, `@classmethod` |
| `aula5/` | Aula 5 | Herança — `Guerreiro`, `Mago`, `Arqueiro` com três padrões de override + ensaio |
| `aula6/` | Aula 6 | Polimorfismo e duck typing — subclasses de `Monstro` (`monstros.py`), classe `Combate`, protocolo de tipo de dano |

## Como usar

Navegue pelos commits para ver como cada solução foi construída passo a passo. Use `git log --oneline` para ver o histórico.

## Aviso sobre o estado dos snapshots (Aulas 3–4 × Aula 5 em diante)

- Os snapshots de `aula3/` e `aula4/` refletem **o estado construído em sala** naquelas semanas: `Personagem`/`Monstro` com `ataque`/`defesa`, `Inventario.remover`, item de tipo `"consumível"`.
- A partir de `aula5/`, o pacote está no **formato definitivo do projeto** — `forca` (no lugar de `ataque`/`defesa`), `nivel`, `xp`, `mostrar_status()`, `Inventario.retirar`, tipos `"arma"`/`"pocao"` — resultado do **Passo 0 da Aula 5** (roteiro no comando da Aula 5). O histórico de commits registra essa transição (commits `aula5: refactor ...`).
- **Se for usar um snapshot como ponto de partida:** os comandos das Aulas 3 e 4 descrevem o formato definitivo, então os nomes podem diferir do snapshot — não é erro; você pode trabalhar com os nomes do snapshot (como foi feito em sala) e converter tudo de uma vez no Passo 0 da Aula 5. Da Aula 5 em diante, snapshot e comandos falam a mesma língua.
