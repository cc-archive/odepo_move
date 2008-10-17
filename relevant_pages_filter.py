# Based on http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/265881
# Also based on Asheesh Laroia's http://www.asheesh.org/note/software/wikipedia-style-edits.html code
# That work is GPLv2 or later, and so is this.
from xml.sax.saxutils import XMLFilterBase

def do_nothing_when_appropriate(fn):
    def new_fn(*args, **kwargs):
        if args:
            self = args[0]
        else:
            self = kwargs['self']
        if self.do_nothing:
            return
        fn(*args, **kwargs)

class RelevantPagesFilter(XMLFilterBase):
    """
    SAX filter to ensure that contiguous white space nodes are
    delivered merged into a single node
    """
    
    def __init__(self, upstream, downstream, text_filter, okay_titles = None,
                 manualOverride = False):
        XMLFilterBase.__init__(self, upstream)
        self._downstream = downstream
        self._accumulator = []
        self.growing_page_title = False
        self.do_nothing = False
        self.text_filter = text_filter
        self.should_filter = False
        self.okay_titles = set(okay_titles)
	self.manualOverride = manualOverride # Set this to True if you want text_filter never to run

    def _complete_text_node(self):
        if self._accumulator:
            text = ''.join(self._accumulator)
            self._accumulator = []
            if self.should_filter and not self.manualOverride:
                text = self.text_filter(text).strip()
            if self.growing_page_title:
                self.growing_page_title = False
                # Check if it's a title we care about.
                # If so, great, we'll keep going.
                if text in self.okay_titles:
                    assert not self.do_nothing
                    pass
                else:
                    # It's not something we care about.  Ditch it.
                    self.do_nothing = True
                    return # get outta here before downstream gets the chars
            if not self.do_nothing:
                self._downstream.characters(text)
        return

    def startElement(self, name, attrs):
        self._complete_text_node()
        if name == 'text':
            self.should_filter = True
        if name == 'page':
            self.growing_page_title = True
        self._downstream.startElement(name, attrs)
        return

    def startElementNS(self, name, qname, attrs):
        self._complete_text_node()
        self._downstream.startElementNS(name, qname, attrs)
        return

    def endElement(self, name):
        self._complete_text_node()
        self._downstream.endElement(name)
        self.should_filter = False
        return

    def endElementNS(self, name, qname):
        self._complete_text_node()
        self._downstream.endElementNS(name, qname)
        return

    def processingInstruction(self, target, body):
        self._complete_text_node()
        self._downstream.processingInstruction(target, body)
        return

    def comment(self, body):
        self._complete_text_node()
        self._downstream.comment(body)
        return

    def characters(self, text):
        self._accumulator.append(text)
        return

    def ignorableWhitespace(self, ws):
        self._accumulator.append(text)
        return


sub = lambda thing: thing
if __name__ == "__main__":
    import sys
    from xml import sax
    from xml.sax.saxutils import XMLGenerator
    parser = sax.make_parser()
    #XMLGenerator is a special SAX handler that merely writes
    #SAX events back into an XML document
    downstream_handler = XMLGenerator(encoding='utf-8')
    #upstream, the parser, downstream, the next handler in the chain
    filter_handler = RelevantPagesFilter(parser, downstream_handler, sub, 
                                         okay_titles=['CcWiki:About'])
    #The SAX filter base is designed so that the filter takes
    #on much of the interface of the parser itself, including the
    #"parse" method
    filter_handler.parse(sys.argv[1])
