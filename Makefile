all:
	make sync
	make server
	
sync:
	virtualenv venv
	source venv/bin/activate 
	pip install -r pip-req.txt

serve:
	source venv/bin/activate
	#python flaskr.py

