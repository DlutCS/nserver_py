all:
	make sync
	make serve

sync:
	virtualenv venv
	. venv/bin/activate 
	pip install -r pip-req.txt

serve:
	. venv/bin/activate
	cat ./../../uwsgi.ini
	#python flaskr.py

