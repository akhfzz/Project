from flask import Flask, render_template, url_for, request, redirect, session, flash, jsonify
from passlib.hash import sha256_crypt
from Prosses.models import Admin, Product, User
from Prosses.__init__ import app, engine, dbs, db
from Prosses import __init__
from flask_login import login_user, logout_user, login_required, current_user

#masuk ke papan user
@app.route("/user", methods=["POST","GET"])
def Page():
	if "user" in session:
		user = session["user"]
		nomer = Admin.query.all()
		page = request.args.get("page", 1, type=int)
		shown = Product.query.paginate(page=page, per_page=8)
		return render_template("inti.html", user=user, post=shown, no=nomer)
	else:
		return redirect("/login")

#masuk ke papan login user
@app.route("/login", methods=["POST","GET"])
def login():
	if request.method == "POST":
	# 	user = request.form.get("name")
	# 	password = request.form.get("password")

		user = request.form.get("name")
		password = request.form.get("password")

		session["user"]=user

		users = dbs.execute("SELECT name FROM user WHERE name='{0}'".format(user)).fetchone()
		psw = dbs.execute("SELECT password FROM user WHERE name='{0}'".format(user)).fetchone()

		if users is None:
			flash("Kamu, Daftar dulu ya", "warning")
			return redirect("/Register")	
		else:
			for acc in psw:
				if sha256_crypt.verify(password, acc):
					return redirect("/user")
				else:
					flash(f"Password Belum dikenali oleh Sistem","warning")
					return redirect("/login")
	return render_template("Login.html")

#masuk ke papan login admin
@app.route("/admin", methods=["POST","GET"])
def admin():
	if request.method == "POST":
		admin = request.form.get("Nama")
		password = request.form.get("Password")
		remember = True if request.form.get("remember") else False
		usr = Admin.query.filter_by(Nama=admin).first()

		users = dbs.execute("SELECT Nama FROM admin WHERE Nama='{0}'".format(admin)).fetchone()
		psw = dbs.execute("SELECT Password FROM admin WHERE Nama='{0}'".format(admin)).fetchone()


		if users is None:
			flash(f"Kamu, Daftar dulu ya", "warning")
			return redirect("/register")
		else:
			for acc in psw:
				if sha256_crypt.verify(password, acc):
					login_user(usr, remember=remember)
					return redirect("/product")
					break
				else:
					flash(f"Password Belum dikenali oleh Sistem","warning")
					return redirect("/register")
					break
		
		login_user(usr, remember=remember)
		return redirect("/post")

	return render_template("admin.html")

#register user
@app.route("/Register", methods=["POST","GET"])
def register():
	if request.method == "POST":
		name = request.form.get("name")
		password = request.form.get("password")
		secure = sha256_crypt.encrypt(str(password))
		jenis = request.form.get("jenis_kelamin")
		alamat = request.form.get("address")

		check_user = User.query.filter_by(name=name).first()

		if check_user:
			flask(f"Kamu sudah terdaftar")
			return redirect("/login")

		new_user = User(name=name, password=secure, jenis_kelamin=jenis, address=alamat)
		db.session.add(new_user)
		db.session.commit()
		flash(f"Registrasi kamu berhasil!!","success")
		return redirect("/login")

	return render_template("form.html")	

#register admin
@app.route("/register", methods=["POST","GET"])
def registAdm():
	if request.method == "POST" :
		Nama = request.form.get("Nama")
		Password = request.form.get("Password")
		# secure = sha256_crypt.encrypt(str(Password))
		gen = request.form.get("Gen")
		jenis = request.form.get("Jenis_Penjualan")
		no = request.form.get("no_telp")
		check_admin = Admin.query.filter_by(Nama=Nama).first()
		if check_admin:
			flash(f"Kamu sudah terdaftar")
			return redirect("/admin")
		else:
			new_admin = Admin(Nama=Nama, Password=sha256_crypt.encrypt(str(Password)), Gen=gen, Jenis_Penjualan=jenis, no_telp=no)
			db.session.add(new_admin)
			db.session.commit()
	# if usr is None:
	# 	query = Admin_app(Nama, secure, gen, jenis, no)
	# 	db.session.add(query)
	# 	db.session.commit()
	# 	flash(f"Registrasi kamu berhasil!!","success")
	# 	return redirect("/papan-admin")
	# else:
	# 	flash(f"Kamu sudah terdaftar","warning")
	# 	return redirect("/admin")
		flash(f"Registrasi kamu berhasil!!","success")
		return redirect("/post")	


	return render_template("admin.html")	

