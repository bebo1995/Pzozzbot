import firebase_admin
from firebase_admin import credentials, firestore
	
def getDB():
	cred = credentials.Certificate('pzozz-53684-firebase-adminsdk-sg7xp-4f367da944.json')
	app = firebase_admin.initialize_app(cred)
	db = firestore.client()
	return db

db = getDB()

def scriviFrase1(frase,utente):
	ref = db.collection('Dialoghi')
	indice = 1
	query = ref.where('utente1','==',utente)
	try:
		docs = query.get()
		numero = 0
		for doc in docs:
			numero += 1
		if numero >= indice:
			indice += numero
	except:
		print('errore di lettura!')
	ref.document().set({
	'indice':indice,
	'frase1':frase,
	'utente1':utente,
	'frase2':None,
	'utente2':None
	})
	
def scriviFrase2(frase,utente1,utente2):
	ref = db.collection('Dialoghi')
	query = ref.where('utente1','==',utente1).where('frase2','==',None).order_by('indice').limit(1)
	try:
		identificativo = None
		docs = query.get()
		for doc in docs:
			identificativo = doc.id
		ref.document(identificativo).update({
		'frase2':frase,
		'utente2':utente2
		})
	except:
		print('errore di lettura!')
		return
