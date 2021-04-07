from Prosses.__init__ import db, login_manager
from sqlalchemy import ForeignKey
from datetime import *
from flask_login import UserMixin, current_user

@login_manager.user_loader
def load_user(id, endpoint='admin'):
	if endpoint == "admin":
		return Admin.query.get(id)

# @login_manager.user_loader
# def load_user(id, endpoint='user'):
# 	if endpoint == "user":
# 		return User.query.get(id)

class Admin(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True, autoincrement=True)
	Nama = db.Column(db.String(100), unique=True)
	Password = db.Column(db.String(100))
	Gen = db.Column(db.String(50))
	Jenis_Penjualan = db.Column(db.String(100))
	no_telp = db.Column(db.Integer)
	frgn = db.relationship("Product", backref="author",cascade="all, delete", lazy="select")

	def is_active(self):
		return True

	def get_id(self):
		return self.id

	def is_authenticated(self):
		return self.authenticated

	def is_anonymous(self):
		return False

	def is_accessible(self):
		return current_user.is_active and current_user.is_authenticated
	# def __init__(self, Nama, Password, Gen, Jenis_Penjualan,no_telp):
	# 	self.Nama = Nama
	# 	self.Password = Password
	# 	self.Gen = Gen
	# 	self.Jenis_Penjualan = Jenis_Penjualan
	# 	self.no_telp = no_telp

	# def toString(self):
	# 	return({"id_adm":self.id_adm,"Nama": self.Nama, "Password": self.Password, "Gen":self.Gen, 
	# 		"Jenis_Penjualan":self.Jenis_Penjualan, "no_telp":self.no_telp})

class Product(db.Model):
	id= db.Column(db.Integer, primary_key = True, autoincrement=True)
	id_product =db.Column(db.String(100), nullable=False)
	merk =  db.Column(db.String(100), nullable=False)
	price = db.Column(db.String(100))
	daerah = db.Column(db.String(100))
	file1 = db.Column(db.String(100), nullable=False)
	file2 =db.Column(db.String(100), nullable=True)
	spesifikasi = db.Column(db.String(255))
	id_adm = db.Column(db.Integer, db.ForeignKey("admin.id"))
	date_posted = db.Column(db.Date, default=datetime.today())

	# def __init__(self, id_product, merk,price, daerah, file1,file2, spesifikasi):
	# 	self.id_product = id_product
	# 	self.merk = merk
	# 	self.price = price
	# 	self.daerah = daerah
	# 	self.file1 = file1
	# 	self.file2 = file2
	# 	self.spesifikasi = spesifikasi

	# def toString(self):
	# 	return({"id_product":self.id_product, "merk":self.merk, "harga":self.price, "posisi":self.daerah,
	# 		"file1":self.file1, "file2":self.file2, "spesifikasi":self.spesifikasi})

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(255),nullable=False )
	password = db.Column(db.String(255), nullable=False)
	jenis_kelamin = db.Column(db.String(255))
	address = db.Column(db.String(255), nullable=False)
	# def __init__(self, name, password, jenis_kelamin, address):
	# 	self.name = name
	# 	self.password = password
	# 	self.jenis_kelamin = jenis_kelamin
	# 	self.address = address

	# def toString(self):
	# 	return({"nama":self.name, "password":self.password, "jenis_kelamin":self.jenis_kelamin, "address":self.jenis_kelamin})
