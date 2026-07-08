# Por que herança em vez de um atributo `tipo`?

A escolha por modelar `Guerreiro`, `Mago` e `Arqueiro` como subclasses de `Personagem` — em vez de manter um único `Personagem` com um atributo `tipo` — é guiada pelo comportamento distinto que cada classe exerce no momento do ataque.

Se houvesse uma única classe `Personagem` com `tipo="guerreiro"`, o método `atacar` precisaria carregar uma cadeia de `if/elif` para decidir qual fórmula aplicar a cada caso. Cada nova classe (Bárbaro, Paladino, Necromante) exigiria mais uma cláusula no condicional, com risco de esquecer algum ramo. O método cresceria sem limite e ficaria difícil de manter — sem falar no acoplamento: o `Personagem` passaria a conhecer todos os tipos do jogo.

Com herança, cada subclasse encapsula a própria estratégia de combate. O `Guerreiro` aplica `self.forca + 5` substituindo completamente o ataque base — é dano físico bruto, e não há interesse em reaproveitar o cálculo da base. O `Mago` estende a base via `super().atacar(alvo)` e acrescenta dano mágico — preserva o golpe original e soma uma camada por cima. O `Arqueiro` consulta um atributo próprio (`self.flechas`) para decidir entre tiro à distância (dano alto) e luta corpo-a-corpo (dano fraco) — estado interno que só a subclasse precisa conhecer, e que não pertence ao contrato do `Personagem` genérico.

Os três padrões de override (substituição, extensão por `super()`, especialização via estado próprio) só fazem sentido com herança. Cada classe pode evoluir independentemente, sem tocar nas outras. Adicionar um novo herói no futuro é criar uma nova subclasse; o `Personagem` permanece intacto.
