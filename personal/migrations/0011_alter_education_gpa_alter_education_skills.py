# Generated by Django 4.2.4 on 2023-08-31 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0010_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='gpa',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='skills',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
