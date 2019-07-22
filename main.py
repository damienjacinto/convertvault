import logging
from bottle import route, run, request, error, static_file, template, post, get, default_app, HTTPResponse
from convertion import Convert

@route('/static/css/<filename:re:.*\.css>')
def static(filename):
    return static_file(filename, root='static/css')

@route('/static/img/<filename:re:.*\.svg>')
def static(filename):
    return static_file(filename, root='static/img')

@get('/')
@post('/')
def index():
    logging.debug("Request route / ")
    password = request.forms.get('vaultpassword', '').strip()
    source = request.forms.get('source', '').strip()
    conv = Convert(password)
    data = conv.convert(source)
    return template('convert_template', data)

@get('/health')
def health():
    return HTTPResponse(status=200)

@error(404)
def error404(error):
    return 'Nothing here, sorry'

if __name__ == '__main__':
    import settings
    logging.basicConfig(level=logging.DEBUG)
    run(host='0.0.0.0', port=settings.PORT, reloader=settings.RELOAD, debug=settings.DEBUG, server='gunicorn')

logging.basicConfig(level=logging.ERROR)
app = default_app()