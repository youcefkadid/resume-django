# Generated by Django 4.2.4 on 2023-08-31 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_alter_experience_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='details',
            field=models.TextField(blank=True, max_length=600),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, default='Present'),
        ),
    ]
