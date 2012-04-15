#! /Users/cgilmer/Projects/github/wedding/env/bin/python

import csv
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from apps.rsvp.models import Group


def main():
    writer = csv.writer(open('maps.csv', 'wb'), delimiter=' ',
                                 quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Address', 'City', 'State', 'Zipcode', 'Name', 'Phone Number', 'Group', 'URL', 'Email'])
    
    
    for group in Group.objects.all():
        writer.writerow([
            group.address,
            group.city,
            group.state,
            group.zipcode,
            group.name,
            group.phone,
            group.get_party_display(),
            '',
            group.email,
                             ])


if __name__ == '__main__':
    main()
