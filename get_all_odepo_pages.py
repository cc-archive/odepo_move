import mwclient
from io import page2line, line2page

extra_pages = [
    'Template:Organization',
    'Form:Organization',
    'Category:Organization',
    ]

def main(site = 'wiki.creativecommons.org', path = '/', 
         catname = 'Category:Organization'):
    site = mwclient.Site(site, path=path)
    cat = site.Pages[catname]
    for page_name in extra_pages:
        print page2line(unicode(page_name))
    for page_obj in cat:
        print page2line(page_obj.name)

if __name__ == '__main__':
    main()
