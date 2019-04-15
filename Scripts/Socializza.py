from Nodo import Nodo
import telepot
from DB import leggiRisposte

def socializza_foo(msg,chat_id,bot):
	parole = msg['text'].split()
	procedi = False
	for parola in parole:
		if parola == '@Pzozzbot':
			parole.remove(parola)
			procedi = True
	if (procedi == False):
		print('Non è un messaggio per Pzozz')
		return
	print('è un messaggio per Pzozz')
	messaggio = ""
	nodo = Nodo("",[])
	for parola in parole:
		messaggio += parola + " "
	messaggio = messaggio[:-1] #rimuovi spazio finale
	docs = leggiRisposte(messaggio)
	for doc in docs:
		nodo = Nodo.from_dict(doc.to_dict(),nodo)
	risposta = 'e sticazzi!'
	if len(nodo.risposte) > 0:
		risposta = nodo.risposte[0]
	bot.sendMessage(chat_id,risposta)
		