# Generated by Django 4.2.4 on 2023-08-31 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0011_alter_education_gpa_alter_education_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]