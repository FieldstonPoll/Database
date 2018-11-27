import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('//Users/lewisarnsten/Desktop/poll-72a8a-1b1d4322cc32.json')
default_app = firebase_admin.initialize_app(cred)