class Nodo(object):
	def __init__ (self, frase, indice, figli):
		self.frase = frase
		self.indice = indice
		self.figli = figli
	
	@staticmethod
	def from_dict(source, selettore):
		if selettore == 1:
			nodo = Nodo(source.to_dict['frase1'], source.to_dict['indice'], [])
		else:
			if selettore == 2:
				nodo = Nodo(source.to_dict()['frase2'], source.to_dict()['indice'], [])
			else:
				print('errore selettore!')
		return nodo
	def __repr__(self):
		return ('nodo: frase: {}, figli: [{}]'.format(self.frase,self.risposte))
