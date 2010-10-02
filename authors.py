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
             ('last_name',),
             ('first_name',),
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
<query-result>
<authors>
  <author new_user="false">
    <astronomer_id>11739</astronomer_id>
    <unique_id>493</unique_id>
    <account-name>rob.fender</account-name>
    <first_name>Robert</first_name>
    <last_name>Fender</last_name>
    <affiliation domestic="false">
     <name>Southampton, University of</name>
      <zipcode>S017 1BJ</zipcode>
    </affiliation>
    <email>rpf@phys.soton.ac.uk</email>
    <professional_status type="All Others">
       <phd_year>1996</phd_year>
       <observe_for_thesis>false</observe_for_thesis>
    </professional_status>
    <telephone>+442380592076</telephone>
    <country>United Kingdom</country>
  </author>
  <author new_user="false">
    <astronomer_id>11737</astronomer_id>
    <unique_id>2612</unique_id>
    <account-name>daverussell</account-name>
    <first_name>David</first_name>
    <last_name>Russell</last_name>
    <affiliation domestic="false">
     <name>Universiteit van Amsterdam</name>
      <zipcode>1098 SM</zipcode>
    </affiliation>
    <email>D.M.Russell@uva.nl</email>
    <professional_status type="All Others">
       <phd_year>-1</phd_year>
       <observe_for_thesis>false</observe_for_thesis>
    </professional_status>
    <telephone/>
    <country>Netherlands</country>
  </author>
  <author new_user="false">
    <astronomer_id>11724</astronomer_id>
    <unique_id>2557</unique_id>
    <account-name>RonaldRemillard</account-name>
    <first_name>Ronald</first_name>
    <last_name>Remillard</last_name>
    <affiliation domestic="true">
     <name>Massachusetts Institute of Technology</name>
      <zipcode>02139</zipcode>
    </affiliation>
    <email>rr@space.mit.edu</email>
    <professional_status type="All Others">
       <phd_year>-1</phd_year>
       <observe_for_thesis>false</observe_for_thesis>
    </professional_status>
    <telephone/>
    <usstate>Massachusetts</usstate>
  </author>
  <author new_user="false">
    <astronomer_id>11725</astronomer_id>
    <unique_id>1320</unique_id>
    <account-name>migliari</account-name>
    <first_name>Simone</first_name>
    <last_name>Migliari</last_name>
    <affiliation domestic="true">
     <name>California at San Diego, University of</name>
      <zipcode>2200 AG</zipcode>
    </affiliation>
    <email>migliari@ucsd.edu</email>
    <professional_status type="All Others">
       <phd_year>-1</phd_year>
       <observe_for_thesis>false</observe_for_thesis>
    </professional_status>
    <telephone>+1-858-534-8016</telephone>
  </author>
  <author new_user="false">
    <astronomer_id>11738</astronomer_id>
    <unique_id>64</unique_id>
    <account-name>mrupen</account-name>
    <first_name>Michael</first_name>
    <last_name>Rupen</last_name>
    <affiliation domestic="true">
     <name>National Radio Astronomy Observatory </name>
      <zipcode>87801</zipcode>
    </affiliation>
    <email>mrupen@nrao.edu</email>
    <professional_status type="NRAO Staff">
       <phd_year>-1</phd_year>
       <observe_for_thesis>false</observe_for_thesis>
    </professional_status>
    <telephone>505 835-7027</telephone>
    <usstate>New Mexico</usstate>
  </author>
  <author new_user="false">
    <astronomer_id>11736</astronomer_id>
    <unique_id>562</unique_id>
    <account-name>koerding</account-name>
    <first_name>Elmar</first_name>
    <last_name>Koerding</last_name>
    <affiliation domestic="false">
     <name>Commissariat a l'Energie Atomique </name>
      <zipcode>91191</zipcode>
    </affiliation>
    <email>elmar@koerding.eu</email>
    <professional_status type="All Others">
       <phd_year>-1</phd_year>
       <observe_for_thesis>false</observe_for_thesis>
    </professional_status>
    <telephone/>
    <country>France</country>
  </author>
  <author new_user="false">
    <astronomer_id>11722</astronomer_id>
    <unique_id>836</unique_id>
    <account-name>gsivakoff</account-name>
    <first_name>Gregory</first_name>
    <last_name>Sivakoff</last_name>
    <affiliation domestic="true">
     <name>Ohio State University</name>
      <zipcode>22903-0818</zipcode>
    </affiliation>
    <email>grs8g@virginia.edu</email>
    <professional_status type="All Others">
       <phd_year>2006</phd_year>
       <observe_for_thesis>false</observe_for_thesis>
    </professional_status>
    <telephone>614 292 2928</telephone>
    <usstate>Virginia</usstate>
  </author>
  <author new_user="false">
    <astronomer_id>11723</astronomer_id>
    <unique_id>901</unique_id>
    <account-name>Sarazin</account-name>
    <first_name>Craig</first_name>
    <last_name>Sarazin</last_name>
    <affiliation domestic="true">
     <name>Virginia, University of</name>
      <zipcode>22903-0818</zipcode>
    </affiliation>
    <email>sarazin@virginia.edu</email>
    <professional_status type="All Others">
       <phd_year>-1</phd_year>
       <observe_for_thesis>false</observe_for_thesis>
    </professional_status>
    <telephone>1-434-924-3104</telephone>
    <usstate>Virginia</usstate>
  </author>
  <author new_user="true">
    <astronomer_id>11740</astronomer_id>
    <unique_id>2820</unique_id>
    <account-name>SebastianHeinz</account-name>
    <first_name>Sebastian</first_name>
    <last_name>Heinz</last_name>
    <affiliation domestic="true">
     <name>Wisconsin at Madison, University of</name>
      <zipcode>53706</zipcode>
    </affiliation>
    <email>heinzs@astro.wisc.edu</email>
    <professional_status type="All Others">
       <phd_year/>
       <observe_for_thesis>false</observe_for_thesis>
    </professional_status>
    <telephone/>
    <usstate>Wisconsin</usstate>
  </author>
  <author new_user="false">
    <astronomer_id>11901</astronomer_id>
    <unique_id>433</unique_id>
    <account-name>serabm</account-name>
    <first_name>Sera</first_name>
    <last_name>Markoff</last_name>
    <affiliation domestic="false">
     <name>Universiteit van Amsterdam</name>
      <zipcode>1098 SM</zipcode>
    </affiliation>
    <email>s.b.markoff@uva.nl</email>
    <professional_status type="All Others">
       <phd_year>-1</phd_year>
       <observe_for_thesis>false</observe_for_thesis>
    </professional_status>
    <telephone>+31 20 525 7478</telephone>
    <country>Netherlands</country>
  </author>
  <author new_user="false">
    <astronomer_id>12002</astronomer_id>
    <unique_id>2863</unique_id>
    <account-name>dmaitra</account-name>
    <first_name>Dipankar</first_name>
    <last_name>Maitra</last_name>
    <affiliation domestic="false">
     <name>Universiteit van Amsterdam</name>
      <zipcode>1098 SM</zipcode>
    </affiliation>
    <email>D.Maitra@uva.nl</email>
    <professional_status type="All Others">
       <phd_year>-1</phd_year>
       <observe_for_thesis>false</observe_for_thesis>
    </professional_status>
    <telephone/>
    <country>Netherlands</country>
  </author>
  <author new_user="false">
    <astronomer_id>11721</astronomer_id>
    <unique_id>492</unique_id>
    <account-name>jcamj</account-name>
    <first_name>James</first_name>
    <last_name>Miller-Jones</last_name>
    <affiliation domestic="true">
     <name>National Radio Astronomy Observatory</name>
      <zipcode>22903-2475</zipcode>
    </affiliation>
    <email>jmiller@nrao.edu</email>
    <professional_status type="All Others">
       <phd_year>-1</phd_year>
       <observe_for_thesis>false</observe_for_thesis>
    </professional_status>
    <telephone>+1 434 244 6824</telephone>
    <usstate>Virginia</usstate>
  </author>

