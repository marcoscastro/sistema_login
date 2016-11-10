from app import app
import os

if __name__ == '__main__':
	if os.environ.get('APP_LOCATION') == 'heroku':
		app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
	else:
		app.run(host='localhost', port=8080, debug=True, reloader=True)
