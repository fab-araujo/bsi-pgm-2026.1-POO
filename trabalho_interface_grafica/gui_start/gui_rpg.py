# -*- coding: utf-8 -*-
"""
gui_rpg.py — Esqueleto do Trabalho de Interface Gráfica (recesso de julho)
===========================================================================

A JANELA em uma frase: ela MOSTRA o status do seu herói (e de um monstro) em
rótulos, e tem BOTÕES que agem sobre eles. A cada clique, os rótulos se
atualizam — ou seja, a interface só lê os objetos do seu `rpg/` e os mostra na
tela. Nada do jogo é reimplementado aqui.

COMO USAR
---------
1. Você está na pasta `gui_start/`, que já tem este arquivo + o `rpg/` (Aula 11).
   No terminal:  cd gui_start   e depois   python3 gui_rpg.py
2. Uma janela deve abrir com o status do herói, o do monstro e um botão "Atacar"
   que JÁ FUNCIONA — antes de você escrever nada. A partir daqui você só COPIA o
   padrão do "Atacar" pra criar as outras ações.
3. No fim do trabalho, leve o SEU gui_rpg.py para a raiz do projeto final (ao
   lado do main.py e da pasta rpg/): ele continua funcionando lá, porque usa só
   métodos que o Personagem já tem.

Tkinter já vem com o Python — NÃO precisa instalar nada. Se der
"ModuleNotFoundError: No module named 'tkinter'" no Linux, rode
`sudo apt install python3-tk`. No Windows e no Mac já vem pronto.

A GRANDE SACADA (lembra da Aula 12?)
------------------------------------
Cada botão recebe uma FUNÇÃO no parâmetro `command=` e a guarda pra chamar
quando for clicado — é o callback da Aula 12 (`aplicar(dobro, 5)`). Você entrega
a função; o Tkinter é quem chama. E a tela é só uma "vista" dos SEUS objetos: a
cada ação você mexe nos objetos e chama `atualizar_tela()` pra reescrever os
rótulos. Mexeu -> atualiza. Sempre.

O QUE FAZER (detalhes, catálogo de peças e rubrica no `comando.md`, no SIGAA)
----------------------------------------------------------------------------
- FAIXA 1 (mínimo p/ passar): botão "Golpe Especial"  ....... TODO A
- FAIXA 2: botão "Usar Poção" + mostrar o inventário  ....... TODO B e TODO C
- FAIXA 3 (OBRIGATÓRIA — a SUA marca): deixe a janela com a sua cara — tema, cores,
  o seu herói/monstro, um widget novo. Veja o "catálogo de peças" no enunciado.
  A base é igual para todos; a cara é sua. (Nem precisa ser tela de batalha.)

Procure a palavra TODO neste arquivo: cada uma é um passo pequeno, com dica.
"""

import tkinter as tk
from tkinter import messagebox

# ─────────────────────────────────────────────────────────────────────────
# 1. OS OBJETOS DO JOGO — a POO que você JÁ fez. A GUI só os USA.
#    (Troque Guerreiro por Mago ou Arqueiro se quiser — todos funcionam.)
# ─────────────────────────────────────────────────────────────────────────
from rpg.guerreiro import Guerreiro
from rpg.monstros import Goblin

heroi = Guerreiro("Aragorn", vida=120, forca=15)
monstro = Goblin()

# ─────────────────────────────────────────────────────────────────────────
# 2. A JANELA e o PAINEL DE STATUS (rótulos que mostram o estado).
#    Guardamos cada Label numa variável pra poder ATUALIZAR o texto depois.
# ─────────────────────────────────────────────────────────────────────────
janela = tk.Tk()
janela.title("Mini RPG")
janela.geometry("560x420")

tk.Label(janela, text="MINI RPG", font=("Helvetica", 18, "bold")).pack(pady=10)

# --- painel de status do herói ---
lbl_heroi = tk.Label(janela, font=("Helvetica", 14))
lbl_heroi.pack(pady=6)

# --- painel de status do monstro ---
lbl_monstro = tk.Label(janela, font=("Helvetica", 14))
lbl_monstro.pack(pady=6)

# --- linha de mensagens ("o herói causou X de dano...") ---
lbl_log = tk.Label(janela, font=("Helvetica", 12), fg="#444",
                   wraplength=520, justify="center")
lbl_log.pack(pady=14)

# TODO C (Faixa 2): se for mostrar o inventário, crie aqui o widget que vai
# exibi-lo — um Label (como os de cima) ou um Listbox (peça E do catálogo, no
# enunciado). Depois preencha-o dentro de atualizar_tela() (veja o TODO C de lá).


