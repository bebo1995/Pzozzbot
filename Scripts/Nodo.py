class Nodo(object):
	def __init__ (self, frase, risposte):
		self.frase = frase
		self.risposte = risposte
	
	@staticmethod
	def from_dict(source, nodo):
		if nodo.frase == None:
			nodo = Nodo(source['frase1'],[])
		nodo.risposte.append(source['frase2'])
		return nodo
	def __repr__(self):
		return ('nodo: frase: {}, figli: [{}]'.format(self.frase,self.risposte))
