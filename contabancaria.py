class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False  

    def __str__(self):
        return f"Conta de {self.titular} - Saldo: R${self.saldo}"

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True


conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 500)

print(conta1)
print(conta2)

conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")


class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo


conta4 = ContaBancariaPythonica("Fernanda", 1500)
print(f"Titular: {conta4.titular}")
print(f"Saldo: R${conta4.saldo}")
print(f"Conta ativa? {conta4.ativo}")
