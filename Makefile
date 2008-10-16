all: import_manually

all_odepo_pages:
	python get_all_odepo_pages.py > all_odepo_pages.tmp
	mv all_odepo_pages.tmp all_odepo_pages

automatic_importable: all_odepo_pages
	python remove_pages_with_multiple_categories.py automatic_importable > \
		all_odepo_pages.tmp
	mv all_odepo_pages.tmp all_odepo_pages

import_manually: all_odepo_pages automatic_importable 
	diff all_odepo_pages automatic_importable | \
		grep '^< ' | sed 's/^< //' > import_manually.tmp
	mv import_manually.tmp import_manually

clean:
	rm -f all_odepo_pages automatic_importable import_manually *.tmp
