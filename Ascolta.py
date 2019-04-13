import telepot

def ascolta_foo(bot,msg,chat_id,n,i):
	if i==0:
		bot.sendMessage(chat_id, 'Posso ascoltare solo 2 persone per'+ 
		' volta...come si chiama la prima delle due?')
	if i >0 and i < 3:
		n.append(msg['text'])
		print('Name received')
		if i == 1:
			bot.sendMessage(chat_id, '...e la seconda?')
	if i == 2:
		bot.sendMessage(chat_id, '%s'%n[0] + ' e %s'%n[1] +
		', vi sto ascoltando!')
