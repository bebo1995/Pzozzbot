import telepot

def ascolta_foo(bot,msg,chat_id,persona,i):
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
		if msg["from"]["first_name"] == persona[0]:
			file1 = open("frasi1.txt","a")
			print('text from %s saved!'%persona[0])
			file1.write(msg['text'] + '\n')
			file1.close()
		if msg["from"]["first_name"] == persona[1]:
			file2 = open("frasi2.txt","a")
			print('text from %s saved!'%persona[1])
			file2.write(msg['text'])
			file2.close()
