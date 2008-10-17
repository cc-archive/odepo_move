all: import_manually

all_odepo_pages: get_all_odepo_pages.py
	./bin/python get_all_odepo_pages.py > all_odepo_pages.tmp
	mv all_odepo_pages.tmp all_odepo_pages

automatic_importable: remove_pages_with_multiple_categories.py all_odepo_pages
	./bin/python remove_pages_with_multiple_categories.py all_odepo_pages > \
		automatic_importable.tmp
	mv automatic_importable.tmp automatic_importable

import_manually: all_odepo_pages automatic_importable 
	diff all_odepo_pages automatic_importable | \
		grep '^< ' | sed 's/^< //' > import_manually.tmp
	mv import_manually.tmp import_manually

ccwiki_dump.xml:
	echo "You must give me a CC Wiki XML dump."
	exit 1



clean:
	rm -f all_odepo_pages automatic_importable import_manually *.tmp
