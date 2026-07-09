# Trabalho de Interface Gráfica — uma janela para o seu RPG

**Recesso de julho. Entrega até 13/08/2026, apresentada na Aula 14. Vale 2,0 pontos** — dos 4,0 da
apresentação da NAP 2; os outros 2,0 são do projeto integrado (`jogo.py` + `rpg/` + *save/load*).
Individual.

Este trabalho pede uma coisa só: colocar o seu RPG **numa janela**. A janela **mostra o status** do
seu herói (e de um monstro) em rótulos e tem **alguns botões** que agem sobre eles. Parece grande,
mas você **não vai reprogramar o jogo** — toda a lógica (herói, monstro, combate, inventário) já
está pronta nas suas classes. A interface é só uma **vista** por cima delas: mostra o estado e
oferece botões que chamam os métodos que você já tem.

> **Leia isto primeiro, é o mais importante:** existe um esqueleto pronto, o **`gui_rpg.py`**, que
> **já abre uma janela funcionando** — com o status do herói, o do monstro e um botão "Atacar" que
> já bate e atualiza a tela. Você começa de um jogo que roda, e só **estende por cópia**. Ninguém
> começa do zero.

**Ponto de partida — a pasta `gui_start/` já roda.** Baixe-a no SIGAA, entre nela e rode
`python3 gui_rpg.py`: uma janela abre com o status do herói e o botão **Atacar** funcionando, antes
de você escrever qualquer linha. Dentro dela há o `rpg/` no estado da **Aula 11** (o esqueleto usa
só `atacar`, `golpe_especial`, `usar_item`, `inventario`, que o seu `Personagem` já tem) e o
`gui_rpg.py`. A GUI é um trabalho **à parte**: **não depende da atividade da Aula 12** — você pode
fazê-la sem ter mexido no `rpg/` de hoje. No fim, leve o seu `gui_rpg.py` para o projeto final.
**Tkinter já vem com o Python — nada a instalar** (no Linux, se faltar: `sudo apt install
python3-tk`).

---

## A ideia em uma frase (e a ligação com a Aula 12)

Uma interface gráfica é feita de **callbacks**. Cada botão recebe uma **função** e a guarda para
chamar **quando for clicado**. É exatamente o callback da Aula 12: você entrega a função, e outra
coisa (agora o botão) é quem chama.

```python
def acao_atacar():          # a função que faz a ação
    ...

botao = tk.Button(janela, text="Atacar", command=acao_atacar)
#                                          ^^^^^^^^^^^^^^^^^^^^
#                    entrega a função (SEM parênteses) — callback!
```

O resto é um ciclo que se repete: **o usuário clica → você mexe nos objetos do jogo → você redesenha
os rótulos**. Só isso, para cada botão.

---

## Tkinter em 4 conceitos (é só o que você precisa)

Tkinter é a biblioteca gráfica que **já vem com o Python** — nada a instalar. Você usa quatro
coisas:

**1. A janela.**
```python
import tkinter as tk
janela = tk.Tk()
janela.title("Mini RPG")
```

**2. Rótulos e botões (widgets).** `Label` mostra texto; `Button` é clicável. `.pack()` coloca o
widget na janela (empilha de cima para baixo).
```python
rotulo = tk.Label(janela, text="Vida: 100")
rotulo.pack()
tk.Button(janela, text="Atacar", command=acao_atacar).pack()
```

**3. Atualizar um rótulo.** Guarde o `Label` numa variável e use `.config(text=...)` para trocar o
texto quando o estado muda.
```python
rotulo.config(text=f"Vida: {heroi.vida}")
```

**4. Ligar tudo.** No fim do arquivo, `janela.mainloop()` mantém a janela aberta esperando cliques.
Fica **sempre por último**.
```python
janela.mainloop()
```

Pronto. Com esses quatro, dá para fazer o trabalho inteiro. Não precisa de mais widget nenhum, nem
de uma segunda janela — **tudo numa janela só**.

---

## O padrão que se repete (guarde isto)

Toda ação de botão segue os mesmos quatro passinhos:

1. **mexe** nos objetos do jogo (`heroi.atacar(monstro)`, `heroi.usar_item("Poção")`…);
2. **registra** uma mensagem do que aconteceu;
3. **atualiza a tela** (`atualizar_tela()` reescreve os rótulos com o novo estado);
4. **checa o fim** (alguém morreu?).

