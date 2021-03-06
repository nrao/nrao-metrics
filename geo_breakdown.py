#!/usr/bin/env python

import copy
import csv
import iso

for mode in ('pi',):
    # build base dictionary of states
    base_states = dict(zip(iso.iso_state.keys(), [0] * len(iso.iso_state.keys())))
    base_states[''] = 0

    # build base dictionary of countries
    base_countries = dict()
    for record in csv.DictReader(open('projects_' + mode + '.csv')):
        base_countries[record.get('iso_country', '')] = 0

    state_list = sorted(base_states.keys())
    country_list = sorted(base_countries.keys())

    # build containers for each telescope
    telescopes = ('GBT', 'VLA', 'VLBA', '', 'all',)
    states = dict()
    countries = dict()

    for tel in telescopes:
        states[tel] = copy.deepcopy(base_states)
        countries[tel] = copy.deepcopy(base_countries)

    # Collect data
    for record in csv.DictReader(open('projects_' + mode + '.csv')):
        state = record.get('iso_state', '')
        country = record.get('iso_country', '')
        tel = record.get('tel', '')

        quarter = (float(record['hours']))
        if country == 'US':
            states[tel][state] = states[tel].get(state, 0) + quarter
            states['all'][state] = states['all'].get(state, 0) + quarter
        countries[tel][country] = countries[tel].get(country, 0) + quarter
        countries['all'][country] = countries['all'].get(country, 0) + quarter

    # write data to file
    country_file = open('projects_countries_' + mode + '.csv', 'w')
    country_file.write('tel,iso_country,q4\n')
    country_writer = csv.writer(country_file)
    for tel in telescopes:
        for country in country_list:
            country_writer.writerow([tel, country,
                                     '%.02f' % countries[tel][country]])
