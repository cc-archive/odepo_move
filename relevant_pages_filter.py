# Based on http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/265881
# Also based on Asheesh Laroia's http://www.asheesh.org/note/software/wikipedia-style-edits.html code
# That work is GPLv2 or later, and so is this.

import xml.dom.minidom
import sys
from io import line2page

# DOM: so inefficient yet so easy.

def main(good_pages_file, fd):
    # Set up stdout for Unicode output
    import codecs
    stdout = codecs.getwriter('utf-8')(sys.stdout)

    # Figure out which pages we like
    yummy = set()
    yummy.update( (line2page(line) for line in open(good_pages_file)) )

    dom = xml.dom.minidom.parse(fd)
    pages = dom.getElementsByTagName('page')
    for page in pages:
        title = page.getElementsByTagName('title')[0]
        if title.childNodes[0].data in yummy:
            pass # great
        else:
            print >> sys.stderr, 'sucka, deleting:', title.childNodes[0].data

            page.parentNode.removeChild(page)
    print >> stdout, dom.toxml()

if __name__ == '__main__':
    main(sys.argv[1], sys.stdin)
