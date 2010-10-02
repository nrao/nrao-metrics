from iso_data import countries

# http://www.maxmind.com/app/iso3166_2

iso_state = {'VA': "Virginia",
             # 'ISO': 'common',
             # 'AA': "Armed Forces Americas",
             # 'AE': "Armed Forces Europe, Middle East, & Canada",
             'AK': "Alaska",
             'AL': "Alabama",
             # 'AP': "Armed Forces Pacific",
             'AR': "Arkansas",
             # 'AS': "American Samoa",
             'AZ': "Arizona",
             'CA': "California",
             'CO': "Colorado",
             'CT': "Connecticut",
             'DC': "District of Columbia",
             'DE': "Delaware",
             'FL': "Florida",
             # 'FM': "Federated States of Micronesia",
             'GA': "Georgia",
             # 'GU': "Guam",
             'HI': "Hawaii",
             'IA': "Iowa",
             'ID': "Idaho",
             'IL': "Illinois",
             'IN': "Indiana",
             'KS': "Kansas",
             'KY': "Kentucky",
             'LA': "Louisiana",
             'MA': "Massachusetts",
             'MD': "Maryland",
             'ME': "Maine",
             # 'MH': "Marshall Islands",
             'MI': "Michigan",
             'MN': "Minnesota",
             'MO': "Missouri",
             # 'MP': "Northern Mariana Islands",
             'MS': "Mississippi",
             'MT': "Montana",
             'NC': "North Carolina",
             'ND': "North Dakota",
             'NE': "Nebraska",
             'NH': "New Hampshire",
             'NJ': "New Jersey",
             'NM': "New Mexico",
             'NV': "Nevada",
             'NY': "New York",
             'OH': "Ohio",
             'OK': "Oklahoma",
             'OR': "Oregon",
             'PA': "Pennsylvania",
             'PR': "Puerto Rico",
             # 'PW': "Palau",
             'RI': "Rhode Island",
             'SC': "South Carolina",
             'SD': "South Dakota",
             'TN': "Tennessee",
             'TX': "Texas",
             'UT': "Utah",
             # 'VI': "Virgin Islands",
             'VT': "Vermont",
             'WA': "Washington",
             'WV': "West Virginia",
             'WI': "Wisconsin",
             'WY': "Wyoming",
             }

state_iso = dict((v,k) for k, v in iso_state.items())

iso_country = dict()
country_iso = dict()

for record in countries:
    iso_country[record['code']] = record['name']
    country_iso[record['name']] = record['code']

# fixes
iso_country['TW'] = 'Taiwan'
country_iso['Taiwan'] = 'TW'
country_iso['Scotland'] = 'GB'

def _test():
    """Testing:
    >>> iso_state['OH']
    'Ohio'
    >>> state_iso['Ohio']
    'OH'
    >>> iso_country['US']
    'United States'
    >>> country_iso['United States']
    'US'
    >>> iso_country['DE']
    'Germany'
    >>> country_iso['Germany']
    'DE'
    >>> country_iso['Scotland']
    'GB'
    >>> country_iso['Taiwan']
    'TW'
    """
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
