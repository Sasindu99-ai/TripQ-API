# Generated by Django 5.0.6 on 2024-06-02 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='setting',
            options={'ordering': ['key']},
        ),
        migrations.AlterModelTable(
            name='setting',
            table='settings',
        ),
    ]
