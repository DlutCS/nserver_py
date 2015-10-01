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
	. venv/bin/activate
	pip install -r pip-req.txt
	deactivate

test:
	. venv/bin/activate
	python -m unittest discover

serve:
	. venv/bin/activate
	python app.py
	
prod_serve:
	. venv/bin/activate
	supervisorctl restart uwsgi_py
	#cat ./../../uwsgi.ini
	#sed -e 's,^chdir.*$$,chdir=$(DEPLOYOUTPUTDIR),g' ./../../uwsgi.ini.default > ./../../uwsgi.ini
	#kill `pidof uwsgi`

prelease_serve:
	. venv/bin/activate
	supervisorctl restart uwsgi_dev_py

clean:
	rm -rf *.pyc
	rm -r venv/
