PLAYGROUND:=$(shell mktemp -d data/tmpXX)
BBQ=$(PLAYGROUND)/bbq

all: data/import_manually

data:
	mkdir data

data/all_odepo_pages: data get_all_odepo_pages.py
	./bin/python get_all_odepo_pages.py > $(BBQ)
	mv $(BBQ) data/all_odepo_pages

data/automatic_importable: remove_pages_with_multiple_categories.py data/all_odepo_pages
	./bin/python remove_pages_with_multiple_categories.py data/all_odepo_pages > \
		$(BBQ)
	mv $(BBQ)  automatic_importable

data/import_manually: data/all_odepo_pages data/automatic_importable 
	diff data/all_odepo_pages data/automatic_importable | \
		grep '^< ' | sed 's/^< //' > $(BBQ)
	mv $(BBQ) import_manually

data/ccwiki_dump.xml:
	echo "You must give me a CC Wiki XML dump."
	exit 1

data/just_interesting_pages_ccwiki_dump.xml: data/import_manually
	python 

clean:
	rm -f data/all_odepo_pages data/automatic_importable data/import_manually data/*.tmp
