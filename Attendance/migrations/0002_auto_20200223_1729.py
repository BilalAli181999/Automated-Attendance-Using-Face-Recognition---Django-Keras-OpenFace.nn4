# Generated by Django 3.0.2 on 2020-02-23 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='id',
        ),
        migrations.AlterField(
            model_name='admin',
            name='Username',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]