import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
filename = os.path.join( 'clave/clave.json')
cred = credentials.Certificate(filename)
try:
    firebase_admin.initialize_app(cred)
    backend_cnx = firestore.client()
except:
    backend_cnx = firestore.client()
# Don't use cookies
db = backend_cnx
# Project ID is determined by the GCLOUD_PROJECT environment variable
subasta = 'WpZxR21fgLOtUOHeIt2b'
doc_ref = db.collection(u'subastas').document(subasta)
doc = doc_ref.get()
# print(u'Document data: {}'.format(doc.to_dict()))
for i in doc.to_dict()['Acceso_subasta']:
    print(i)
