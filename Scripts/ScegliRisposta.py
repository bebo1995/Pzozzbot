from DB import leggiRisposte
from Nodo import Nodo
import random

def scegliRisposta(messaggio):
	root = Nodo(messaggio, 0, [])
	docs = leggiRisposte(messaggio)
	indiceMax = 0
	risposta = 'stocazz'
	for doc in docs:
		root.figli.append(Nodo.from_dict(doc, 2))
		if doc.to_dict()['indice'] > indiceMax:
			indiceMax = doc.to_dict()['indice']
			risposta = doc.to_dict()['frase2']
	return risposta
