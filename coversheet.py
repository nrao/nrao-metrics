from parser import Parser

def parse(filepath):
    return CoversheetParser().parse(filepath)

def fromstring(xml):
    return CoversheetParser().fromstring(xml)

class CoversheetParser(Parser):
    multi_texts = (('scientific_categories', 'scientific_category',),)

    attrs = (('legacy_id',),
             ('proposal_id',),
             ('pi',),
             )

    translation = {'scientific_category': 'categories',
                   }
    tag = 'proposal'

    def fix(self, element_dict):
        return element_dict

test_xml = """<?xml version="1.0" encoding="UTF-8"?>
<coverSheet>
<proposal proposal_id="VLBA/09B-129"
 legacy_id="BM308"
 create_date="Jan 30, 2009"
 modify_date="Feb 2, 2009"
 submit_date="Feb 2, 2009"
 deadline_date="Feb 2, 2009"
 editor="11721"
 contact="11721"
 pi="11721"
 previous_proposal_ids="null"
 total_time="274.0 hour"
 processed="true"
 status="SUBMITTED">
  <proposal_title>Probing jet acceleration and collimation in stellar-mass compact objects</proposal_title>
  <dissertation_plan>no</dissertation_plan>
  <related_proposal>BM297/AM976</related_proposal>
  <scientific_categories>
    <scientific_category>Stellar</scientific_category>
    <scientific_category>Galactic</scientific_category>
  </scientific_categories>
</proposal>
</coverSheet>
"""

bare_xml = """<?xml version="1.0" encoding="UTF-8"?>
<coverSheet>
  <proposal />
</coverSheet>
"""

def _test():
    """Testing:
    >>> bare_dicts = [{'proposal_id': '', 'legacy_id': '',
    ...                'pi': '', 'categories': []}]
    >>> fromstring(bare_xml) == bare_dicts
    True
    >>> test_dicts = [{'proposal_id': 'VLBA/09B-129', 'legacy_id': 'BM308',
    ...                'pi': '11721', 'categories': ['Stellar', 'Galactic']}]
    >>> fromstring(test_xml) == test_dicts
    True
    """
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
    coversheet = parse('coversheet/AG826.xml')
