import telepot
from DB import scriviFrase1,scriviFrase2

f1Arrivata = 0
f2Arrivata = 0
personaInAttesa = None

def ascolta_foo(bot,msg,chat_id,persona,i):
	global f1Arrivata
	global f2Arrivata
	global personaInAttesa
	if i==0:
		bot.sendMessage(chat_id, 'Posso ascoltare solo 2 persone per'+ 
		' volta...come si chiama la prima delle due?')
	if i >0 and i < 3:
		persona.append(msg['text'])
		print('Name received')
		if i == 1:
			bot.sendMessage(chat_id, '...e la seconda?')
	if i == 2:
		bot.sendMessage(chat_id, '%s'%persona[0] + ' e %s'%persona[1] +
		', vi sto ascoltando!')
	if i > 2:
		if msg["from"]["first_name"] == persona[0] or msg["from"]["first_name"] == persona[1]:
			if (f1Arrivata == 0 and f2Arrivata == 0) or ((f1Arrivata > f2Arrivata)and msg["from"]["first_name"] == personaInAttesa):
				personaInAttesa = msg["from"]["first_name"]
				scriviFrase1(msg['text'],personaInAttesa,i)
				f1Arrivata += 1
			if (f1Arrivata > f2Arrivata) and msg["from"]["first_name"] != personaInAttesa:
				scriviFrase2(msg['text'],personaInAttesa,msg["from"]["first_name"])
				f2Arrivata += 1
			if f1Arrivata == f2Arrivata:
				f1Arrivata = 0
				f2Arrivata = 0
				personaInAttesa = None #tutte le risposte sono arrivate
			print('messaggio di %s salvato!'%msg["from"]["first_name"])
