# Generated by Django 2.1.5 on 2020-06-18 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='age',
            field=models.CharField(blank=True, choices=[('kiddo', 'Kiddo'), ('Teen', 'Teenager'), ('Legal', 'Legal'), ('Mid-life crisis', 'Mid-Life Crisis'), ('Boomer', 'boomer')], max_length=20, null=True, verbose_name='What age you are bud ?'),
        ),
        migrations.AlterField(
            model_name='job',
            name='work_type',
            field=models.CharField(choices=[('Full-Time', 'fulltime'), ('Internship', 'internship')], max_length=10, verbose_name='What type of an opening suits you ?'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(choices=[('Applied', 'applied'), ('Shorlisted', 'shortlisted'), ('Accepted', 'accepted'), ('Rejected', 'rejected')], default='applied', max_length=20),
        ),
    ]
