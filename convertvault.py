import logging
from bottle import Bottle, run, request, static_file, template, HTTPResponse
from convertion import Convert

app = Bottle()
logging.basicConfig(level=logging.ERROR)

@app.route('/static/css/<filename:re:.*\.css>')
def static(filename):
    return static_file(filename, root='static/css')

@app.route('/static/img/<filename:re:.*\.svg>')
def static(filename):
    return static_file(filename, root='static/img')

@app.get('/')
@app.post('/')
def index():
    logging.debug("Request route / ")
    password = request.forms.get('vaultpassword', '').strip()
    source = request.forms.get('source', '').strip()
    conv = Convert(password)
    data = conv.convert(source)
    return template('convert_template', data)

@app.get('/health')
def health():
    return HTTPResponse(status=200)

@app.error(404)
def error404(error):
    return 'Nothing here, sorry'

if __name__ == '__main__':
    import settings
    logging.basicConfig(level=logging.DEBUG)
    run(app, host='0.0.0.0', port=settings.PORT, reloader=settings.RELOAD, debug=settings.DEBUG, server='gunicorn')
