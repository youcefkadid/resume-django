# Generated by Django 4.2.4 on 2023-08-31 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_aboutp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('start_date', models.DateField(default='%m-%Y')),
                ('end_date', models.DateField(default='%m-%Y')),
                ('details', models.TextField(max_length=600)),
            ],
        ),
    ]