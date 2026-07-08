# Aula 2 — Análise de classes do Mini RPG

## Tabela de análise

| Classe | Propósito | Atributos principais | Métodos principais |
|--------|-----------|----------------------|--------------------|
| `Personagem` | Representa o herói jogável | `nome`, `vida`, `ataque`, `defesa`, `inventario` | `atacar(alvo)`, `receber_dano(qtd)`, `esta_vivo()` |
| `Monstro` | Representa um inimigo | `nome`, `vida`, `ataque`, `defesa`, `tipo` | `atacar(alvo)`, `receber_dano(qtd)`, `esta_vivo()` |
| `Item` | Um objeto que ocupa um slot no inventário | `nome`, `tipo`, `valor` | `__str__()` |
| `Inventario` | Guarda e gerencia os itens do personagem | `_itens` (lista), `LIMITE` | `adicionar(item)`, `remover(nome)`, `listar()` |
| `Combate` | Orquestra o combate entre dois combatentes | — | `lutar(combatente_a, combatente_b)` |

## Esboço visual das relações

```
[Personagem] ──── compõe (1:1) ────→ [Inventario]
                                           │
                                     contém (0..*)
                                           │
                                           ↓
                                         [Item]

[Monstro]    (estrutura análoga a Personagem, sem inventário)

[Combate] ───── conhece (usa em método) ─────→ [Personagem]
          ───── conhece (usa em método) ─────→ [Monstro]
```

**Relação de composição:** `Personagem` *compõe* `Inventario` — se o personagem desaparece, o inventário também desaparece. Não faz sentido ter um inventário "solto" sem dono.

**Relação de associação:** `Combate` apenas *conhece* `Personagem` e `Monstro` durante o método `lutar` — não os possui.

## Decisões de modelagem

**Por que `Monstro` é uma classe separada de `Personagem`?**
Monstros e personagens compartilham uma interface (atacar, receber dano, verificar se vivo), mas têm origens diferentes. `Personagem` tem inventário; `Monstro` não. Manter separado agora deixa o código mais claro. Nas próximas aulas, quando aprendermos herança, vamos unificar isso de forma mais elegante.

**O que ficou de fora desta análise?**
- Sistemas de XP e nível (aparecem mais à frente)
- Subclasses de personagem (Guerreiro, Mago, Arqueiro) — vêm na Aula 5
- Exceções personalizadas — Aula 8
- Persistência (salvar/carregar) — Aula 13
