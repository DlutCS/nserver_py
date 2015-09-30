all:
	make sync
ifdef DEPLOYOUTPUTDIR
	make prod_serve
else
	make serve
endif

database:
	#把生产数据库配置复制到指定位置
	# if $SERVERMODE == "PROD" then replace database.ini

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
	
prod_serve:
	. venv/bin/activate
	sed -e 's,^chdir.*$*,chdir=$(DEPLOYOUTPUTDIR),g' ./../../uwsgi.ini > ./../../uwsgi.ini
	kill `pidof uwsgi`

clean:
	rm -rf *.pyc
	rm -r venv/
