import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import uuid

cred = credentials.Certificate('/Users/lewisarnsten/Desktop/poll-72a8a-1b1d4322cc32.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://poll-72a8a.firebaseio.com'})

ref = db.reference('server/saving-data/')
users_ref = ref.child('users')
posts_ref = ref.child('posts')
comments_ref = ref.child('posts/comments')

class User():
	def __init__(self,username,name,date_of_birth,sex,zipc):
		self.username = username
		self.name = name
		self.date_of_birth = date_of_birth
		self.sex = sex
		self.zipc = zipc
		self.userID = uuid.uuid4()

	def generate(self):
		users_ref.update({
		'u{}'.format(self.userID):{
		'username':'{}'.format(self.username),
		'full_name':'{}'.format(self.name),
		'date_of_birth':'{}'.format(self.date_of_birth),
		'sex':'{}'.format(self.sex),
		'zip':'{}'.format(self.zipc)
		}
		})

class Post():
	def __init__(self,title,tags,location):
		self.location = location
		self.title = title
		self.tags = tags
		self.postID = uuid.uuid4()

	def upload(self):
		comments = []
		posts_ref.update({
		'p{}'.format(self.postID):{
		'title':'{}'.format(self.title),
		'tags':'{}'.format(self.tags),
		'location':'{}'.format(self.location),
		'comments': '{}'.format(comments)
		}
		})

class Comment():
	def __init__(self,text,postID):
		self.text = text
		self.postID = postID
		#use ref.get() for uuid
	def upload(self):
		posts_ref.update({
		'c{}'.format(self.postID):{
		'title':'{}'.format(self.text),
		}
		})


u1 = User('lewarn','Lewis Arnsten', '10/31/2000', 'male', '10025')
#u1.generate()
p1 = Post('Vote to make David the new head of the comp sci department','David Pitt, Politics, Computers', '10471')
#p1.upload()
c1 = Comment('I like pies',p1.postID)
c2 = Comment('I like shrek', p1.postID)
c2.upload()
