# Create projects.csv as input!
all: projects.csv projects_pi.csv projects_categories.csv projects_countries_pi.csv

projects.csv:
	echo create projects.csv as input
	echo with columns 'tel,legacy_id,proposal_id,hours'

projects_pi.csv: projects_distinct.csv projects_collected.csv proposals
	./project.py pi > projects_pi.csv

projects_categories.csv: projects_distinct.csv projects_collected.csv proposals
	./project.py category > projects_categories.csv

projects_countries_pi.csv: projects_pi.csv
	./geo_breakdown.py

projects_distinct.csv: projects.csv
	./project.py accumulate > projects_distinct.csv

maps: in-env googlechart projects_pi.csv
	./in-env ./geo_breakdown_maps.py

remove_empty: # Removes empty proposal files, matching *_empty.xml.
	./remove_empty.sh

proposals: cookie.txt
	./project.py get

cookie.txt: recent-cookie

recent-cookie: nraouserdb in-env
	./in-env ./set-cookie

nraouserdb: in-env
	./in-env easy_install -f 'http://www.cv.nrao.edu/~kgroner/python/#nraouserdb' nraouserdb
	touch nraouserdb

googlechart: in-env
	./in-env easy_install pygooglechart
	touch googlechart

in-env: python-env
	echo '#!/bin/bash\n\nsource python-env/bin/activate\nexec $$@' > in-env
	chmod a+x in-env

python-env: virtualenv.py
	python virtualenv.py --no-site-packages --distribute python-env

virtualenv.py:
	wget http://bit.ly/virtualenv -O virtualenv.py

clean:
	rm -fr python-env virtualenv.py *.egg *.egg-info *.pyc cookie.txt in-env nraouserdb author coversheet

.PHONY: recent-cookie
.SILENT: recent-cookie projects.csv
