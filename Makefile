all:
	make sync
	make serve

database:
	#把生产数据库配置复制到指定位置

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
