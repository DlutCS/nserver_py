all:
	make sync
ifdef PRODUCTION
	make prod_serve

else
ifdef PRELEASE
	make prelease_serve
else
	make serve
endif
endif

database:
	#把生产数据库配置复制到指定位置
	# if $SERVERMODE == "PROD" then replace database.ini

sync:
	virtualenv venv
	. venv/bin/activate; \
	pip install -r pip-req.txt
	
test:
	. venv/bin/activate; \
	export CONFIG_FILE='./default.cfg'; \
	python -m unittest discover
	

serve:
	. venv/bin/activate; \
	export CONFIG_FILE='./default.cfg'; \
	python app.py 
	
	
prod_serve:
	export CONFIG_FILE='./../prod.cfg'; \
	supervisorctl restart uwsgi_py

prelease_serve:
	export CONFIG_FILE='./default.cfg'; \
	supervisorctl restart uwsgi_dev_py

clean:
	rm -rf *.pyc
	rm -rf venv/
