# Generated by Django 3.1.3 on 2020-11-13 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('can_get_name', 'Can get a name'),)},
        ),
    ]
