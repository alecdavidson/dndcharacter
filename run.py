import os
from server import app

port = int(os.environ.get('PORT', 33507))

@app.route('/.well-known/pki-validation/AC0212261B5BDB1C7517E4C11DB3C970.txt')
def showhash():
	return 'EBCB539DC61ACC1556AA522E17F961336102B3CCA259507C64DACFE29A2F0BDC comodoca.com'
	
app.debug = True
app.run(host='0.0.0.0', port=port)
