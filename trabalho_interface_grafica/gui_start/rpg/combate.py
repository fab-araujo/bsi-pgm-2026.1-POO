from rpg.exceptions import RpgError


class Combate:
    """Gerencia uma batalha entre dois combatentes.

    Duck typing: aceita qualquer combinação de Personagem e Monstro —
    não usa isinstance, só os métodos da interface comum (atacar,
    receber_dano, esta_vivo, nome).
    """

    def __init__(self, atacante, defensor) -> None:
        self.atacante = atacante
        self.defensor = defensor

    def executar_turno(self, acao: str = "atacar") -> dict:
        """Executa um turno e devolve um resumo.

        O parâmetro `acao` aceitará "atacar", "golpe_especial" e
        "usar_item" em aulas futuras; nesta aula só "atacar" faz algo
        concreto, então o parâmetro fica declarado mas não é consultado.
        A separação executar_turno (um turno) / lutar (até morrer) é
        deliberada: na Aula 13 o jogo.py chama executar_turno direto,
        intercalando um menu entre os turnos.
        """
        # 1. Efeitos ativos do atacante (preparatório — no-op nesta aula)

        # 2. Ação do atacante
        dano_atk = self.atacante.atacar(self.defensor)
        if not self.defensor.esta_vivo():
            self._distribuir_xp(self.atacante, self.defensor)

        # 3. Contra-ataque se o defensor continua vivo
        dano_def = 0
        if self.defensor.esta_vivo():
            dano_def = self.defensor.atacar(self.atacante)
            if not self.atacante.esta_vivo():
                self._distribuir_xp(self.defensor, self.atacante)

        # 4. Efeitos ativos do defensor (preparatório — no-op nesta aula)

        return {
            "dano_atacante": dano_atk,
            "dano_defensor": dano_def,
            "atacante_vivo": self.atacante.esta_vivo(),
            "defensor_vivo": self.defensor.esta_vivo(),
        }

    @staticmethod
    def _distribuir_xp(vencedor, perdedor) -> None:
        """Dá XP ao vencedor por derrotar o perdedor (Aula 9).

        Fórmula desta oferta: nível_do_inimigo * 50. Duck typing (Aula 6):
        só quem TEM ganhar_xp recebe XP — ou seja, só o Personagem; o
        Monstro foi modelado sem XP desde a Aula 3, então quando um Monstro
        mata o Personagem a batalha encerra sem distribuir nada.
        """
        if hasattr(vencedor, "ganhar_xp"):
            vencedor.ganhar_xp(perdedor.nivel * 50)

    def lutar(self):
        """Itera turnos até um lado morrer. Devolve o vencedor.

        Sem anotação de retorno de propósito (Aula 11): o vencedor é um
        combatente duck-typed (pode ser Personagem ou Monstro), e forçar um
        tipo concreto aqui contraria a decisão de projeto do Combate — a
        mesma razão pela qual os parâmetros atacante/defensor ficam sem
        anotação. Devolve None quando o combate é interrompido por RpgError.
        """
        turno = 1
        while self.atacante.esta_vivo() and self.defensor.esta_vivo():
            # Rede de segurança na BORDA (Aula 8): qualquer falha do domínio
            # (RpgError e subclasses) que suba da pilha encerra o combate com
            # mensagem amigável, em vez de derrubar o programa. Bugs de
            # programação (que não são RpgError) continuam estourando.
            try:
                resumo = self.executar_turno()
            except RpgError as erro:
                print(f"[combate interrompido] {erro}")
                return None
            print(f"Turno {turno}: "
                  f"{self.atacante.nome} causou {resumo['dano_atacante']} | "
                  f"{self.defensor.nome} causou {resumo['dano_defensor']}")
            turno += 1

        vencedor = self.atacante if self.atacante.esta_vivo() else self.defensor
        print(f"\nVencedor: {vencedor.nome}!")
        return vencedor
