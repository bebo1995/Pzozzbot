from ScegliRisposta import scegliRisposta
import telepot

def socializza_foo(msg,chat_id,bot):
	parole = msg['text'].split()
	procedi = False
	for parola in parole:
		if parola == '@Pzozzbot':
			parole.remove(parola)
			procedi = True
	if (procedi == False):
		return
	print('è un messaggio per Pzozz!')
	messaggio = ""
	for parola in parole:
		messaggio += parola + " "
	messaggio = messaggio[:-1] #rimuovi spazio finale
	risposta = scegliRisposta(messaggio)
	bot.sendMessage(chat_id,risposta)
	print('risposta inviata!')
		
