# Generated by Django 3.1.6 on 2021-03-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managing_deadlines', '0002_auto_20210320_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='course_code',
            field=models.CharField(default='Unnamed assessment type', max_length=254),
        ),
        migrations.AddField(
            model_name='assessment',
            name='course_name',
            field=models.CharField(default='Unnamed assessment type', max_length=254),
        ),
        migrations.AddField(
            model_name='assessment',
            name='deadline_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='assessment',
            name='deadline_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='assessment',
            name='school_name',
            field=models.CharField(default='Unnamed assessment type', max_length=254),
        ),
    ]
