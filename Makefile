all:
	make sync
	make serve

sync:
	virtualenv venv
	. venv/bin/activate
	pip install -r pip-req.txt

test:
	. venv/bin/activate
	python -m unittest discover

serve:
	. venv/bin/activate
	cat ./../../uwsgi.ini
	# python app.py

clean:
	rm -rf *.pyc
	rm -r venv/
