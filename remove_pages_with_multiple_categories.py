import mwclient
from io import page2line, line2page

def main(infile, site = 'wiki.creativecommons.org', path = '/', 
         catname = 'Category:Organization'):
    site = mwclient.Site(site, path=path)
    for line in infile:
        page = line2page(line)
        page_obj = site.Pages[page]
        if len(list(page_obj.categories())) == 1:
            print page2line(page)

if __name__ == '__main__':
    import sys
    main(open(sys.argv[1]))
