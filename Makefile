mytest: cookie.txt
	echo Hooray

cookie.txt: recent-cookie

recent-cookie: nraouserdb in-env
	./in-env ./set-cookie

nraouserdb: in-env
	./in-env easy_install -f 'http://www.cv.nrao.edu/~kgroner/python/#nraouserdb' nraouserdb
	touch nraouserdb

in-env: python-env
	echo '#!/bin/bash\n\nsource python-env/bin/activate\nexec $$@' > in-env
	chmod a+x in-env

python-env: virtualenv.py
	python virtualenv.py --no-site-packages --distribute python-env

virtualenv.py:
	wget http://bit.ly/virtualenv -O virtualenv.py

clean:
	rm -fr python-env virtualenv.py *.egg *.egg-info *.pyc cookie.txt in-env nraouserdb

.PHONY: recent-cookie
.SILENT: recent-cookie
