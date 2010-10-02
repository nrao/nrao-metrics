#!/usr/bin/env python
# gbt-report: build a HTML table of project info in a given quarter

import csv
import sys

from jinja2 import Template

import proposals

template = Template("""
  <style type="text/css">

    table {
        border-width: 0px;
        border-style: solid;
        border-color: gray;
        width=100%;
        border-collapse: collapse;
        font-family: "Times New Roman";
    }

    th {
        font-size: 12px;
        font-style: bold;
        border-style: none;
    }

    td {
        padding: 5px;
        font-size: 12px;
        border-width: 1px;
        border-style: solid;
    }

    .col1 {
        width: 10px;
    }

    .col3, .col4 {
        width: 20px;
    }

  </style>

  <table>
    <tr><th>No.</th>
    <th>Observer(s)</th>
    <th>Programs</th>
    <th>Hours Allotted</th></tr>
    {% for k in projects %}
      <tr>{% for elem in k %}
           <td class="col{{ loop.index }}">{{ elem }}</td>
          {% endfor %}</tr>
        {%  endfor %}</table> """)

def get_projects(quarter_name=None):
    "Get project name,hour pairs for given quarter, default: latest quarter."
    projects = []
    for project in csv.DictReader(open('projects.csv')):
        if project.get('tel', '').upper() != 'GBT':
            continue
        if project.get('legacy_id'):
            name = project.get('legacy_id', '')
        else:
            name = project.get('proposal_id', '')
        projects.append((name, project.get('hours', 0),))
    return projects

def get_details(projects):
    "Fill in given projects with details from proposal."
    details = []
    for project in projects:
        project_name, project_hours = project
        proposal_info = proposals.get(project_name)
        if not proposal_info:
            print >>sys.stderr, 'no proposal info for', project_name
            details.append([project_name, '', '', project_hours])
        else:
            project_name = proposal_info.get('proposal_id', project_name)
            details.append([project_name,
                            '<br/>'.join(proposal_info['investigators']),
                            proposal_info['title'],
                            project_hours])
    return details

def main():
    if len(sys.argv) > 1:
        quarter_name = sys.argv[1]
    else:
        quarter_name = ''

    # 1. Get names, hours
    projects = get_projects(quarter_name)

    # 2. Get project info
    details = get_details(projects)

    # 3. build html table
    report = template.render(projects=details)

    # 4. output formatted html
    print report

if __name__ == "__main__":
    main()
