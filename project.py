#!/usr/bin/env python
# This file is simply meant to give structure to otherwise throwaway code.

import copy
import csv
import subprocess
import sys

import authors
import coversheet
import iso

from authors_found import project as get_missing_author

months = ('hours',)

project_fields = ['tel', 'legacy_id', 'proposal_id'] + list(months)
author_fields = project_fields + ['astronomer_id', 'professional_status_type',
                                  'affiliation_name', 'country', 'domestic',
                                  'usstate', 'iso_country', 'iso_state',
                                  'zipcode']
category_fields = project_fields + ['category']

def write_projects(projects, openfile=sys.stdout, fieldnames=[]):
    if len(projects) > 0:
        fieldnames += [k for k in projects[0].keys() if k not in fieldnames]
    openfile.write(','.join(fieldnames) + '\n')
    writer = csv.DictWriter(openfile, fieldnames)
    writer.writerows(projects)

def accumulate_projects(filepath='projects.csv'):
    return _accumulate_projects(open(filepath))

def _accumulate_projects(openfile=sys.stdin):
    """Accumulate monthly hours where there exists multiple rows with same id.

    This is useful for a first pass on the data to ensure 1 row per project.
    """
    project_template = {'tel': '', 'legacy_id': '', 'proposal_id': ''}
    for month in months:
        project_template[month] = 0.0
    projects = get_projects(openfile)
    acc = {'VLA': {}, 'VLBA': {}, 'GBT': {}}
    for project in projects:
        telescope = project['tel']
        legacy_id = project['legacy_id']
        proposal_id = project.get('proposal_id', '')
        project_id = legacy_id or proposal_id
        if not acc[telescope].has_key(project_id):
            acc[telescope][project_id] = copy.deepcopy(project_template)
            acc[telescope][project_id]['tel'] = telescope
            acc[telescope][project_id]['legacy_id'] = legacy_id
            acc[telescope][project_id]['proposal_id'] = proposal_id
        for month in months:
            acc[telescope][project_id][month] += float(project[month])
            sum = acc[telescope][project_id][month]
            if int(sum) == float(sum):
                acc[telescope][project_id][month] = int(sum)
    vla_project_ids = sorted(acc['VLA'].keys())
    vlba_project_ids = sorted(acc['VLBA'].keys())
    gbt_project_ids = sorted(acc['GBT'].keys())
    write_projects([acc['VLA'][key] for key in vla_project_ids] +
                   [acc['VLBA'][key] for key in vlba_project_ids] +
                   [acc['GBT'][key] for key in gbt_project_ids],
                   fieldnames=project_fields)

def clean_project_id(project_id):
    return project_id.replace('/', '')

def get_coversheet_file(project_id):
    return subprocess.call(['./get_coversheet.sh', project_id]) == 0

def get_coversheet_info(project_id):
    project_id = clean_project_id(project_id)
    coversheets = coversheet.parse('coversheet/%s.xml' % project_id)
    if len(coversheets) > 1:
        print >>sys.stderr, '%s has more than one proposal' % project_id
    elif len(coversheets) == 0:
        return {}
    else:
        return coversheets[0]

def get_authors_file(project_id):
    project_id = clean_project_id(project_id)
    return subprocess.call(['./get_authors.sh', project_id]) == 0

def get_authors_info(project_id, tel=None):
    project_id = clean_project_id(project_id)
    info = get_missing_author(project_id)
    if not info:
        info = authors.parse('author/%s.xml' % project_id)
    # print >>sys.stderr, info
    return info

def get_projects(openfile=sys.stdin):
    return [record for record in csv.DictReader(openfile)]

def resolve_proposal_ids(filepath='projects.csv'):
    return _resolve_proposal_ids(open(filepath))

def _resolve_proposal_ids(openfile=sys.stdin):
    projects = get_projects(openfile)
    resolved_projects = []
    for project in projects:
        proposal_id = project['proposal_id']
        if proposal_id and not project.get('legacy_id', ''):
            print >>sys.stderr, proposal_id
            # remove files manually first... lame, I know.
            get_coversheet_file(proposal_id)
            coversheet = get_coversheet_info(proposal_id)
            project['legacy_id'] = coversheet.get('legacy_id', '')
        resolved_projects.append(project)
    write_projects(resolved_projects, fieldnames=project_fields)

def get_files(filepath='projects.csv'):
    return _get_files(open(filepath))

def _get_files(openfile=sys.stdin):
    projects = get_projects(openfile)
    for project in projects:
        project_id = project['legacy_id']
        get_coversheet_file(project_id)
        get_authors_file(project_id)

def spay_cats(filepath='projects.csv'):
    return _spay_cats(open(filepath))

def _spay_cats(openfile):
    projects = get_projects(openfile)
    split_projects = []
    for project in projects:
        try:
            coversheet = get_coversheet_info(project['legacy_id'])
        except IOError:
            coversheet = {}
        if not coversheet:
            try:
                coversheet = get_coversheet_info(project['proposal_id'])
            except IOError:
                coversheet = {}
        cats = coversheet.get('categories', [])
        count = float(len(cats))
        for cat in cats:
            shared_project = copy.deepcopy(project)
            shared_project['category'] = cat
            for key in ('hours',):
                hours = float(project[key] or 0) / count
                if int(hours) == float(hours):
                    hours = int(hours)
                shared_project[key] = str(hours)
            split_projects.append(shared_project)
        if not cats:
            split_projects.append(project)

    write_projects(split_projects, fieldnames=category_fields)

def share_authors(filepath='projects.csv'):
    return _share_authors(open(filepath))

def _share_authors(openfile=sys.stdin, pi_only=False):
    keys = ('professional_status_type', 'affiliation_name',
            'domestic', 'country',)

    projects = get_projects(openfile)
    new_projects = []
    for project in projects:
        try:
            authors = get_authors_info(project['legacy_id'], tel=project['tel'])
        except IOError:
            authors = []
        try:
            coversheet = get_coversheet_info(project['legacy_id'])
        except IOError:
            coversheet = {}
        if not authors:
            try:
                authors = get_authors_info(project['proposal_id'], tel=project['tel'])
            except IOError:
                authors = []
            try:
                coversheet = get_coversheet_info(project['proposal_id'])
            except IOError:
                coversheet = {}
        legacy_id = coversheet.get('legacy_id', project['legacy_id'])
        if len(authors) > 1 and pi_only:
            pi_id = coversheet.get('pi', '-1')
            authors = [author for author in authors
                       if author.get('astronomer_id', '-2') == pi_id]
        count = len(authors)
        for author in authors:
            for key in keys:
                project[key] = author[key]
            project['legacy_id'] = legacy_id
            iso_country = iso.country_iso.get(project['country'], '')
            project['iso_country'] = iso_country
            new_projects.append(project)
        if not authors:
            new_projects.append(project)

    write_projects(new_projects, fieldnames=author_fields)

def calculate_pi(filepath='projects.csv'):
    return _share_authors(open(filepath), pi_only=True)

commands = {'resolve': resolve_proposal_ids,
            'accumulate': accumulate_projects,
            'get': get_files,
            'category': spay_cats,
            'author': share_authors,
            'pi': calculate_pi,
            }


if __name__ == '__main__':
    command = 'category'
    if len(sys.argv) > 1:
        command = sys.argv[1]
    if commands.has_key(command):
        commands[command]()
    else:
        print >>sys.stderr, 'command not found:', command
