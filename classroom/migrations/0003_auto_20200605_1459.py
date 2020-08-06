# Generated by Django 2.0.1 on 2020-06-05 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_create_initial_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='interests',
        ),
        migrations.AddField(
            model_name='student',
            name='enroll',
            field=models.ManyToManyField(related_name='enroll_students', to='classroom.Subject'),
        ),
    ]
