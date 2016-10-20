from bottle import route, run
from bottle import request, template
from bottle import static_file, get
from bottle import error

'''
@route('/')
@route('/user/<nome>')
def index(nome='Desconhecido'):
	return '<center><h1>Olá ' + nome + '</h1></center>'

@route('/artigo/<id>')
def artigo(id):
	return '<h1>Você está lendo o artigo ' + id + '</h1>'

@route('/pagina/<id>/<nome>')
def pagina(id, nome):
	return '<h1>Você está vendo a página ' + id + ' com o nome ' + nome + '</h1>'
'''

# static routes
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root='static/css')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='static/js')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
	return static_file(filename, root='static/fonts')

@route('/login') # @get('/login')
def login():
	return template('login')

def check_login(username, password):
	d = {'marcos':'python', 'joao':'java', 'pedro':'go'}
	if username in d.keys() and d[username] == password:
		return True
	return False

@route('/login', method='POST') # @post('/login')
def acao_login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	return template('verificacao_login', sucesso=check_login(username, password), nome=username)

@error(404)
def error404(error):
	return template('pagina404')

if __name__ == '__main__':
	run(host='localhost', port=8080, debug=True, reloader=True)