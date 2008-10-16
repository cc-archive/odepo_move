# -*- coding: utf-8 -*-

import base64

def page2line(u):
    assert type(u) == unicode
    return base64.b64encode(u.encode('utf-8'))

def line2page(s):
    '''
    >>> u = u'Frédéric'
    >>> line2page(page2line(u)) == u
    True
    '''
    assert type(s) == str
    return unicode(base64.b64decode(s), 'utf-8')

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
