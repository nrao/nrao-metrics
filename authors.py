from parser import Parser

def parse(filepath):
    return AuthorsParser().parse(filepath)

def fromstring(xml):
    return AuthorsParser().fromstring(xml)

class AuthorsParser(Parser):
    texts = (('astronomer_id',),
             ('affiliation', 'zipcode'),
             ('country',),
             ('usstate',),
             ('affiliation', 'name'),
             )

    attrs = (('affiliation', 'domestic',),
             ('professional_status', 'type'),
             )

    translation = {'name': 'affiliation_name',
                   'type': 'professional_status_type',
                   }
    tag = 'author'

    def fix(self, element_dict):
        if element_dict['domestic'] == 'true':
            element_dict['country'] = 'United States'
        return element_dict

test_xml = """<?xml version="1.0" encoding="UTF-8"?>
<authors>
  <author  new_user="false">
    <astronomer_id>9141</astronomer_id>
    <username>jbraatz</username>
    <first_name>James</first_name>
    <last_name>Braatz</last_name>
    <affiliation domestic="true">
     <name>National Radio Astronomy Observatory</name>
      <zipcode>22903-2475</zipcode>
    </affiliation>
    <email>jbraatz@nrao.edu</email>
    <professional_status type="NRAO Staff">
       <phd_year>-1</phd_year>
       <observe_for_thesis>false</observe_for_thesis>
    </professional_status>
    <telephone>434-296-0251</telephone>
    <usstate>Virginia</usstate>
  </author>
</authors>
"""

bare_xml = """<?xml version="1.0" encoding="UTF-8"?>
<authors>
  <author />
</authors>
"""

def _test():
    """Testing:
    >>> bare_dicts = [{'usstate': '', 'country': '', 'domestic': '',
    ...                'astronomer_id': '', 'zipcode': '',
    ...                'professional_status_type': '', 'affiliation_name': ''}]
    >>> fromstring(bare_xml) == bare_dicts
    True
    >>> test_dicts = [
    ...              {'usstate': 'Virginia', 'country': 'United States',
    ...              'domestic': 'true', 'astronomer_id': '9141',
    ...              'zipcode': '22903-2475',
    ...              'professional_status_type': 'NRAO Staff',
    ...              'affiliation_name': 'National Radio Astronomy Observatory'
    ...              }
    ...              ]
    >>> fromstring(test_xml) == test_dicts
    True
    """
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
    authors = parse('author/AG826.xml')
