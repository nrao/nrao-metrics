from parser import Parser

def parse(filepath):
    return CoversheetParser().parse(filepath)

def fromstring(xml):
    return CoversheetParser().fromstring(xml)

class CoversheetParser(Parser):
    tag = 'proposal'

    multi_texts = (('scientific_categories', 'scientific_category',),
                   ('observing_types', 'observing_type',),
                   )

    texts = (('proposal_title',),
             ('abstract',),
             ('proposal_type',),
             ('joint_proposal',),
             ('rapid_response_type',),
             ('related_proposal',),
             ('other_observing_type',),
             ('dissertation_plan',),
             )

    attrs = (('legacy_id',),
             ('proposal_id',),
             ('create_date',),
             ('modify_date',),
             ('submit_date',),
             ('pi',),
             ('contact',),
             ('editor',),
             ('total_time',),
             )

    translation = {'scientific_category': 'categories',
                   }

    def fix(self, element_dict):
        return element_dict

test_xml = """<?xml version="1.0" encoding="UTF-8"?>
<query-result>
<coverSheet>
<proposal proposal_id="VLBA/09B-129" legacy_id="BM308" create_date="Jan 30, 2009" modify_date="Feb 2, 2009" submit_date="Feb 2, 2009" deadline_date="Feb 2, 2009" editor="11721" contact="11721" pi="11721" previous_proposal_ids="null" total_time="274.0 hour" processed="true" status="SUBMITTED">
  <proposal_title>Probing jet acceleration and collimation in stellar-mass compact objects</proposal_title>
  <dissertation_plan>no</dissertation_plan>
  <related_proposal>BM297/AM976</related_proposal>
  <scientific_categories>
    <scientific_category>Stellar</scientific_category>
    <scientific_category>Galactic</scientific_category>
  </scientific_categories>
  <abstract>Accreting stellar-mass black hole, neutron star and white dwarf systems all undergo occasional outburst episodes, in which they show similar, distinctive patterns of behaviour, leading us to infer that radio-emitting jets are present in all three types of system.  We propose a program of high-resolution VLBA monitoring of an outburst of each of the three classes of object, triggered by an X-ray or optical detection of an outburst, and a subsequent VLA radio detection via our joint VLA proposal.  These VLBA observations will directly resolve the evolution of the jets, and determine the similarities and differences in the jet properties and jet-disc coupling.  Together with simultaneous X-ray, optical and infrared monitoring, this will provide an unprecedented dataset with which to test the current paradigm for the jet-disc coupling, and, by comparing the three, to probe the importance of the depth of the gravitational potential well, the stellar surface and the stellar magnetic field, in the production, acceleration and collimation of jets.
</abstract>
  <support_request present="no" staff_support="None"/>
  <proposal_type>Large</proposal_type>
  <joint_proposal>Joint with VLA</joint_proposal>
  <observing_types>
    <observing_type>Continuum</observing_type>
    <observing_type>Monitoring</observing_type>
    <observing_type>Phase Referencing</observing_type>
    <observing_type>Triggered Transient</observing_type>
  </observing_types>
  <other_observing_type/>
  <scientific_technical_justification file_type="null" file_name="hid_proposal3.pdf" size="341504" id="3129-341504" date="Feb 2, 2009"/>
</proposal>
</coverSheet>
</query-result>"""

test_title = 'Probing jet acceleration and collimation in stellar-mass compact objects'
test_abstract = """Accreting stellar-mass black hole, neutron star and white dwarf systems all undergo occasional outburst episodes, in which they show similar, distinctive patterns of behaviour, leading us to infer that radio-emitting jets are present in all three types of system.  We propose a program of high-resolution VLBA monitoring of an outburst of each of the three classes of object, triggered by an X-ray or optical detection of an outburst, and a subsequent VLA radio detection via our joint VLA proposal.  These VLBA observations will directly resolve the evolution of the jets, and determine the similarities and differences in the jet properties and jet-disc coupling.  Together with simultaneous X-ray, optical and infrared monitoring, this will provide an unprecedented dataset with which to test the current paradigm for the jet-disc coupling, and, by comparing the three, to probe the importance of the depth of the gravitational potential well, the stellar surface and the stellar magnetic field, in the production, acceleration and collimation of jets.
"""

bare_xml = """<?xml version="1.0" encoding="UTF-8"?>
<query-result>
<coverSheet>
  <proposal />
</coverSheet>
</query-result>"""

test_dicts = [{'total_time': '274.0 hour', 'other_observing_type': '',
               'create_date': 'Jan 30, 2009', 'legacy_id': 'BM308',
               'proposal_title': test_title, 'abstract': test_abstract,
               'submit_date': 'Feb 2, 2009', 'proposal_type': 'Large',
               'categories': ['Stellar', 'Galactic'],
               'rapid_response_type': '', 'contact': '11721',
               'modify_date': 'Feb 2, 2009', 'editor': '11721',
               'observing_type': ['Continuum', 'Monitoring',
               'Phase Referencing', 'Triggered Transient'],
               'joint_proposal': 'Joint with VLA', 'pi': '11721',
               'dissertation_plan': 'no', 'proposal_id': 'VLBA/09B-129',
               'related_proposal': 'BM297/AM976'}]

def _test():
    """Testing:
    >>> bare_dicts = [{'total_time': '', 'other_observing_type': '',
    ...                'create_date': '', 'legacy_id': '',
    ...                'proposal_title': '', 'submit_date': '',
    ...                'categories': [], 'abstract': '',
    ...                'proposal_type': '', 'rapid_response_type': '',
    ...                'contact': '', 'modify_date': '', 'editor': '',
    ...                'observing_type': [], 'joint_proposal': '',
    ...                'dissertation_plan': '', 'proposal_id': '',
    ...                'pi': '', 'related_proposal': ''}]
    >>> fromstring(bare_xml) == bare_dicts
    True
    >>> fromstring(test_xml) == test_dicts
    True
    """
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
    if test_dicts != parse('coversheet/BM308.xml'):
        print '***Test Failed***', 'parsing coversheet/BM308.xml'
