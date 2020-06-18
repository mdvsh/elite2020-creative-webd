# script to start the database with some existing teams for jobs

# Later: Add jobs too to this list.

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

import django
django.setup()
from accounts.models import Team

def main():
    depts = ['Engineering', 'Creative Team', 'Execution', 'User Growth', 'Product']
    
    def add_dept(name):
        d = Team.objects.get_or_create(name=name)[0]
        d.save()
        return d

    for dept in depts:
        d = add_dept(dept)
        print(f'- Added Team: {d}')
    
if __name__ == "__main__":
    print("Initializing Team/Department initializing script... ")
    main()
    