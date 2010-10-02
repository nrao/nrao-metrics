import csv

keys = ('professional_status_type', 'affiliation_name', 'country', 'domestic',)

records = [record for record in csv.DictReader(open('projects_collected.csv'))]

projects = {}

def project(name):
    return projects.get(name, [])

for record in records:
    name = record.pop('legacy_id', None)
    listing = project(name)
    new_record = {'legacy_id': name}
    for key in keys:
        new_record[key] = record.get(key, '')
    if new_record not in listing:
        listing.append(new_record)
    projects[name] = listing
