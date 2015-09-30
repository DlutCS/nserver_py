all:
	make sync
	make serve

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
	ifdef DEPLOYOUTPUTDIR
	sed -e 's/^chdir.*$//g' -e "s/\#gitbase=\(.*\)$/\#gitbase=\1\nchdir=\1$(DEPLOYOUTPUTDIR)/" ./../../uwsgi.ini
	else
	cat ./../../uwsgi.ini
	endif
	
	
	# python app.py

clean:
	rm -rf *.pyc
	rm -r venv/
