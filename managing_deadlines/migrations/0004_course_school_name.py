# Generated by Django 3.1.6 on 2021-03-20 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managing_deadlines', '0003_auto_20210320_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='school_name',
            field=models.CharField(default='Unnamed assessment type', max_length=254),
        ),
    ]
