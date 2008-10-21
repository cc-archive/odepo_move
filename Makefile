PLAYGROUND:=$(shell mktemp -d data/tmpXX)
BBQ=$(PLAYGROUND)/bbq

all: data/just_interesting_pages_ccwiki_dump.xml

data/.stamp:
	mkdir -p data
	touch data/.stamp

data/all_odepo_pages: data/.stamp get_all_odepo_pages.py
	./bin/python get_all_odepo_pages.py > $(BBQ)
	mv -v $(BBQ) data/all_odepo_pages

data/automatic_importable: remove_pages_with_multiple_categories.py data/all_odepo_pages
	./bin/python remove_pages_with_multiple_categories.py data/all_odepo_pages > \
		$(BBQ)
	mv $(BBQ)  data/automatic_importable

data/import_manually: data/all_odepo_pages data/automatic_importable 
	diff data/all_odepo_pages data/automatic_importable | \
		grep '^< ' | sed 's/^< //' > $(BBQ)
	mv $(BBQ) data/import_manually

data/ccwiki_dump.xml:
	echo "You must give me a CC Wiki XML dump."
	exit 1

data/just_interesting_pages_ccwiki_dump.xml: data/all_odepo_pages
	python relevant_pages_filter.py data/all_odepo_pages < \
		data/ccwiki_dump.xml > $(BBQ)
	mv $(BBQ) data/just_interesting_pages_ccwiki_dump.xml

clean:
	rm -f data/all_odepo_pages data/automatic_importable data/import_manually data/*.tmp
