import firebase_admin
from firebase_admin import credentials, firestore
	
def getDB():
	cred = credentials.Certificate('pzozz-53684-firebase-adminsdk-sg7xp-44b6ab3049.json')
	app = firebase_admin.initialize_app(cred)
	db = firestore.client()
	return db

db = getDB()

def scriviFrase1(frase,utente,contatore):
	indice = contatore - 2 #il contatore parte da 3. se sottraggo 2 inizia da 1.
	frase = frase.lower()
	ref = db.collection('Dialoghi')
	n_dialogo = 1
	query = ref.order_by('ndialogo',direction=firestore.Query.DESCENDING).limit(1)
	docs = query.get()
	numero = 0
	for doc in docs:
		if indice == 1: #se indice == 1 è iniziato un nuovo dialogo
			#quindi devi incrementare il numero del dialogo.
			n_dialogo = doc.to_dict()['ndialogo'] + 1
	ref.document().set({
	'ndialogo' :n_dialogo,
	'indice':indice,
	'frase1':frase,
	'utente1':utente,
	'frase2':None,
	'utente2':None
	})
	
def scriviFrase2(frase,utente1,utente2):
	frase = frase.lower()
	ref = db.collection('Dialoghi')
	query = ref.where('utente1','==',utente1).where('frase2','==',None).order_by('indice').limit(1)
	identificativo = None
	docs = query.get()
	for doc in docs:
		identificativo = doc.id
	ref.document(identificativo).update({
	'frase2':frase,
	'utente2':utente2
	})
		
def leggiRisposte(frase1):
	frase1 = frase1.lower()
	ref = db.collection('Dialoghi')
	query = ref.where('frase1','==',frase1)
	docs = query.get()
	return docs	