O esqueleto já traz a ação "Atacar" escrita assim. Para criar as outras, **copie essa função e mude
uma linha**. É esse o trabalho.

---

## A base é a mesma para todos; a CARA é sua

O esqueleto é só o ponto de partida — não é para entregar ele com dois botões a mais e pronto. A
regra do trabalho: **a sua janela precisa ter algo autoral e visual — uma cara que a dos outros
não vai ter.** Pode ser o tema, as cores, um widget novo, o herói e os monstros que você escolheu,
o layout. Isso **não é bônus, é requisito** (vale 0,5 dos 2,0 — a Faixa 3). Duas entregas idênticas
ao esqueleto valem menos que uma janela simples **com a sua marca**.

E ela **nem precisa ser uma tela de batalha**. Alguns temas possíveis (escolha um ou invente):

- **Ficha de personagem** — só o status do herói, caprichado, com botões que sobem XP / usam item.
- **Loja / taverna** — lista de itens, um botão "comprar/usar" que mexe no inventário.
- **Bestiário** — mostra vários monstros do `rpg/` e os atributos de cada um.
- **Party** — dois ou três heróis na tela, cada um com o seu painel.
- **Arena de batalha** — a versão do esqueleto, com a sua cara.

## O que entregar — três faixas

Faça na ordem.

### Faixa 1 — funciona e conecta (o mínimo para passar)
- Rodar o `gui_rpg.py`: a janela abre com o **painel de status** do herói (nome, classe, nível, XP,
  vida/vida máxima) e do monstro, mais o botão **Atacar** — os rótulos **atualizam** a cada clique.
  (O esqueleto já dá isto.)
- Adicionar o botão **Golpe Especial** (`TODO A`): copiar a ação "Atacar" e trocar
  `heroi.atacar(monstro)` por `heroi.golpe_especial(monstro)`.

### Faixa 2 — mais ações
- Botão **Usar Poção** (`TODO B`): `heroi.usar_item("Poção")` + atualizar a tela.
- Mostrar o **inventário** na tela (`TODO C`): os nomes dos itens da mochila
  (`heroi.inventario.listar()`).

### Faixa 3 — o seu toque (OBRIGATÓRIO, e a parte mais importante)
Pelo menos **uma** coisa autoral, que os outros não terão. Não precisa ser difícil — precisa ser
**sua**. Use o **catálogo de peças** abaixo, combine as peças como quiser, ou invente. Mudar as
cores e trocar o herói/monstro já conta; quanto mais a janela tiver a sua cara, melhor.

---

## Catálogo de peças (misture à vontade)

Cada peça é curta e cai direto no `gui_rpg.py`. **Não use todas** — escolha as que combinam com a
sua ideia. É daqui que sai a sua versão única.

**A. Cores.** Qualquer rótulo/botão aceita `fg` (cor do texto) e `bg` (fundo); a janela aceita `bg`.
```python
janela.config(bg="#1e1e1e")
tk.Label(janela, text="MINI RPG", fg="#f4c430", bg="#1e1e1e").pack()
tk.Button(janela, text="Atacar", bg="#a33", fg="white", command=acao_atacar).pack()
```

**B. Escolha o seu herói.** Troque a classe lá no topo — todas já funcionam.
```python
from rpg.mago import Mago
heroi = Mago("Gandalf", vida=90, forca=18)     # ou Guerreiro, ou Arqueiro
```

**C. Escolha o seu inimigo (roster próprio).**
```python
from rpg.monstros import Dragao, Esqueleto
monstro = Dragao()                              # troque o adversário
```

**D. Barra de vida.** Uma barrinha que encolhe conforme a vida cai.
```python
from tkinter import ttk
barra = ttk.Progressbar(janela, maximum=heroi.vida_maxima, length=300)
barra.pack(pady=4)
# dentro de atualizar_tela():
barra["value"] = heroi.vida
```

**E. Uma lista rolável (`Listbox`).** Serve pra mostrar vários nomes (itens, monstros, heróis…).
```python
lista = tk.Listbox(janela, height=5)
lista.pack(pady=4)
# para encher/atualizar: limpe e insira os textos que você quiser
lista.delete(0, tk.END)
lista.insert(tk.END, "exemplo 1")
lista.insert(tk.END, "exemplo 2")
```
Troque os textos de exemplo pelos dados que você for exibir (é você que liga a lista aos objetos).

