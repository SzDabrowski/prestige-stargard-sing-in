# Generated by Django 4.2.4 on 2023-08-03 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_server', '0002_dancecoursetype_alter_dancecourse_course_choice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DanceCourse',
            new_name='Clients',
        ),
    ]
