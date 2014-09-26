class FalhouNoTeste(Exception):
    pass


class Teste(object):
    "Classe que representa um teste generico"
    def __init__(self, saida_obtida='', saida_esperada='', test_name=''):
        self.test_name = test_name
        self.saida_obtida = saida_obtida
        self.saida_esperada = saida_esperada

    def run(self):
        if self.obter_saida() != self.esperada():
            print(self.test_name)
            print(self.obter_saida())
            print(self.esperada())
            raise FalhouNoTeste

    def obter_saida(self):
        return self.saida_obtida

    def esperada(self):
        return self.saida_esperada
