# script to start the database with some existing teams for jobs

# Later: Add jobs too to this list.

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

import django
django.setup()
from accounts.models import Team
from jobs.models import Job

def main():

    lipsum_desc = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget rutrum ipsum. Nulla lobortis egestas mattis. Aliquam id luctus ligula. Etiam dignissim convallis purus a lacinia. Nullam quis molestie libero."

    jobs = {
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
        'Backend Developer': {'work_type':"fulltime", 'age':'Legal', 'pay':50000, 'desc':lipsum_desc},
        'Frontend Developer': {'work_type':"fulltime", 'age':'Teenager', 'pay':40000, 'desc':lipsum_desc}, 
        'iOS Developer': {'work_type':"internship", 'age':'Teenager', 'pay':45000, 'desc':lipsum_desc}, 
        'Full-Stack Engineer': {'work_type':"fulltime", 'age':'Legal', 'pay':60000, 'desc':lipsum_desc}, 
        'Graphic Designer': {'work_type':"internship", 'age':'Kiddo', 'pay':30000, 'desc':lipsum_desc}, 
        'Video Editor': {'work_type':"fulltime", 'age':'Kiddo', 'pay':35000, 'desc':lipsum_desc}, 
        'Creative Content Writer': {'work_type':"fulltime", 'age':'Teenager', 'pay':25000, 'desc':lipsum_desc}, 
        'Motion Graphics Animator': {'work_type':"internship", 'age':'Legal', 'pay':40000, 'desc':lipsum_desc}, 
        '3D Designer': {'work_type':"fulltime", 'age':'Teenager', 'pay':40000, 'desc':lipsum_desc}, 
        'Data Analyst': {'work_type':"internship", 'age':'Boomer', 'pay':70000, 'desc':lipsum_desc}, 
        'Risk Analyst': {'work_type':"fulltime", 'age':'Legal', 'pay':80000, 'desc':lipsum_desc}, 
        'BizOp Manager': {'work_type':"fulltime", 'age':'Mid-life crisis', 'pay':70000, 'desc':lipsum_desc}, 
        'HR Manager': {'work_type':"fulltime", 'age':'Boomer', 'pay':60000, 'desc':lipsum_desc}, 
        'Recruiter':{'work_type':"internship", 'age':'Teenager', 'pay':20000, 'desc':lipsum_desc}, 
        'PR Specialist': {'work_type':"fulltime", 'age':'Legal', 'pay':40000, 'desc':lipsum_desc}, 
        'Produt Manager': {'work_type':"fulltime", 'age':'Boomer', 'pay':55000, 'desc':lipsum_desc}, 
        '(Technical) Program Manager': {'work_type':"internship", 'age':'Mid-life crisis', 'pay':65000, 'desc':lipsum_desc}
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
    