</authors>
</query-result>"""


test_dicts = [{'first_name': 'Robert', 'last_name': 'Fender', 'usstate': '',
               'country': 'United Kingdom', 'domestic': 'false',
               'astronomer_id': '11739', 'zipcode': 'S017 1BJ',
               'professional_status_type': 'All Others',
               'affiliation_name': 'Southampton, University of'},
              {'first_name': 'David', 'last_name': 'Russell', 'usstate': '',
               'country': 'Netherlands', 'domestic': 'false',
               'astronomer_id': '11737', 'zipcode': '1098 SM',
               'professional_status_type': 'All Others',
               'affiliation_name': 'Universiteit van Amsterdam'},
              {'first_name': 'Ronald', 'last_name': 'Remillard',
               'usstate': 'Massachusetts', 'country': 'United States',
               'domestic': 'true',
               'astronomer_id': '11724', 'zipcode': '02139',
               'professional_status_type': 'All Others',
               'affiliation_name': 'Massachusetts Institute of Technology'},
              {'first_name': 'Simone', 'last_name': 'Migliari',
               'usstate': '', 'country': 'United States',
               'domestic': 'true',
               'astronomer_id': '11725', 'zipcode': '2200 AG',
               'professional_status_type': 'All Others',
               'affiliation_name': 'California at San Diego, University of'},
              {'first_name': 'Michael', 'last_name': 'Rupen',
               'usstate': 'New Mexico', 'country': 'United States',
               'domestic': 'true',
               'astronomer_id': '11738', 'zipcode': '87801',
               'professional_status_type': 'NRAO Staff',
               'affiliation_name': 'National Radio Astronomy Observatory '},
              {'first_name': 'Elmar', 'last_name': 'Koerding',
               'usstate': '', 'country': 'France', 'domestic': 'false',
               'astronomer_id': '11736', 'zipcode': '91191',
               'professional_status_type': 'All Others',
               'affiliation_name': "Commissariat a l'Energie Atomique "},
              {'first_name': 'Gregory', 'last_name': 'Sivakoff',
               'usstate': 'Virginia', 'country': 'United States',
               'domestic': 'true',
               'astronomer_id': '11722', 'zipcode': '22903-0818',
               'professional_status_type': 'All Others',
               'affiliation_name': 'Ohio State University'},
              {'first_name': 'Craig', 'last_name': 'Sarazin',
               'usstate': 'Virginia', 'country': 'United States',
               'domestic': 'true',
               'astronomer_id': '11723', 'zipcode': '22903-0818',
               'professional_status_type': 'All Others',
               'affiliation_name': 'Virginia, University of'},
              {'first_name': 'Sebastian', 'last_name': 'Heinz',
               'usstate': 'Wisconsin', 'country': 'United States',
               'domestic': 'true',
               'astronomer_id': '11740', 'zipcode': '53706',
               'professional_status_type': 'All Others',
               'affiliation_name': 'Wisconsin at Madison, University of'},
              {'first_name': 'Sera', 'last_name': 'Markoff',
               'usstate': '', 'country': 'Netherlands', 'domestic': 'false',
               'astronomer_id': '11901', 'zipcode': '1098 SM',
               'professional_status_type': 'All Others',
               'affiliation_name': 'Universiteit van Amsterdam'},
              {'first_name': 'Dipankar', 'last_name': 'Maitra',
               'usstate': '', 'country': 'Netherlands', 'domestic': 'false',
               'astronomer_id': '12002', 'zipcode': '1098 SM',
               'professional_status_type': 'All Others',
               'affiliation_name': 'Universiteit van Amsterdam'},
              {'first_name': 'James', 'last_name': 'Miller-Jones',
               'usstate': 'Virginia', 'country': 'United States',
               'domestic': 'true',
               'astronomer_id': '11721', 'zipcode': '22903-2475',
               'professional_status_type': 'All Others',
               'affiliation_name': 'National Radio Astronomy Observatory'}
              ]

bare_xml = """<?xml version="1.0" encoding="UTF-8"?>
<authors>
  <author />
</authors>
"""

def _test():
    """Testing:
    >>> bare_dicts = [{'first_name': '', 'last_name': '', 'usstate': '',
    ...                'country': '', 'domestic': '', 'astronomer_id': '',
    ...                'zipcode': '', 'professional_status_type': '',
    ...                'affiliation_name': ''}]
    >>> fromstring(bare_xml) == bare_dicts
    True
    >>> fromstring(test_xml) == test_dicts
    True
    """
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