#halaman first
@app.route("/")
def firstly():
	return render_template("first.html")

#to admin
@app.route("/admin")
def adminpage():
	return("admin.html")

#logout
@login_required
@app.route("/Logout")
def logout():
	# session.pop("user", None)
	logout_user()
	flash(f"Kamu berhasil keluar","success")
	return redirect("/Login-user-admin")

#papan developer
@app.route("/See-me")
def lookfor():
	return render_template("kontak.html")

#papan akses
@app.route("/Login-user-admin")
def userLogin():
	return render_template("choice.html")


#Post admin
@login_required
@app.route("/post", methods=["POST","GET"])
def postpro():
	if request.method == "POST":
		# session["user"] = user
		ID = request.form.get("id_product")
		merk = request.form.get("merk")
		harga = request.form.get("price")
		posisi = request.form.get("daerah")
		gambar1 = request.form.get("file1")
		gambar2 = request.form.get("file2")
		spesifikasi = request.form.get("spesifikasi")
		queri =  dbs.execute("SELECT id_product FROM product WHERE id_product='{0}'".format(ID)).fetchone()
		if queri:
			flash(f"File sudah dipost")
			return redirect("/product")

		if current_user.is_authenticated:
			query = Product(id_product=ID,merk=merk,price=harga,daerah=posisi,file1=gambar1,file2=gambar2,spesifikasi=spesifikasi, author=current_user)
			db.session.add(query)
			db.session.commit()
			flash(f"File success uploaded","success")
			return redirect("/all")
		else:
			flash(f'Server gagal meresponse', 'warning')
		
	return render_template("postadmin.html")



#shown product
@login_required
@app.route("/all")
def post():
	post = Product.query.all()
	page = request.args.get("page", 1, type=int)
	shown = Product.query.paginate(page=page, per_page=8)
	return render_template("postadmin.html", posts=shown, target="file")		

#shown table
@login_required
@app.route("/product")
def product_all():
	page = request.args.get("page", 1, type=int)
	post = Product.query.paginate(page=page, per_page=8)
	queries = Product.query.all()
	return render_template("all_produk.html", post=post, target="file")

@login_required
@app.route("/delete/<id>", methods=["POST", "GET"])
def delete(id):
	produk = Product.query.filter_by(id=id).first()
	if not produk:
		abort(404)
	db.session.delete(produk)
	db.session.commit()
	flash(f"Kamu berhasil menghapus", "success")
	return redirect("/product")

# @login_required
# @app.route("/update", methods=["POST","GET"])
# def update():
# 	if request.method == "POST":
# 		my_data = Product.query.get(request.form.get("id_product"))
# 		my_data.merk = request.form.get("merk")
# 		my_data.price =  request.form.get("price")
# 		my_data.file1 =  request.form.get("file1")
# 		my_data.file2 =  request.form.get("file2")
# 		my_data.spesifikasi = request.form.get("spesifikasi")
# 		db.session.commit()
# 		flash(f"Data telah di update", "info")
# 		return redirect("/all")

#mencari di page admin
@app.route("/search", methods=["POST","GET"])
def searching():
	found = Product.query.filter_by(merk=request.form["search"]).first()
	return redirect("/product")

#mencari di page user
@app.route("/cari", methods=["POST","GET"])
def cariProduk():
	found = Product.query.filter_by(merk=request.form["search"]).first()
	return redirect("/user")

