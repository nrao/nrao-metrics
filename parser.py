from xml.etree import ElementTree
from xml.parsers.expat import ExpatError

import latscii

class Parser(object):
    """Base class for simple parsing of XML.
    This should be rewritten to use xpath.
    """
    texts = tuple()
    multi_texts = tuple()
    attrs = tuple()
    translation = dict()
    tag = 'doc'
    dicts = list()

    def __init__(self, xml='', filepath=''):
        if xml:
            self.fromstring(xml)
        elif filepath:
            self.parse(filepath)

    def parse(self, filepath):
        # TODO: preserve character encoding
        try:
            return self.fromstring(open(filepath).read().decode('latscii'))
        except ExpatError:
            self.xml = ''
            return []

    def fromstring(self, xml):
        self.xml = xml
        self.dicts = list()

        root = ElementTree.fromstring(self.xml)
        elements = root.getiterator(self.tag)

        for element in elements:
            # Build a dict from the element.
            element_dict = dict()
            element_dict = self.get_texts(element, element_dict)
            element_dict = self.get_multi_texts(element, element_dict)
            element_dict = self.get_attrs(element, element_dict)
            element_dict = self.fix(element_dict)
            self.dicts.append(element_dict)
        return self.dicts

    def fix(self, element_dict):
        return element_dict

    def get_xs(self, element, element_dict, function, arg_group):
        for args in arg_group:
            item_key = self.translation.get(args[-1], args[-1])
            element_dict[item_key] = function(element, *args)
        return element_dict

    def get_texts(self, element, element_dict):
        return self.get_xs(element, element_dict, self.get_text, self.texts)

    def get_text(self, element, *args, **kwargs):
        default = kwargs.get('default', '')
        multi_text = self.get_multi_text(element, *args, **kwargs)
        if len(multi_text) < 1:
            return default
        else:
            return multi_text[0]

    def get_multi_texts(self, element, element_dict):
        return self.get_xs(element, element_dict, self.get_multi_text, 
                           self.multi_texts)

    def get_multi_text(self, element, *args, **kwargs):
        default = kwargs.get('default', [])
        leaf = args[-1]
        args = args[:-1]
        try:
            for arg in args:
                element = element.find(arg)
            elements = element.findall(leaf)
            texts = [element.text or '' for element in elements]
        except AttributeError:
            texts = default
        return texts

    def get_attrs(self, element, element_dict):
        return self.get_xs(element, element_dict, self.get_attr, self.attrs)

    def get_attr(self, element, *args, **kwargs):
        default = kwargs.get('default', '')
        name = args[-1]
        args = args[:-1]
        try:
            for arg in args:
                element = element.find(arg)
            attr = element.get(name, default)
        except AttributeError:
            attr = default
        return attr

latscii.register_codec()

class TestParser(Parser):
    texts = (('field', 'language',),
             )
    multi_texts = (('field',),
                   )
    attrs = (('spam',),
             ('does', 'not', 'exist', 'nonexistent'),
             )
    translation = {'field': 'fields'}
    tag = 'item'

    def fix(self, element_dict):
        element_dict['fake'] = element_dict.pop('nonexistent', '')
        return element_dict

test_xml = """<?xml version="1.0" encoding="UTF-8"?>
<items>
  <item>
    <field>1</field>
    <field>2</field>
  </item>
  <item spam="eggs">
  </item>
  <item>
    <field><language>Python</language></field>
  </item>
  <item>

  </item>
</items>
"""

bare_xml = """<?xml version="1.0" encoding="UTF-8"?>
<doc />
"""

def _test():
    """Testing:
    >>> TestParser().fromstring(bare_xml)
    []
    >>> dicts = [{'fields': ['1', '2'], 'fake': '', 'language': '', 'spam': ''},
    ...          {'fields': [], 'fake': '', 'language': '', 'spam': 'eggs'},
    ...          {'fields': [''], 'fake': '', 'language': 'Python', 'spam': ''},
    ...          {'fields': [], 'fake': '', 'language': '', 'spam': ''},
    ...          ]
    >>> TestParser().fromstring(test_xml) == dicts
    True
    """
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
