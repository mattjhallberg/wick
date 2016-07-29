from django.shortcuts import render, redirect
from .models import User
import bcrypt


def index(request):

	return render(request, 'entry/users.html')


def login(request):
	if request.method == "POST":
		username = request.POST["username"]
		userPassword = request.POST["password"]
		if(len(username) < 2 or len(userPassword) < 8):
			print("Username or Password is invalid.")
			return redirect('/entry')
		user = User.objects.filter(username = username)
		if not user:
			print("Invalid Username.")
			return redirect('/entry')
		else:
			user = user[0]
			if bcrypt.hashpw(userPassword.encode(), user.password.encode()) == user.password.encode():
				request.session['user_id'] = user.id
				request.session['name'] = user.name
				print("Welcome!")
				return redirect('/')
			else:
				print("Invalid Password.")
	return redirect('/entry')

def register(request):
	if request.method == "POST":
		username = request.POST["username"]
		userExists = User.objects.filter(username = username)
		if userExists:
			print "Pick a different username!"
			return redirect('/entry')
		else:
			name = request.POST["name"]
			userPassword = request.POST["password"]
			c_password = request.POST["c_password"]
		if(len(username) < 2 or len(name) < 2 or len(userPassword) < 8):
			print("Invalid Info")
			return redirect('/entry')
		if(userPassword != c_password):
			print("Password does not match.")
			return redirect('/entry')
		if not'username' in request.session:
			request.session['username'] = username
		if not'name' in request.session:
			request.session['name'] = name
		if not'password' in request.session:
			hashed = bcrypt.hashpw(userPassword.encode(), bcrypt.gensalt())
			new_user = User.objects.create(
			username = username,
			name = name,
			password = hashed,
			user_level = 1)
			print new_user.username
			print new_user.name
			print new_user.password
			print User.objects.all()
			request.session['user_id'] = new_user.id
			return redirect('/')
	return redirect('/entry')