**F. Botão Reiniciar.** Recomeça o jogo do zero.
```python
def acao_reiniciar():
    global heroi, monstro
    heroi = Guerreiro("Aragorn", vida=120, forca=15)
    monstro = Goblin()
    registrar("Novo jogo!")
    atualizar_tela()
tk.Button(janela, text="Reiniciar", command=acao_reiniciar).pack()
```

**G. Símbolos nos rótulos.** É só texto — coloque o que quiser no `text=` (ex.: `"HP: "`, setas,
`>>`, `[x]`).

**H. Duas colunas (`grid`).** Quer herói de um lado e monstro do outro? Troque **todos** os `.pack()`
por `.grid(row=, column=)` — só não misture `pack` e `grid` na mesma janela.
```python
lbl_heroi.grid(row=1, column=0, padx=20)
lbl_monstro.grid(row=1, column=1, padx=20)
```

> **Onde mexer:** abra o `gui_rpg.py`, procure a palavra **`TODO`** (as faixas 1–2) e escolha peças
> do catálogo (faixa 3). Faça uma coisa de cada vez, rodando a cada mudança.

---

## Erros comuns (e a solução)

- **`command=acao_atacar()` não funciona / o botão "clica sozinho".** Você pôs **parênteses**. Sem
  eles: `command=acao_atacar`. Com parênteses, a função roda na hora de criar o botão, não no
  clique — é o erro nº 1 de GUI. (É o mesmo cuidado do `f = dobro` sem `()` da Aula 12.)
- **`ModuleNotFoundError: No module named 'rpg'`.** Rode de dentro da pasta `gui_start` (ela já traz
  o `rpg/`). Se você levou o `gui_rpg.py` para o seu projeto, ele precisa ficar na **raiz**, ao lado
  da pasta `rpg/`.
- **`ModuleNotFoundError: No module named 'tkinter'` (Linux).** Instale: `sudo apt install
  python3-tk`. No Windows e no Mac já vem junto.
- **A tela não muda depois de clicar.** Você esqueceu de chamar `atualizar_tela()` no fim da ação.
  Mexeu nos objetos? Então atualize a tela.
- **`PersonagemMortoError` ao clicar depois que alguém morreu.** Cheque `jogo_acabou()` no começo de
  cada ação (o esqueleto já mostra como) — um morto não pode atacar.

---

## Como entregar

- **Arquivo:** o seu `gui_rpg.py` (com os `TODO` que você completou), junto com a pasta do projeto,
  compactado em **ZIP**.
- **Screenshots:** 1 ou 2 imagens (PNG/JPG) da janela funcionando — antes e depois de uns cliques,
  por exemplo.
- **Canal:** SIGAA. **Prazo:** **13/08/2026**.
- **Apresentação:** na **Aula 14** você mostra a janela rodando e explica, em duas frases, onde está
  o callback (o `command=` de um botão) e onde a tela lê os seus objetos (o `atualizar_tela`).

## Como isto é avaliado (2,0 pontos)

Não é um concurso de beleza. A nota:

- **1,0 — funciona e conecta (Faixa 1):** a janela abre e mostra o status; os botões **Atacar** e
  **Golpe Especial** chamam os métodos certos do seu RPG; a tela reflete o estado a cada clique; a
  interface usa as **suas** classes (`Personagem`/`Inventario`), não uma lógica paralela.
- **0,5 — mais ações (Faixa 2):** botão **Usar Poção** + inventário mostrado na tela.
- **0,5 — o seu toque (Faixa 3, obrigatório):** pelo menos uma coisa autoral que os outros não
  terão (tema, cores, um widget do catálogo, o seu herói/roster, layout). Entregar o esqueleto **sem
  nenhuma marca própria** perde esta faixa inteira, mesmo que funcione.

Na apresentação (Aula 14), além de apontar o callback (`command=`) e onde a tela lê os seus objetos
(`atualizar_tela`), **mostre o seu toque**. Uma janela simples que mostra o status, tem os botões
funcionando lendo os seus objetos e tem uma marca sua por cima já é um trabalho completo — o
essencial é pequeno e você **consegue**.
