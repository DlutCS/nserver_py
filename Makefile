all:
ifdef PRODUCTION
	make server_sync
	make prod_serve
else
ifdef PRELEASE
	make server_sync
	make prelease_serve
else
	make sync
	make serve
endif
endif

database:
	#把生产数据库配置复制到指定位置
	# if $SERVERMODE == "PROD" then replace database.ini

sync:
	virtualenv venv --python=python2.7
	. venv/bin/activate; \
	pip install -r pip-req.txt

server_sync:
	virtualenv ../venv --python=python2.7
	. ../venv/bin/activate; \
	pip install -r pip-req.txt
	
test:
	. venv/bin/activate; \
	python -m unittest discover
	

serve:
	. venv/bin/activate; \
	python app.py 
	
	
prod_serve:
	ln -sf ../prod.cfg ./default.cfg
	supervisorctl restart uwsgi_py

prelease_serve:
	supervisorctl restart uwsgi_dev_py

clean:
	rm -rf *.pyc
	rm -rf venv/
