# script to start the database with some existing departments for jobs

# Later: Add jobs too to this list.

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

import django
django.setup()
from accounts.models import Department

def main():
    depts = ['Engineering', 'Creative Team', 'Execution', 'User Growth', 'Product']
    
    def add_dept(name):
        d = Department.objects.get_or_create(name=name)[0]
        d.save()
        return d

    for dept in depts:
        d = add_dept(dept)
        print(f'- Added Department: {d}')
    
if __name__ == "__main__":
    print("Initializing department initializing script... ")
    main()
    