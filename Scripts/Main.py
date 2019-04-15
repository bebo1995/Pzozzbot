import telepot
import time
from Ascolta import ascolta_foo
from Socializza import socializza_foo

contatore = 0
token = '875364456:AAHS_6zDU5-PE7WeVxUvRhwHnu4QSwoyAtg'
Pzozzbot = telepot.Bot(token)
ascoltando = False
socializzando = False
nomi = []

def on_chat_message(msg):
	global nomi
	global contatore
	global ascoltando
	global socializzando
	global Pzozzbot
	print('Message received')
	content_type, chat_type, chat_id = telepot.glance(msg)
	name = msg["from"]["first_name"]#nome di chi ha scritto
	txt = msg['text']#messaggio scritto
	if content_type == 'text':
		print ('Text received')
		if txt == '/smetti':
			Pzozzbot.sendMessage(chat_id, 'Ok.')
			ascoltando = False
			socializzando = False
			contatore = 0
			nomi = []
		if socializzando == True:
			print('Socializing function running...')
			socializza_foo(msg,chat_id,Pzozzbot)
		if txt == '/socializza':
			print('Socializing function started')
			Pzozzbot.sendMessage(chat_id, 'Vediamo cosa ho imparato.')
			ascoltando = False
			socializzando = True
		if txt == '/ascolta':
			print('Listening function started')
			ascoltando = True
			socializzando = False
			contatore = 0
			nomi = []
		if ascoltando == True:
			print('Listening function running...')
			ascolta_foo(Pzozzbot,msg,chat_id,nomi,contatore)
			contatore += 1
		

Pzozzbot.message_loop(on_chat_message)

print('Pzozz started!')
while 1:
	time.sleep(10)
