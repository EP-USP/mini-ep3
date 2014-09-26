class FalhouNoTeste(Exception):
	pass

class Teste(object):
	"Classe que representa um teste generico"

	def run(self):
		if self.saida_obtida() != self.saida_esperada():
			raise FalhouNoTeste

	def saida_obtida(self):
		return ''

	def saida_esperada(self):
		return ''


