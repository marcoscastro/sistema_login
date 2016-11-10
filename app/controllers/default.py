from app import app
from app.models.tables import User
from bottle import template, static_file, request

# static routes
@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root='app/static/css')

@app.get('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='app/static/js')

@app.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='app/static/img')

@app.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
	return static_file(filename, root='app/static/fonts')

@app.route('/')
def login():
	return template('login')

@app.route('/cadastro')
def cadastro():
	return template('cadastro')

@app.route('/cadastro', method='POST')
def acao_cadastro(db):
	username = request.forms.get('username')
	password = request.forms.get('password')
	new_user = User(username, password)
	db.add(new_user)
	return template('verificacao_cadastro', nome=username)

@app.route('/', method='POST')
def acao_login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	return template('verificacao_login', sucesso=True)

@app.error(404)
def error404(error):
	return template('pagina404')