# ─────────────────────────────────────────────────────────────────────────
# 3. ATUALIZAR A TELA — lê os objetos e reescreve os rótulos.
#    Chame esta função DEPOIS de toda ação. É o "mexeu -> atualiza".
#    (type(heroi).__name__ dá a CLASSE do herói: "Guerreiro", "Mago"...)
# ─────────────────────────────────────────────────────────────────────────
def atualizar_tela():
    lbl_heroi.config(
        text=f"{heroi.nome} ({type(heroi).__name__})   |   "
             f"vida {heroi.vida}/{heroi.vida_maxima}   |   "
             f"nível {heroi.nivel}   |   XP {heroi.xp}")
    lbl_monstro.config(
        text=f"{monstro.nome} ({monstro.tipo})   |   vida {monstro.vida}"
             f"   |   nível {monstro.nivel}")

    # TODO C (Faixa 2): mostre o inventário aqui. Você tem
    # heroi.inventario.listar() — uma lista de itens, cada um com .nome. Junte
    # os nomes num texto (Label) ou preencha um Listbox (peça E do catálogo).


def registrar(mensagem):
    """Escreve uma linha no rótulo de mensagens."""
    lbl_log.config(text=mensagem)


def jogo_acabou():
    """True se alguém já morreu — usado para travar os botões no fim."""
    return (not heroi.esta_vivo()) or (not monstro.esta_vivo())


def checar_fim():
    """Mostra uma caixa de aviso quando a batalha termina."""
    if not monstro.esta_vivo():
        messagebox.showinfo("Fim da batalha", f"{heroi.nome} venceu!")
    elif not heroi.esta_vivo():
        messagebox.showinfo("Fim da batalha",
                            f"{monstro.nome} derrotou {heroi.nome}...")


# ─────────────────────────────────────────────────────────────────────────
# 4. AS AÇÕES — cada botão chama uma destas funções (o CALLBACK da Aula 12).
#    O padrão é sempre o mesmo:
#       (a) mexe nos objetos;  (b) registra;  (c) atualizar_tela();  (d) checa fim.
# ─────────────────────────────────────────────────────────────────────────
def acao_atacar():
    if jogo_acabou():
        return
    dano = heroi.atacar(monstro)              # (a) herói bate no monstro
    if monstro.esta_vivo():
        contra = monstro.atacar(heroi)        #     monstro revida, se sobreviveu
        registrar(f"{heroi.nome} causou {dano} de dano. "
                  f"{monstro.nome} revidou {contra}.")   # (b)
    else:
        registrar(f"{heroi.nome} causou {dano} e derrotou {monstro.nome}!")
    atualizar_tela()                          # (c)
    checar_fim()                              # (d)


# A acao_atacar() acima é o seu MOLDE. As suas ações seguem os mesmos 4 passos
# (mexe / registra / atualizar_tela() / checar_fim()). Escreva as suas aqui:

# TODO A (Faixa 1) — a ação do GOLPE ESPECIAL.
#   É a acao_atacar() com UMA diferença: em vez de heroi.atacar(monstro), use
#   heroi.golpe_especial(monstro). Comece por  def acao_golpe():  e siga os 4
#   passos, olhando a acao_atacar como referência. (O botão dela fica no bloco 5.)


# TODO B (Faixa 2) — a ação de USAR POÇÃO.
#   Dentro dela: chame  heroi.usar_item("Poção")  (devolve True se havia poção),
#   registre uma mensagem com registrar(...) e chame atualizar_tela() no fim.
#   (Aqui não precisa do checar_fim: poção não mata ninguém.)


# ─────────────────────────────────────────────────────────────────────────
# 5. OS BOTÕES.
#    command=acao_atacar entrega a FUNÇÃO (repare: SEM os parênteses!) pro
#    botão guardar e chamar no clique. É o callback da Aula 12 na prática.
#    Escrever command=acao_atacar() com parênteses é o erro clássico: aí você
#    chamaria a função AGORA e passaria o retorno (None) pro botão. Sem ().
# ─────────────────────────────────────────────────────────────────────────
tk.Button(janela, text="Atacar", width=18, font=("Helvetica", 13),
          command=acao_atacar).pack(pady=5)

# TODO A — crie o botão do "Golpe Especial". Molde: o botão "Atacar" logo acima
#          (mude o text= e aponte o command= para a SUA acao_golpe, sem os ()).

# TODO B — crie o botão "Usar Poção", do mesmo jeito, apontando para acao_pocao.


# ─────────────────────────────────────────────────────────────────────────
# 6. COMEÇA. atualizar_tela() desenha o estado inicial; mainloop() mantém a
#    janela aberta esperando os cliques. (mainloop fica SEMPRE por último.)
# ─────────────────────────────────────────────────────────────────────────
atualizar_tela()
janela.mainloop()
