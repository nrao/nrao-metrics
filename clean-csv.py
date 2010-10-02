import csv
import sys

if sys.argv > 1:
    filename = sys.argv[1]
else:
    filename = 'projects.csv'

if filename == 'projects_collected.csv':
    fields = ['legacy_id', 'proposal_id', 'professional_status_type',
              'affiliation_name', 'country', 'domestic']
    no_dupes = True
else:
    fields = ['tel', 'legacy_id', 'proposal_id', 'scheduled', 'downtime', 'actual']
    no_dupes = False

print >>sys.stderr, 'Processing', filename
print >>sys.stderr, 'Fields:', ', '.join(fields)
print >>sys.stderr, 'Avoid duplicate rows:', no_dupes

readthis = open(filename)
records = [record for record in csv.DictReader(readthis)]
readthis.close()

writemes = []
for record in records:
    writeme = {}
    for field in fields:
        writeme[field] = record[field].strip().replace('\xA0', '')
        if field == 'legacy_id':
            prev_id = writeme[field]
            writeme[field] = writeme[field].upper().rstrip('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            if prev_id != writeme[field]:
                print >>sys.stderr, 'Stripped %s to %s' % (prev_id, writeme[field])
    if no_dupes:
        if writeme not in writemes:
            writemes.append(writeme)
    else:
        writemes.append(writeme)

writethis = open(filename, 'w')
writethis.write(','.join(fields))
writethis.write('\n')
writer = csv.DictWriter(writethis, fields)
writer.writerows(writemes)
writethis.close()
