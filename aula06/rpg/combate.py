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

        # 3. Contra-ataque se o defensor continua vivo
        dano_def = 0
        if self.defensor.esta_vivo():
            dano_def = self.defensor.atacar(self.atacante)

        # 4. Efeitos ativos do defensor (preparatório — no-op nesta aula)

        return {
            "dano_atacante": dano_atk,
            "dano_defensor": dano_def,
            "atacante_vivo": self.atacante.esta_vivo(),
            "defensor_vivo": self.defensor.esta_vivo(),
        }

    def lutar(self):
        """Itera turnos até um lado morrer. Devolve o vencedor."""
        turno = 1
        while self.atacante.esta_vivo() and self.defensor.esta_vivo():
            resumo = self.executar_turno()
            print(f"Turno {turno}: "
                  f"{self.atacante.nome} causou {resumo['dano_atacante']} | "
                  f"{self.defensor.nome} causou {resumo['dano_defensor']}")
            turno += 1

        vencedor = self.atacante if self.atacante.esta_vivo() else self.defensor
        print(f"\nVencedor: {vencedor.nome}!")
        return vencedor
