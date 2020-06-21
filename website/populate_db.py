# script to start the database with some existing teams for jobs

# Later: Add jobs too to this list.

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

import django
django.setup()
from accounts.models import Team
from jobs.models import Job

def main():

    lipsum_desc  = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin efficitur non neque rutrum pretium. Vivamus dictum hendrerit mauris eu imperdiet. Donec efficitur consequat lectus, et volutpat lectus condimentum quis. Suspendisse.'

    jobs = {
        "Volunteering" : ["Volunteer", "Enlistee"],
        "Engineering" : ["Backend Developer", "Frontend Developer", "iOS Developer", "Full-Stack Engineer"],
        "Creative" : ["Graphic Designer", "Video Editor", "Creative Content Writer", "Motion Graphics Animator", "3D Designer"],
        "Operations" : ["Data Analyst", "Risk Analyst", "BizOp Manager"],
        "User Growth" : ["HR Manager", "Recruiter", "PR Specialist"],
        "Product" : ["Produt Manager", "(Technical) Program Manager"]
    }
    """
    k = {}
    for a in jobs:
            for j in jobs[a]:
                    k[j] = {}
    print(k)
    """


    gen_jobs = {
        'Volunteer' :{'work_type':"internship", 'age':'teen', 'pay':5000, 'desc':lipsum_desc},
        'Enlistee' : {'work_type':"fulltime", 'age':'teen', 'pay':45000, 'desc':lipsum_desc},
        'Backend Developer': {'work_type':"fulltime", 'age':'legal', 'pay':50000, 'desc':lipsum_desc},
        'Frontend Developer': {'work_type':"fulltime", 'age':'teen', 'pay':40000, 'desc':lipsum_desc}, 
        'iOS Developer': {'work_type':"internship", 'age':'teen', 'pay':45000, 'desc':lipsum_desc}, 
        'Full-Stack Engineer': {'work_type':"fulltime", 'age':'legal', 'pay':60000, 'desc':lipsum_desc}, 
        'Graphic Designer': {'work_type':"internship", 'age':'kiddo', 'pay':30000, 'desc':lipsum_desc}, 
        'Video Editor': {'work_type':"fulltime", 'age':'teen', 'pay':35000, 'desc':lipsum_desc}, 
        'Creative Content Writer': {'work_type':"fulltime", 'age':'teen', 'pay':25000, 'desc':lipsum_desc}, 
        'Motion Graphics Animator': {'work_type':"internship", 'age':'legal', 'pay':40000, 'desc':lipsum_desc}, 
        '3D Designer': {'work_type':"fulltime", 'age':'teen', 'pay':40000, 'desc':lipsum_desc}, 
        'Data Analyst': {'work_type':"internship", 'age':'boomer', 'pay':70000, 'desc':lipsum_desc}, 
        'Risk Analyst': {'work_type':"fulltime", 'age':'legal', 'pay':80000, 'desc':lipsum_desc}, 
        'BizOp Manager': {'work_type':"fulltime", 'age':'mid-life-crisis', 'pay':70000, 'desc':lipsum_desc}, 
        'HR Manager': {'work_type':"fulltime", 'age':'boomer', 'pay':60000, 'desc':lipsum_desc}, 
        'Recruiter':{'work_type':"internship", 'age':'teen', 'pay':20000, 'desc':lipsum_desc}, 
        'PR Specialist': {'work_type':"fulltime", 'age':'legal', 'pay':40000, 'desc':lipsum_desc}, 
        'Produt Manager': {'work_type':"fulltime", 'age':'boomer', 'pay':55000, 'desc':lipsum_desc}, 
        '(Technical) Program Manager': {'work_type':"internship", 'age':'mid-life-crisis', 'pay':65000, 'desc':lipsum_desc},
        }

    def add_team(name):
        d = Team.objects.get_or_create(name=name)[0]
        d.save()
        return d

    def add_job(title, team, work_type, age, pay, desc):
        j, c = Job.objects.get_or_create(title=title, team=team, work_type=work_type, age=age, pay=pay, desc=desc)
        j.save()
        return j

    for tname, jnames in jobs.items():
        t = add_team(tname)
        for jname in jnames:
            jdesc = gen_jobs[jname]
            j = add_job(jname, t, jdesc['work_type'], jdesc['age'], jdesc['pay'], jdesc['desc'])
        
    for t in Team.objects.all():
        for j in Job.objects.filter(team=t):
            print(f'- {t}: {j}')


if __name__ == "__main__":
    print("Initializing population script... ")
    main()
    