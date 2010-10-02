#!/usr/bin/env python

import cPickle
import glob
import os
import re

import authors
import coversheet

relevant_coversheet_keys = ('proposal_title', 'abstract', 'legacy_id',
                            'proposal_id', 'categories')
relevant_author_keys = ('last_name', 'first_name', 'affiliation_name', 'zipcode', 'usstate', 'country',)
rename_keys = {'proposal_title': 'title', 'affiliation_name': 'affiliation'}

def rename(key):
    return rename_keys.get(key, key)

def build(filenames):
    """Build a dict of dicts given filenames of xml files from PST.

    Assume: coversheet/ and author/ are local directories w/file named filename
    """
    need0_re = re.compile('^([A|B][A-Z])(\d\d\d)$')
    megadict = {}
    for filename in filenames:
        coversheet_info = coversheet.parse('coversheet/' + filename)[0]
        authors_info = authors.parse('author/' + filename)

        relevant = {}
        for key in relevant_coversheet_keys:
            relevant[rename(key)] = coversheet_info[key]

        pi = None
        pi_id = coversheet_info.get('pi', '-1')
        maybe_pi = [author for author in authors_info
                    if author.get('astronomer_id', '-2') == pi_id]
        if len(maybe_pi) > 0:
            pi = maybe_pi[0]

        investigators = []
        investigator_details = []

        for author_info in authors_info:
            author_relevant = {}
            for key in relevant_author_keys:
                author_relevant[rename(key)] = author_info[key]
            investigator_details.append(author_relevant)
            investigators.append('%s, %s (%s)' %
                                 (author_relevant['last_name'],
                                  author_relevant['first_name'],
                                  author_relevant['affiliation'],
                                  ))
            if author_info == pi:
                relevant['pi_details'] = author_relevant
        relevant['investigators'] = sorted(investigators)
        relevant['investigator_details'] = sorted(investigator_details)

        alt_id = relevant['proposal_id'].replace('/', '').replace('-', '_')
        megadict[relevant['proposal_id']] = relevant
        megadict[relevant['legacy_id']] = relevant
        megadict[alt_id] = relevant

        megadict[filename.replace('.xml', '')] = relevant

        if relevant['proposal_id'].startswith('GBT'):
            print relevant['proposal_id']
        else:
            leg_id = relevant['legacy_id']
            need0_match = need0_re.match(leg_id)
            if need0_match is not None:
                leg_id = '0'.join(need0_match.groups())
                megadict[leg_id] = relevant
            print leg_id

    return megadict

def dump(obj):
    return cPickle.dump(obj, open('proposals.dat', 'w'))

def load():
    return cPickle.load(open('proposals.dat', 'r'))

if __name__ == '__main__':
    import user
    os.chdir('coversheet')
    filenames = glob.glob('*.xml')
    os.chdir('..')
    dump(build(filenames))
